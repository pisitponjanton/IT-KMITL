#include <WiFiS3.h>
#include <MQTTClient.h>
#include <Arduino.h>

// ------------------- ตัวแปรหลัก -------------------
WiFiClient net;
MQTTClient client(256);

String currentSubTopic = "";
String lastReceivedTopic = "";
String lastReceivedPayload = "";

// ค่าที่ส่งขึ้น web
float web = 0;

unsigned long lastMillis = 0;
int n = 0;

int led = 3;
int pin = A0;
int trigPin = 9;
int echoPin = 10;

// กำหนดรูปแบบการเปิดไฟของแต่ละเลข (0–9)
int num_array[10][7] = {
  { 1, 1, 1, 1, 1, 1, 0 },  // 0
  { 0, 1, 1, 0, 0, 0, 0 },  // 1
  { 1, 1, 0, 1, 1, 0, 1 },  // 2
  { 1, 1, 1, 1, 0, 0, 1 },  // 3
  { 0, 1, 1, 0, 0, 1, 1 },  // 4
  { 1, 0, 1, 1, 0, 1, 1 },  // 5
  { 1, 0, 1, 1, 1, 1, 1 },  // 6
  { 1, 1, 1, 0, 0, 0, 0 },  // 7
  { 1, 1, 1, 1, 1, 1, 1 },  // 8
  { 1, 1, 1, 0, 0, 1, 1 }   // 9
};

// ------------------- ฟังก์ชันเชื่อมต่อ Wi-Fi -------------------
void connectToWiFi(const char* ssid = "iPhoner", const char* password = "top44444") {
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
}

// ------------------- ฟังก์ชัน callback เมื่อมีข้อความเข้า -------------------
void onMessageReceived(String& topic, String& payload) {
  lastReceivedTopic = topic;
  lastReceivedPayload = payload;

  if (topic == currentSubTopic) {
    if (payload == "on") {
      digitalWrite(LED_BUILTIN, HIGH);
    } else if (payload == "off") {
      digitalWrite(LED_BUILTIN, LOW);
    }
  }
}

// ------------------- ฟังก์ชันเชื่อมต่อ MQTT -------------------
void connectToMQTT(const char* broker = "phycom.it.kmitl.ac.th",
                   int port = 1883,
                   const char* clientID = "ArduinoClient67070119",
                   const char* subTopic = "67070119/venus") {
  client.begin(broker, port, net);
  client.onMessage(onMessageReceived);

  while (!client.connect(clientID)) {
    delay(1000);
  }

  client.subscribe(subTopic);
  currentSubTopic = subTopic;
}

// ------------------- ฟังก์ชันส่งข้อมูลไป MQTT -------------------
void publishToMQTT(const char* topic, const String& value) {
  client.publish(topic, value);
}

// ------------------- ฟังก์ชันรับค่าจาก MQTT -------------------
String getMQTTMessage() {
  return lastReceivedPayload;
}

// ------------------- ฟังก์ชันรับชื่อ topic ล่าสุด -------------------
String getMQTTTopic() {
  return lastReceivedTopic;
}

// ------------------- ฟังก์ชันอ่านอุณหภูมิ -------------------
float readTemperature(int pin = pin) {
  int sensorValue = analogRead(pin);             // อ่านค่าจากขา A0
  float voltage = sensorValue * (5.0 / 1023.0);  // แปลงเป็นแรงดันไฟฟ้า (โวลต์)
  float temperatureC = (voltage - 0.5) * 100.0;  // แปลงเป็นอุณหภูมิ (°C)
  return temperatureC;                           // คืนค่าเป็น float
}

// ฟังก์ชันอ่านค่าอุณหภูมิจาก Thermistor (NTC แบบ 10k)
float readThermistor(int pin = pin) {
  // ==== ปรับค่าตามวงจรจริงที่คุณใช้ ====
  const float VCC = 5;                 // ⚡ ถ้าใช้ UNO (5V) ให้เปลี่ยนเป็น 5.0
  const float R_FIXED = 10000.0;       // ⚙️ ตัวต้านทานคงที่ (10kΩ)
  const float B_COEFFICIENT = 3380.0;  // 🧩 ค่า Beta (ลอง 3950, 3435, 3380)
  const float R0 = 10000.0;            // Ω ของ thermistor ที่ 25°C
  const float T0 = 25.0 + 273.15;      // 25°C → 298.15 K

  // ==== อ่านค่า ADC ====
  int adcValue = analogRead(pin);
  if (adcValue <= 0) return -100.0;

  // ==== คำนวณความต้านทาน ====
  float Vout = (adcValue * VCC) / 1023.0;
  if (Vout <= 0 || Vout >= VCC) return -100.0;
  float R_thermistor = (Vout * R_FIXED) / (VCC - Vout);

  // ==== คำนวณอุณหภูมิ (°C) ====
  float tempK = 1.0 / ((1.0 / T0) + (1.0 / B_COEFFICIENT) * log(R_thermistor / R0));
  return tempK - 273.15;
}

// ฟังก์ชันอ่านระยะทางจาก Ultrasonic Sensor (HC-SR04)
float readUltrasonic(int trigPin = trigPin, int echoPin = echoPin) {
  // สร้างพัลส์สั้น ๆ 10 µs เพื่อเริ่มการวัด
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // อ่านค่าระยะเวลาที่เสียงเดินทางไป-กลับ (microseconds)
  long duration = pulseIn(echoPin, HIGH, 30000);  // timeout 30ms (≈5m)

  // คำนวณระยะทางในหน่วยเซนติเมตร
  float distanceCm = duration * 0.034 / 2.0;

  return distanceCm;  // ✅ คืนค่าระยะทาง (cm)
}

// ฟังก์ชันควบคุมความสว่าง LED ด้วย Potentiometer
int controlLEDWithPot(int pin = pin, int potPin = led) {
  delay(10);
  // อ่านค่าจาก potentiometer (0–1023)
  int potValue = analogRead(pin);

  // แปลงค่าเป็นช่วง 0–255 สำหรับ PWM
  int brightness = potValue / 4;  // (1023 ÷ 4 ≈ 255)

  // เขียนค่า PWM ไปยังขา LED
  analogWrite(potPin, brightness);
  return potValue;
}

// ------------------- ฟังก์ชันแสดงเลขบน 7-segment -------------------
void display7Segment(int digit, int pins[7]) {
  if (digit < 0 || digit > 9) return;  // ป้องกันค่าผิดพลาด

  // เขียนค่า HIGH/LOW ไปยังแต่ละขา segment
  for (int i = 0; i < 7; i++) {
    digitalWrite(pins[i], num_array[digit][i]);
  }
}

int segmentPins[8] = { 2, 3, 4, 5, 6, 7, 8, 9 };  // a,b,c,d,e,f,g,จุด

// ------------------- Setup -------------------
void setup() {
  Serial.begin(9600);

  pinMode(led, OUTPUT);  //3

  pinMode(pin, OUTPUT);  //A0

  pinMode(trigPin, OUTPUT);  //9
  pinMode(echoPin, INPUT);   //10

  // กำหนดเลขบน 7-segment ทุกขาเป็น OUTPUT
  for (int i = 0; i < 8; i++) {
    pinMode(segmentPins[i], OUTPUT);
  };

  connectToWiFi();
  connectToMQTT();
}

// ------------------- Loop -------------------
void loop() {
  client.loop();

  if (!client.connected()) {
    connectToMQTT();
  }

  // ส่งขึ้นเว็บ
  if (millis() - lastMillis > 1000) {
    lastMillis = millis();
    publishToMQTT("67070119/temp", String(web));
  }

  String msg = getMQTTMessage();
  //ฟังก์ชันอ่านอุณหภูมิ
  // float tem = readTemperature(); pin->A0

  // ฟังก์ชันอ่านค่าอุณหภูมิจาก Thermistor (NTC แบบ 10k) pin->A0
  // float tem = readThermistor();

  // // ฟังก์ชันอ่านระยะทางจาก Ultrasonic Sensor trigPin->9 , echoPin->10
  // float tem = readUltrasonic();

  // ฟังก์ชันควบคุมความสว่าง LED ด้วย Potentiometer pin->A0, potPin->3(ต่อไฟ LED)
  // float tem = controlLEDWithPot();

  for (int d = 0; d < 10; d++) {
    display7Segment(d, segmentPins);
    delay(1000);
  }
  // Serial.println(tem);
  // web = tem;
}

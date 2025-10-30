#include <WiFiS3.h>
#include <MQTTClient.h>
#include <Arduino.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

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

int red = 11;
int blue = 12;
int green = 13;

int button = 2;

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

// Custom Font รูปหัวใจ ♥
byte heart[8] = {
  0b00000,
  0b01010,
  0b11111,
  0b11111,
  0b01110,
  0b00100,
  0b00000,
  0b00000
};

// Custom Font องศา °
byte degreeSymbol[8] = {
  0b00111,
  0b00101,
  0b00111,
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b00000
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
  if (millis() - lastMillis > 500) {
    lastMillis = millis();
    client.publish(topic, value);
  }
}

// ------------------- ฟังก์ชันรับค่าจาก MQTT -------------------
String getMQTTMessage() {
  return lastReceivedPayload;
}

// ------------------- ฟังก์ชันรับชื่อ topic ล่าสุด -------------------
String getMQTTTopic() {
  return lastReceivedTopic;
}

// ------------------- ฟังก์ชันแปลงอุณหภูมิ เช่น F, K, R,-------------------
float convertTemperature(float celsius, char unit) {
  switch (unit) {
    case 'F': return (celsius * 9.0 / 5.0) + 32.0;    // Fahrenheit
    case 'K': return celsius + 273.15;                // Kelvin
    case 'R': return (celsius + 273.15) * 9.0 / 5.0;  // Rankine
    case 'E': return celsius * 4.0 / 5.0;             // Reaumur
    default: return celsius;                          // Celsius
  }
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

// ฟังก์ชันคุมสี LED  RGB Common Anode ใส่ค่่าแค่ 0 -> LOW และ 1 -> HIGH
void setColorRGB(int r, int g, int b) {
  // red	setColorRGB(1,0,0);
  // green	setColorRGB(0,1,0);
  // blue	setColorRGB(0,0,1);
  // yellow	setColorRGB(1,1,0);
  // magenta	setColorRGB(1,0,1);
  // cyan	setColorRGB(0,1,1);
  // white	setColorRGB(1,1,1);
  // ปิด	setColorRGB(0,0,0);

  digitalWrite(red, r ? LOW : HIGH);  // Common Anode → LOW = ติด
  digitalWrite(green, g ? LOW : HIGH);
  digitalWrite(blue, b ? LOW : HIGH);
}

// ฟังก์ชันอ่านสถานะปุ่ม ใส่ค่าปุ่มที่ต้องการ set
int readButton(int pin = button) {
  static unsigned long lastPress = 0;
  const unsigned long debounceDelay = 50;  // หน่วงกันเด้ง 50ms

  int state = digitalRead(pin);

  // ใช้ INPUT_PULLUP → ปกติ HIGH, กดแล้ว LOW
  if (state == LOW && millis() - lastPress > debounceDelay) {
    lastPress = millis();
    return 1;  // ✅ มีการกดปุ่ม
  }
  return 0;  // ❌ ยังไม่กด
}

// ------------------- ฟังก์ชันแสดงเลขบน 7-segment -------------------
void display7Segment(int digit, int pins[7]) {
  if (digit < 0 || digit > 9) return;  // ป้องกันค่าผิดพลาด

  // เขียนค่า HIGH/LOW ไปยังแต่ละขา segment
  for (int i = 0; i < 7; i++) {
    digitalWrite(pins[i], num_array[digit][i]);
  }
}

// ------------------- กำหนด LCD -------------------
LiquidCrystal_I2C lcd(0x27, 16, 2);
// 📌 ถ้าไม่ขึ้น ให้ลองเปลี่ยนเป็น 0x3F (บางบอร์ดใช้ address นี้)

// ------------------- ฟังก์ชันส่งข้อความ -------------------
void printLCD(String text, int col = 0, int row = 0) {
  lcd.setCursor(col, row);  // ตั้งตำแหน่ง (คอลัมน์, แถว)
  lcd.print(text);          // แสดงข้อความ
}

// ------------------- ฟังก์ชันส่งตัวเลข -------------------
void printLCDint(float text, int col = 0, int row = 0) {
  lcd.setCursor(col, row);  // ตั้งตำแหน่ง (คอลัมน์, แถว)
  lcd.print(text, 2);       // แสดงทศนิยม 2 ตำแหน่ง
}

// ------------------- ฟังก์ชันโจทย์ Mock Exam Subscribe ข้อ 1-------------------
void mockExamSubscribe_1(int value) {
  int red_led = red;
  int blue_led = blue;
  int green_led = green;
  digitalWrite(red_led, LOW);
  digitalWrite(blue_led, LOW);
  digitalWrite(green_led, LOW);

  Serial.println(value);

  if (value >= 10 && value <= 25) {
    digitalWrite(green_led, HIGH);
  } else if (value >= 26 && value <= 35) {
    digitalWrite(blue_led, HIGH);
  } else if (value >= 36 && value <= 50) {
    digitalWrite(red_led, HIGH);
  }
}

// ------------------- ฟังก์ชันโจทย์ Mock Exam อ่านค่าจาก Sensor อุณหภูมิ -------------------
void mockExamPublish_1() {
  float tem = readTemperature();
  publishToMQTT("67070119/temp", String(tem));
}

// ------------------- ฟังก์ชันโจทย์ Mock Exam อ่านค่าจาก ตัวต้านทานปรับค่าได้ แล้วแสดงค่า (0-1023)-------------------
void mockExamPublish_2() {
  float tem = controlLEDWithPot();
  publishToMQTT("67070119/light", String(tem));
}

// ------------------- ฟังก์ชันโจทย์ Mock Exam อ่านค่าระยะทางจาก Ultrasonic หน่วยเป็น cm-------------------
void mockExamPublish_3() {
  float tem = readUltrasonic();
  if (tem > 20) {
    publishToMQTT("67070119/food", "off");
  }
  Serial.println(tem);
}

int segmentPins[8] = { 2, 3, 4, 5, 6, 7, 8, 9 };  // a,b,c,d,e,f,g,จุด

// ------------------- Setup -------------------
void setup() {
  Serial.begin(9600);

  pinMode(led, OUTPUT);  //3

  pinMode(red, OUTPUT);    //11
  pinMode(blue, OUTPUT);   //12
  pinMode(green, OUTPUT);  //13

  pinMode(pin, OUTPUT);  //A0

  pinMode(trigPin, OUTPUT);  //9
  pinMode(echoPin, INPUT);   //10

  pinMode(button, INPUT_PULLUP);  //2

  // กำหนดเลขบน 7-segment ทุกขาเป็น OUTPUT
  for (int i = 0; i < 8; i++) {
    pinMode(segmentPins[i], OUTPUT);
  };

  // set LCD
  // lcd.init();       // เริ่มต้น LCD
  // lcd.backlight();  // เปิดไฟพื้นหลัง
  // lcd.clear();      // ล้างหน้าจอ
  // lcd.createChar(0, heart);
  // lcd.createChar(1, degreeSymbol);
  // printLCD("Hello LCD!", 0, 0);
  // printLCD("Arduino Ready", 0, 1);

  connectToWiFi();
  connectToMQTT();
}

// ------------------- Loop -------------------
void loop() {
  client.loop();

  if (!client.connected()) {
    //ต่อ wifi
    connectToMQTT();
  }

  // ส่งขึ้นเว็บ
  //   publishToMQTT("67070119/temp", String(web));

  //ฟังก์ชันรับค่าจาก web dataType เป็น String
  String msg = getMQTTMessage();


  //ฟังก์ชันโจทย์ Mock Exam Subscribe ข้อ 1
  // mockExamSubscribe_1(msg.toInt());

  //ฟังก์ชันโจทย์ Mock Exam อ่านค่าจาก Sensor อุณหภูมิ
  mockExamPublish_1();

  //ฟังก์ชันโจทย์ Mock Exam อ่านค่าจาก ตัวต้านทานปรับค่าได้ แล้วแสดงค่า (0-1023)
  // mockExamPublish_2();

  //ฟังก์ชันโจทย์ Mock Exam อ่านค่าระยะทางจาก Ultrasonic หน่วยเป็น cm
  // mockExamPublish_3();

  //ฟังก์ชันอ่านอุณหภูมิ
  // float tem = readTemperature(); pin->A0

  // ฟังก์ชันอ่านค่าอุณหภูมิจาก Thermistor (NTC แบบ 10k) pin->A0
  // float tem = readThermistor();

  // ฟังก์ชันอแปลงอุณหภูมิหน่วยใส่ค่า C -> F, K, R, E
  // float tem_covert convertTemperature(tem, 'F');


  // // ฟังก์ชันอ่านระยะทางจาก Ultrasonic Sensor trigPin->9 , echoPin->10
  // float tem = readUltrasonic();

  // ฟังก์ชันควบคุมความสว่าง LED ด้วย Potentiometer pin -> A0, potPin -> 3(ต่อไฟ LED)
  // float tem = controlLEDWithPot();

  // loop เลข 1 - 10
  // for (int d = 0; d < 10; d++) {
  // // ฟังก์ชันแสดงเลขบน 7-segment d->ตัวเลขที่ต้องการให้แสดง segmentPing -> ค่าแต่ละขา
  //   display7Segment(d, segmentPins);
  //   delay(1000);
  // }

  // ฟังก์ชันคุมสี LED  RGB Common Anode ใส่ค่่าแค่ 0 -> LOW และ 1 -> HIGH
  // setColorRGB(1, 0, 1);

  // readButton จะให้ใส่ค่าปุ่มที่ต่อลงไปเช่น จะต่อกับ 3 ให้ใส่สามลงไป หมายเหตุ: ถ้าไม่ใส่ค่าเริ่มต้นจะเป็นช่อง 2
  // if (readButton()) {
  //   // ตัวอย่างถ้ากดปุ่มไฟช่อง 11 จะติด
  //   digitalWrite(red, HIGH);
  // }

  // การอัปเดตค่าจอ LCD
  // delay(2000);
  // lcd.clear();
  // printLCD("I LOVE YOU ", 0, 0);
  // lcd.write(byte(0));
  // printLCDint(readTemperature(), 0, 1);
  // printLCD(" C", 6, 1);
  // lcd.write(byte(1));

  // Serial.println(tem);
  // web = tem;
}

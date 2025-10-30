#include <WiFiS3.h>
#include <MQTTClient.h>
#include <Arduino.h>

// ------------------- ตัวแปรหลัก -------------------
WiFiClient net;
MQTTClient client(256);

String currentSubTopic = "";
String lastReceivedTopic = "";
String lastReceivedPayload = "";

unsigned long lastMillis = 0;
int n = 0;

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
float readTemperature(int p = A0) {
  int sensorValue = analogRead(p);               // อ่านค่าจากขา A0
  float voltage = sensorValue * (5.0 / 1023.0);  // แปลงเป็นแรงดันไฟฟ้า (โวลต์)
  float temperatureC = (voltage - 0.5) * 100.0;  // แปลงเป็นอุณหภูมิ (°C)
  return temperatureC;                           // คืนค่าเป็น float
}

// ฟังก์ชันอ่านค่าอุณหภูมิจาก Thermistor (NTC แบบ 10k)
float readThermistor(int pin = A0) {
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
// ------------------- Setup -------------------
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);

  Serial.begin(9600);
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
  if (millis() - lastMillis > 100) {
    lastMillis = millis();
    float tem = readTemperature();
    publishToMQTT("67070119/temp", String(tem));
  }

  String msg = getMQTTMessage();
  float tem = readTemperature();
  // float tem = readThermistor();
  Serial.println(tem);
  n = tem;
}

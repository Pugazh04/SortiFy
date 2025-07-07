#include <WiFi.h> 
#include <ESP_Mail_Client.h> 

const char* ssid = "<add your Wifi ssid>"; 
const char* password = "<add your Wifi password>"; 

#define SMTP_HOST "smtp.gmail.com" 
#define SMTP_PORT 465 
#define SENDER_EMAIL "<add sender email address>" 
#define SENDER_PASSWORD "<add sender password>" 
#define RECIPIENT_EMAIL "<add receiver email address>" 

#define TRIG2 14 
#define ECHO2 15  
#define TRIG3 16  
#define ECHO3 17  
#define TRIG4 18  
#define ECHO4 19  

#define STOP_BUTTON 0  
#define CHECK_INTERVAL 5000  
#define FULL_DISTANCE 4      
SMTPSession smtp; 
volatile bool systemActive = true; 
void IRAM_ATTR stopSystem() { 
systemActive = false; 
Serial.println("\nSYSTEM PAUSED: Press EN button to restart"); 
} 
void setup() { 
Serial.begin(115200); 

pinMode(TRIG2, OUTPUT); 
pinMode(ECHO2, INPUT); 
pinMode(TRIG3, OUTPUT); 
pinMode(ECHO3, INPUT); 
pinMode(TRIG4, OUTPUT); 
pinMode(ECHO4, INPUT); 

pinMode(STOP_BUTTON, INPUT_PULLUP); 
attachInterrupt(digitalPinToInterrupt(STOP_BUTTON), stopSystem, FALLING); 
 
if (systemActive) { 
WiFi.begin(ssid, password); 
Serial.print("Connecting to WiFi"); 
while (WiFi.status() != WL_CONNECTED && systemActive) { 
delay(500); 
Serial.print("."); 
} 
if (systemActive) Serial.println("\nWiFi connected!"); 
} 
} 
float readUltrasonic(int trigPin, int echoPin) { 
digitalWrite(trigPin, LOW); 
delayMicroseconds(2); 
digitalWrite(trigPin, HIGH); 
delayMicroseconds(10); 
digitalWrite(trigPin, LOW); 
long duration = pulseIn(echoPin, HIGH); 
return duration * 0.0343 / 2; 
} 
void sendAlert(String alertType, String details) { 
Session_Config config; 
config.server.host_name = SMTP_HOST; 
config.server.port = SMTP_PORT; 
config.login.email = SENDER_EMAIL; 
config.login.password = SENDER_PASSWORD; 
SMTP_Message message; 
message.sender.name = "Bin Monitoring System"; 
message.sender.email = SENDER_EMAIL; 
message.subject = "[URGENT] " + alertType; 
message.addRecipient("Maintenance Team", RECIPIENT_EMAIL); 
message.text.content = "Alert Details:\n" + details; 
if (smtp.connect(&config)) { 
MailClient.sendMail(&smtp, &message); 
smtp.closeSession();     
Serial.println("Alert email sent!"); 
} 
} 
void loop() { 
if (!systemActive) { 
delay(1000); 
return; 
} 

float bin2 = readUltrasonic(TRIG2, ECHO2); 
float bin3 = readUltrasonic(TRIG3, ECHO3); 
float bin4 = readUltrasonic(TRIG4, ECHO4); 

Serial.println("\n--- Sensor Readings ---"); 
Serial.printf("Bin2: %.1fcm | Bin3: %.1fcm | Bin4: %.1fcm\n", bin2, bin3, bin4); 

String alertDetails = ""; 
bool needsAlert = false; 
if (bin2 < FULL_DISTANCE) { 
alertDetails += "Bin2 FULL (" + String(bin2, 1) + "cm)\n"; 
needsAlert = true;  } 
if (bin3 < FULL_DISTANCE) { 
alertDetails += "Bin3 FULL (" + String(bin3, 1) + "cm)\n"; 
needsAlert = true; 
} 
if (bin4 < FULL_DISTANCE) { 
alertDetails += "Bin4 FULL (" + String(bin4, 1) + "cm)\n"; 
needsAlert = true;} 
if (needsAlert) { 
sendAlert("Bin Overflow Alert", alertDetails); 
} 
delay(CHECK_INTERVAL);}

#include "esp_camera.h"
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
const char *ssid = "";
const char *password = "";
const char *commandURL = "";
const char *urltosdisplayimage = "";
void capture_image(){
  camera_fb_t * fb = esp_camera_fb_get();
  if (!fb) {
    Serial.println("Camera capture failed");
    return;
  }
  HTTPClient http;
  http.begin(urltosdisplayimage);
  http.addHeader("Content-Type", "image/jpeg");

  int response = http.POST(fb->buf,fb->len);
  Serial.println("Image sent ...");
  Serial.println(response);

  http.end();
  esp_camera_fb_return(fb);

}
void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid, password);
  Serial.print("Connecting");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nConnected!");

}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {

    HTTPClient http;
    http.begin(commandURL);

    int httpCode = http.GET();
    if (httpCode > 0) {
      String payload = http.getString();
      Serial.println("Server Response: " + payload);

      if (payload.indexOf("\"T\"") != -1) {
          Serial.println("Capture Triggered!");
          capture_image();
      }
    }
    http.end();
  }
  delay(2000);
}

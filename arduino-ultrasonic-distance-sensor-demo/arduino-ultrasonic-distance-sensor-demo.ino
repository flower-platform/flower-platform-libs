#include <Arduino.h>
#include <HardwareSerial.h>
#include <stdbool.h>

#include <Timer.h>
#include <UltrasonicDistanceSensor.h>


class AppGen {
public: 
	
	Timer timer;
	UltrasonicDistanceSensor ultrasonicDistanceSensor;

	int distanceIn;
	int distanceCm;

	AppGen()
		: timer(true)
		, ultrasonicDistanceSensor(8,7,200)
	{};

	void timer_onTimer(TimerEvent* event) {
        distanceIn = ultrasonicDistanceSensor.ping_in();
        Serial.print("Ping: ");
        Serial.print(distanceIn);
        Serial.print(" in               ");
        distanceCm = ultrasonicDistanceSensor.ping_cm();
        Serial.print("Ping: ");
        Serial.print(distanceCm);
        Serial.println(" cm");

	}

	void setup() {
		timer.delay = 20;
		timer.onTimer = new DelegatingCallback<AppGen, TimerEvent>(this, &AppGen::timer_onTimer); 


		timer.setup();
	}

	void loop() {
		timer.loop();
	}

};

#include "CustomCode.h"

App app;

void setup() {
	Serial.begin(115200);
	app.setup();
}

void loop() {
	app.loop();
}

#include <Arduino.h>
#include <HardwareSerial.h>
#include <stdbool.h>

#include <NewPing.h>
#include <Timer.h>


class AppGen {
public: 
	
	NewPing newPing;
	Timer timer;

	int distanceIn;
	int distanceCm;
	AppGen() : newPing(8,7,200) {}
			
	void setDistances() {
        distanceIn = newPing.ping_in();
        delay(1000);// Wait 100ms between pings (about 10 pings/sec). 29ms should be the shortest delay between pings;
        distanceCm = newPing.ping_cm();

	}

	void printDistances(int distance, char* type) {
        Serial.print("Ping: ");
        Serial.print(distance);
        Serial.print(" ");
        Serial.println(type);

	}

	void timer_onTimer(TimerEvent* event) {
        setDistances();
        printDistances(distanceIn, "in");
        printDistances(distanceCm, "cm");
        Serial.println("---------------");

	}

	void setup() {

		timer.delay = 20;
		timer.autoStart = true;
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

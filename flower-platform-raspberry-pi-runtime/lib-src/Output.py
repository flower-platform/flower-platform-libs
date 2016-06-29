from FlowerPlatformRuntime import ValueChangedEvent
import RPi.GPIO as GPIO

"""
@component
"""
class Output:

    """    
    @componentAttribute
    """    
    contributesToState = False

    """
    @componentAttribute
    """
    isPwm = False

    """
    @componentAttribute
    """
    pin = None
    
    """    
    @componentHandler
    """    
    onValueChanged = None

    initialValue = GPIO.LOW
    pwm = None

    def setup(self):
    	GPIO.setmode(GPIO.BCM)
    	GPIO.setup(self.pin, GPIO.OUT)
    	GPIO.output(self.pin, self.initialValue)
    	self.lastValue = self.initialValue

    '''
    @componentMethod
    '''
    def setValue(self, value):
    	if self.isPwm:
    	    if self.pwm is None:
    	        self.pwm = GPIO.PWM(self.pin, 1000)
    		self.pwm.start(value)
    	    else:
    		self.pwm.ChangeDutyCycle(value)
    	else:
    	    GPIO.output(self.pin, value)
    
    	if self.onValueChanged is not None:
    	    event = ValueChangedEvent()
    	    event.previousValue = lastValue
    	    event.currentValue = value
    	    self.onValueChanged(event)

        self.lastValue = value


    '''
    @componentMethod
    '''
    def getValue(self):
	   return self.lastValue

    '''
    @componentMethod
    '''
    def toggleHighLow(self):
    	if self.lastValue == GPIO.HIGH:
    	    self.setValue(GPIO.LOW)
    	else:
    	    self.setValue(GPIO.HIGH)
        
    '''
    @componentMethod
    '''
    def getStateAsJson(self):
    	return self.lastValue

    def loop(self) :
        return

    def stop(self) :
        return

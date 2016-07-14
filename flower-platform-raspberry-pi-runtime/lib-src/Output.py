from FlowerPlatformRuntime import ValueChangedEvent
import RPi.GPIO as GPIO

"""
documentation of output
"""
class Output:

    """    
    contributesToState
    """    
    contributesToState = False

    """
    isPwm
    """
    isPwm = False

    """
    pin
    """
    pin = None
    
    """    
    onValueChanged
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
    setValue
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
    getValue
    '''
    def getValue(self):
      return self.lastValue

    '''
    toggleHighLow
    '''
    def toggleHighLow(self):
      if self.lastValue == GPIO.HIGH:
          self.setValue(GPIO.LOW)
      else:
          self.setValue(GPIO.HIGH)
        
    '''
    getStateAsJson
    '''
    def getStateAsJson(self):
      return self.lastValue

    def loop(self) :
      return

    def stop(self) :
      return

from FlowerPlatformRuntime import ValueChangedEvent
import RPi.GPIO as GPIO
import time

"""
@component
"""
class Input :

    lastValue = GPIO.LOW
    lastTime = 0
    
    """    
    @componentAttribute
    """    
    contributesToState = False

    """    
    @componentHandler
    """    
    onValueChanged = None

    """
    @componentAttribute
    """
    pin = None

    """
    @componentAttribute
    """
    pollInterval = 50
    
    """
    @componentAttribute
    """
    internalPullUp = False

    def setup(self) :
      GPIO.setmode(GPIO.BCM)
      if self.internalPullUp :
          GPIO.setup(self.pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
          self.lastValue = GPIO.HIGH
      else :
          GPIO.setup(self.pin, GPIO.IN)
          self.lastValue = GPIO.LOW

    def loop(self) :
      value = GPIO.input(self.pin)

      if value == self.lastValue :
          return
    
      if time.time() * 1000 - self.lastTime < self.pollInterval : 
          return
    
      if self.onValueChanged is not None :
          event = ValueChangedEvent
          event.previousValue = self.lastValue
          event.currentValue = value
          self.onValueChanged(event)
    
      self.lastValue = value
      self.lastTime = time.time() * 1000

    def stop(self) :
      return

    def getStateAsJson(self) :
      return self.lastValue

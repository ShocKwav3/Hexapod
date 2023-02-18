import pca9685
import math
import uasyncio
from time import ticks_us

from transitions import Transitions
from constants import Constants


class Servo:
    _name = ''
    _index = 0
    _invert = False
    _tickStartTime = 0
    _elapsedTime = 0
    _duration = 2 * 1000000
    _currentAngle = None
    _defaulyStartAngle = None
    _targetAngle = 0
    _transitionList = {
        Constants.EASE_IN_OUT_SINE: {
            'function': Transitions().ease_in_out_sine,
            'sleepTime': 0.005
        },
        Constants.EASE_IN_CUBIC: {
            'function': Transitions().ease_in_cubic,
            'sleepTime': 0.001
        },
    }

    def __init__(self, i2c, address=0x40, index=0, invert=False, name='', freq=50, min_us=600, max_us=2400, degrees=180):
        self._name = name
        self._index = index
        self._invert = invert
        self.period = 1000000 / freq
        self.min_duty = self._us2duty(min_us)
        self.max_duty = self._us2duty(max_us)
        self.degrees = degrees
        self.freq = freq
        self.pca9685 = pca9685.PCA9685(i2c, address)
        self.pca9685.freq(freq)

    def _us2duty(self, value):
        return int(4095 * value / self.period)

    def position(self, index, degrees=None, radians=None, us=None, duty=None):
        if self._invert and degrees:
            degrees = 180 - degrees
            print('Inverted Angle => ', degrees)

        span = self.max_duty - self.min_duty
        if degrees is not None:
            duty = self.min_duty + span * degrees / self.degrees

            print("Channel => ", index, " PWM => ", duty)
        elif radians is not None:
            duty = self.min_duty + span * radians / math.radians(self.degrees)
        elif us is not None:
            duty = self._us2duty(us)
        elif duty is not None:
            pass
        else:
            return self.pca9685.duty(index)
        duty = min(self.max_duty, max(self.min_duty, int(duty)))
        self.pca9685.duty(index, duty, self._invert)

    def getPWM(self, channel):
        channelAddress = 0x0A

        print("Channel => ", channel, " Address => ", channelAddress, " PWM => ", self.pca9685._readFromAddress(address=channelAddress))

    def release(self):
        self.pca9685.duty(self._index, 0)

    async def setAngle(self, angle, transition='', id=''):
        print("Setting ", id, ' => ', angle)
        if not transition:
            print("Value without transition => ", angle)
            self.position(index=self._index, degrees=angle)
            return

        transitionAlgorithm = self._transitionList[transition]['function']

        self._tickStartTime = ticks_us()
        self._targetAngle = angle

        while self._elapsedTime < self._duration and self._currentAngle != self._targetAngle:
            if not self._currentAngle:
                self._currentAngle = 0

            newAngle = transitionAlgorithm(
                current_time=self._elapsedTime,
                start_value=self._currentAngle,
                change_in_value=self._targetAngle - self._currentAngle,
                duration=self._duration
            )

            if self._targetAngle < self._currentAngle:
                newAngle -= 1

            self.position(index=self._index, degrees=newAngle)

            self._currentAngle = newAngle
            self._elapsedTime = ticks_us() - self._tickStartTime

            await uasyncio.sleep(self._transitionList[transition]['sleepTime'])

            # print(self._name, ': ', 'Value => ', self._currentAngle)

        self._tickStartTime = 0
        self._elapsedTime = 0
        self._targetAngle = 0

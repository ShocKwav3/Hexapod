import uasyncio
from machine import SoftI2C

from servo import Servo
from config import i2cConfig, defaultStandAngles
from constants import Constants


class Leg:
    _i2cAddress = None
    _legName = ''

    _coxa = None
    _coxaChannel = 0
    _coxaDegreeToAdjust = 0
    _coxaActivityConfig = []
    _coxaIdentifier = ''

    _femur = None
    _femurChannel = 0
    _femurDegreeToAdjust = 0
    _femurActivityConfig = []
    _femurIdentifier = ''

    _tibia = None
    _tibiaChannel = 0
    _tibiaDegreeToAdjust = 0
    _tibiaActivityConfig = []
    _tibiaIdentifier = ''

    def __init__(self, legConfig):
        self._i2cAddress = legConfig[Constants.I2C_ADDRESS]
        self._legName = legConfig[Constants.LEG_NAME]

        self._coxaChannel = legConfig[Constants.COXA][Constants.CHANNEL]
        self._coxaDegreeToAdjust = legConfig[Constants.COXA][Constants.DEGREES_TO_ADJUST]
        self._coxaActivityConfig = legConfig[Constants.COXA][Constants.ACTIVITIES]
        self._coxaIdentifier = self._legName + '_' + legConfig[Constants.COXA][Constants.JOINT_NAME]

        self._femurChannel = legConfig[Constants.FEMUR][Constants.CHANNEL]
        self._femurDegreeToAdjust = legConfig[Constants.FEMUR][Constants.DEGREES_TO_ADJUST]
        self._femurActivityConfig = legConfig[Constants.FEMUR][Constants.ACTIVITIES]
        self._femurIdentifier = self._legName + '_' + legConfig[Constants.FEMUR][Constants.JOINT_NAME]

        self._tibiaChannel = legConfig[Constants.TIBIA][Constants.CHANNEL]
        self._tibiaDegreeToAdjust = legConfig[Constants.TIBIA][Constants.DEGREES_TO_ADJUST]
        self._tibiaActivityConfig = legConfig[Constants.TIBIA][Constants.ACTIVITIES]
        self._tibiaIdentifier = self._legName + '_' + legConfig[Constants.TIBIA][Constants.JOINT_NAME]

        i2c = SoftI2C(sda=i2cConfig[Constants.SDA], scl=i2cConfig[Constants.SCL])

        self._coxa = Servo(
            i2c=i2c,
            address=self._i2cAddress,
            index=self._coxaChannel,
            name=self._coxaIdentifier
        )
        self._femur = Servo(
            i2c=i2c,
            address=self._i2cAddress,
            index=self._femurChannel,
            name=self._femurIdentifier
        )
        self._tibia = Servo(
            i2c=i2c,
            address=self._i2cAddress,
            index=self._tibiaChannel,
            name=self._tibiaIdentifier
        )

    def getJointServoConfig(self, joint):
        jointMap = {
            Constants.COXA: {
                'instance': self._coxa,
                Constants.CHANNEL: self._coxaChannel,
                Constants.DEGREES_TO_ADJUST: self._coxaDegreeToAdjust
            },
            Constants.FEMUR: {
                'instance': self._femur,
                Constants.CHANNEL: self._femurChannel,
            },
            Constants.TIBIA: {
                'instance': self._tibia,
                Constants.CHANNEL: self._tibiaChannel,
            }
        }

        return jointMap[joint]

    async def stand(self):
        await uasyncio.create_task(
            self._coxa.setAngle(
                angle=self.getCalculatedAngle(
                    angle=defaultStandAngles[self._legName][Constants.COXA][0],
                    degreesToAdjust=self._coxaDegreeToAdjust,
                    inverted=self._coxaActivityConfig[Constants.STAND][Constants.INVERTED]
                ),
                transition=Constants.EASE_IN_OUT_SINE,
                id=self._coxaIdentifier
            )
        )
        await uasyncio.create_task(
            self._femur.setAngle(
                angle=self.getCalculatedAngle(
                    angle=defaultStandAngles[self._legName][Constants.FEMUR][0],
                    degreesToAdjust=self._femurDegreeToAdjust,
                    inverted=self._femurActivityConfig[Constants.STAND][Constants.INVERTED]
                ),
                transition=Constants.EASE_IN_OUT_SINE,
                id=self._femurIdentifier
            )
        )
        await uasyncio.create_task(
            self._tibia.setAngle(
                angle=self.getCalculatedAngle(
                    angle=defaultStandAngles[self._legName][Constants.TIBIA][0],
                    degreesToAdjust=self._tibiaDegreeToAdjust,
                    inverted=self._tibiaActivityConfig[Constants.STAND][Constants.INVERTED]
                ),
                transition=Constants.EASE_IN_OUT_SINE,
                id=self._tibiaIdentifier
            )
        )
        await uasyncio.create_task(
            self._femur.setAngle(
                angle=self.getCalculatedAngle(
                    angle=defaultStandAngles[self._legName][Constants.FEMUR][1],
                    degreesToAdjust=self._femurDegreeToAdjust,
                    inverted=self._femurActivityConfig[Constants.STAND][Constants.INVERTED]
                ),
                transition=Constants.EASE_IN_OUT_SINE,
                id=self._femurIdentifier
            )
        )

    async def swing(self):
        await uasyncio.create_task(
            self._femur.setAngle(
                angle=self.getCalculatedAngle(
                    angle=45,
                    degreesToAdjust=self._femurDegreeToAdjust,
                    inverted=self._femurActivityConfig[Constants.SWING][Constants.INVERTED]
                ),
                transition=Constants.EASE_IN_OUT_SINE,
                id=self._femurIdentifier
            )
        )

        await uasyncio.create_task(
            self._coxa.setAngle(
                angle=self.getCalculatedAngle(
                    angle=110,
                    degreesToAdjust=self._coxaDegreeToAdjust,
                    inverted=self._coxaActivityConfig[Constants.SWING][Constants.INVERTED]
                ),
                transition=Constants.EASE_IN_OUT_SINE,
                id=self._coxaIdentifier
            )
        )

        await uasyncio.create_task(
            self._femur.setAngle(
                angle=self.getCalculatedAngle(
                    angle=75,
                    degreesToAdjust=self._femurDegreeToAdjust,
                    inverted=self._femurActivityConfig[Constants.SWING][Constants.INVERTED]
                ),
                transition=Constants.EASE_IN_OUT_SINE,
                id=self._femurIdentifier
            )
        )

    async def stance(self):
        await uasyncio.create_task(
            self._coxa.setAngle(
                angle=self.getCalculatedAngle(
                    angle=70,
                    degreesToAdjust=self._coxaDegreeToAdjust,
                    inverted=self._coxaActivityConfig[Constants.STANCE][Constants.INVERTED]
                ),
                transition=Constants.EASE_IN_OUT_SINE,
                id=self._coxaIdentifier
            )
        )

    async def retract(self):
        await uasyncio.create_task(
            self._femur.setAngle(
                angle=self.getCalculatedAngle(
                    angle=30,
                    degreesToAdjust=self._femurDegreeToAdjust,
                    inverted=self._femurActivityConfig[Constants.SWING][Constants.INVERTED]
                ),
                transition=Constants.EASE_IN_OUT_SINE,
                id=self._femurIdentifier
            )
        )

        await uasyncio.create_task(
            self._coxa.setAngle(
                angle=self.getCalculatedAngle(
                    angle=90,
                    degreesToAdjust=self._coxaDegreeToAdjust,
                    inverted=self._coxaActivityConfig[Constants.STANCE][Constants.INVERTED]
                ),
                transition=Constants.EASE_IN_OUT_SINE,
                id=self._coxaIdentifier
            )
        )

        await uasyncio.create_task(
            self._tibia.setAngle(
                angle=self.getCalculatedAngle(
                    angle=0,
                    degreesToAdjust=self._tibiaDegreeToAdjust,
                    inverted=self._tibiaActivityConfig[Constants.STAND][Constants.INVERTED]
                ),
                transition=Constants.EASE_IN_OUT_SINE,
                id=self._tibiaIdentifier
            )
        )

    async def defaultPosition(self):
        await uasyncio.create_task(self._coxa.setAngle(angle=90 , transition=Constants.EASE_IN_OUT_SINE))
        await uasyncio.sleep(0.5)
        await uasyncio.create_task(self._femur.setAngle(angle=0 , transition=Constants.EASE_IN_OUT_SINE))
        await uasyncio.sleep(0.5)
        await uasyncio.create_task(self._tibia.setAngle(angle=135 , transition=Constants.EASE_IN_OUT_SINE))
        await uasyncio.sleep(0.5)

    async def getBodyLow(self):
        await uasyncio.create_task(self._femur.setAngle(angle=70 , transition=Constants.EASE_IN_OUT_SINE))
        await uasyncio.create_task(self._coxa.setAngle(angle=90 , transition=Constants.EASE_IN_OUT_SINE))

    def getPWM(self, joint):
        jointConfig = self.getJointServoConfig(joint)

        jointConfig['instance'].getPWM(channel=jointConfig[Constants.CHANNEL])

    def directJointControl(self, joint, angle):
        jointConfig = self.getJointServoConfig(joint)

        # adjustedAngle = angle + jointConfig[Constants.DEGREES_TO_ADJUST]

        # print("Setting to => ", adjustedAngle)

        jointConfig['instance'].position(index=jointConfig[Constants.CHANNEL], degrees=angle)

    def getAdjustedAngle(self, angle, degreesToAdjust):
        return min(180, max(angle + degreesToAdjust, 0))

    def getInvertedAngle(self, angle):
        return 180 - angle

    def getCalculatedAngle(self, angle, degreesToAdjust, inverted=False):
        if inverted:
            angle = self.getInvertedAngle(angle=angle)

        return self.getAdjustedAngle(angle=angle, degreesToAdjust=degreesToAdjust)


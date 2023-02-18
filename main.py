import uasyncio

from leg import Leg
from config import legs
from constants import Constants


legA = Leg(legConfig=legs[Constants.LEG_RIGHT_A])
legB = Leg(legConfig=legs[Constants.LEG_RIGHT_B])
legC = Leg(legConfig=legs[Constants.LEG_RIGHT_C])
legD = Leg(legConfig=legs[Constants.LEG_LEFT_D])
legE = Leg(legConfig=legs[Constants.LEG_LEFT_E])
legF = Leg(legConfig=legs[Constants.LEG_LEFT_F])

async def stand():
    """await uasyncio.gather(
        legA.stand(),
        legB.stand(),
        legC.stand()
    )

    await uasyncio.gather(
        legD.stand(),
        legE.stand(),
        legF.stand()
    )"""

    await uasyncio.gather(
        legA.stand(),
        legB.stand(),
        legC.stand(),
        legD.stand(),
        legE.stand(),
        legF.stand()
    )

    await uasyncio.sleep(1)

async def layRetracted():
    await uasyncio.gather(
        legA.retract(),
        legB.retract(),
        legC.retract(),
        legD.retract(),
        legE.retract(),
        legF.retract(),
    )

async def walk():
    await uasyncio.gather(
        legA.swing(),
        legB.stance(),
        legC.swing(),
        legD.stance(),
        legE.swing(),
        legF.stance()
    )

    await uasyncio.gather(
        legA.stance(),
        legB.swing(),
        legC.stance(),
        legD.swing(),
        legE.stance(),
        legF.swing(),
    )

    await uasyncio.sleep(0.5)

async def main():
    await uasyncio.create_task(stand())

    for x in range(3):
        await uasyncio.create_task(walk())

    await uasyncio.create_task(layRetracted())

uasyncio.run(main())


# ws://192.168.1.122:8266


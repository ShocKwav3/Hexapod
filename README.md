# Hexapod
Just a hobby project, because it's cool

Body and construction is based on [this cool hexapod project](https://github.com/SmallpTsai/hexapod-v2-7697). Electronics are conceptually almost the same as the original project uses.

Code written by me, this was the main goal for this robot.

## Pre-requisites

Before proceeding, the following needs to be ready. Some of them are not mandatory, such as [pymakr-vsc](https://github.com/pycom/pymakr-vsc), but it sure makes development hassle free.

### Software
 - [VSCode](https://code.visualstudio.com/)
    - Better to keep [Thonny](https://thonny.org/) around too. I found it being very consistant and reliable when in doubt about connectivity.
 - [Micropython](https://micropython.org/)
    - For the microcontroller
    - My board is a [LilyGo TTGO ESP32 S2](http://www.lilygo.cn/prod_view.aspx?TypeId=50063&Id=1300&FId=t3:50063:3) which needs a micropython [version that supports esp32-s2](https://micropython.org/download/GENERIC_S2/)
 - [pymakr 2 for VSCode](https://github.com/pycom/pymakr-vsc)
    - For live coding, syncing, reboot, soft reboot etc. with the microcontroller
    - Optional. Thonny can do all of it but I like VSCode's appearance and it's features more.

### Hardware
 - A suitable microcontroller with WiFi and bluetooth
    - I went with [LilyGo TTGO ESP32 S2](http://www.lilygo.cn/prod_view.aspx?TypeId=50063&Id=1300&FId=t3:50063:3)
 - Physical parts. All are available in the reference repository mentioned above. The author was generous enough to make the 3d files available in thingiverse as well.
 - 18 Servos, at-least, to begin with since it's a 18-DOF robot.
    - I went with [tower pro mg92b](https://www.towerpro.com.tw/product/mg92b/)
    - Different servos would require the 3d files to be modified to support their dimensions
 - Multi channel servo driver
    - I went with the obvious PCA9685
        - I needed two, since each of them supports 16 channels.
        - One of their I2C address must be changed. See `config.py`. [How-to](https://learn.adafruit.com/16-channel-pwm-servo-driver/chaining-drivers).
        - I used 9 from each. Maybe I will drive some leds with the free ones later.
    - Optional if the microcontroller has enough pins and a power supply to be designed in such case
 - Power supply.
    - Mainly a battery that is capable of supplying required power for the whole system. I used a 3S 2200mAh 30C LiPo that I had lying around from my rc hobby.
    - I went with a mini360 buck converter for the microcontroller
    - I chose [this 10A buck converter](https://www.ebay.de/itm/402319289990) to power the servos

## Local setup

Few mandatory things and some convenient tools are needed to be setup to make life easier.

 - pymakr 2 should be [setup with VSCode](https://www.donskytech.com/micropython-using-vscode-pymakr-on-esp32-esp8266/)
 - While it's optional, it's good to [setup thonny](https://randomnerdtutorials.com/getting-started-thonny-micropython-python-ide-esp32-esp8266/) as well incase pymakr gives trouble, which is probable when a new update drops for VSCode
 - Also optional but nice to [setup webrepl](https://www.techcoil.com/blog/how-to-setup-micropython-webrepl-on-your-esp32-development-board/) since it serves as a wireless connection point where we can upload code.
    - by this point, REPL can be easily accessed using thonny or pymakr-vsc
    - `boot.py` seems to be a good place for it right after WiFi setup
 - Nodejs should be installed for pymakr to work
 - Micropython, on the microcontroller, should be [installed using esptools](https://www.embedded-robotics.com/esp8266-micropython/)
 - Rename `secretConfigs.sample.py` to `secretConfigs.py` and populate the values
 - Map joints and update values in `config.py`

## Troubleshooting
 - pymakr was a nightmere to work with for me and resorted to thonny and webrepl (yes one is enough). pymakr 2 seemed to be much better. Although I ran into [this problem](https://github.com/pycom/pymakr-vsc/issues/253), the solution there did the trick for me. The thread has some explanation as well.

# ESP8266 Ecomontoring project
Ecological monitorng using ESP8266 and MicroPython

This repository represents code for ecological monitoring station based on ESP8266 (LoLin NodeMCU v3 version), MQ gas sensors 
and Shinyei PPD42 sensor. 

All scripts are written on Python for MicroPython interpreter.

## Contents

### MQ_Base.py

Base class to deal with MQ gas sensor. Represents all functions needed; constants to calculate exact amount of gas are defined
in sub-classes:
1. MQ4 - Methane
2. MQ7 - CO
3. MQ131 - Ozone
4. MQ136 - H2S

Concentration of gases is calculated in ppm values.

MQ_Base.py strongly refers to https://github.com/rubfi/MQ135 repo, please check it out.

### PPD42.py

MicroPython lib to deal with Shinyei PPD42 dust sensor. 

Measuring particles with Shinyei PPD42 sensor is based on calculating Low Pulse Occupance of sensor output signal during 
30 seconds period. Currently this function of Python lib were implemented:
* [x] Input signal reading
* [x] LPO calculation
* [ ] Convertation of LPO value to actual concentration value

### multiplexor.py

MicroPython lib to deal with analog multiplexors.


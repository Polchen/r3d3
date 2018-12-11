#!/usr/bin/env python3
import time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import TouchSensor, LightSensor, ColorSensor

ls_rechts = LightSensor(INPUT_1)
RECHTER_WERT = ls_rechts.reflected_light_intensity # Wert des rechten Sensors
ls_links = LightSensor(INPUT_2)
LINKER_WERT = ls_links.reflected_light_intensity # Wert des linken Sensors
ls_mitte=ColorSensor(INPUT_3)
MITTE_WERT = ls_mitte.reflected_light_intensity #Wert des mittleren Sensors

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B) # Motoren (links, rechts)

#time.time = 1 hat auch irgendwie funkrioniert 

def main():
    a = -25 #inneres kurvenrad für starke kurve
    b1 = 5
    b = 25 #äußeres Kurvenrad
    c = 30
    d = 3 #inneres kurvenrad für leichte kurve
    
    while True: #Zeilenumbrüche fehlen noch
        """if i >= 140:
            i = 0
        if j >= 140:
            j = 0"""
        if (LINKER_WERT - RECHTER_WERT) > 8 and (LINKER_WERT - MITTE_WERT) > 8: #leicht rechts
            tank_drive.on(SpeedPercent(d), SpeedPercent(b))
            MANÖVER = tank_drive.on(SpeedPercent(d), SpeedPercent(b))
            """i = i+1
            j = 0"""

        elif (LINKER_WERT - RECHTER_WERT) > 8 and (LINKER_WERT - MITTE_WERT) <= 6: #stark rechts
            tank_drive.on(SpeedPercent(a), SpeedPercent(b1))
            MANÖVER = tank_drive.on(SpeedPercent(a), SpeedPercent(b1))
            """i = i+1
            j = 0"""
        
        elif (RECHTER_WERT - LINKER_WERT) > 8 and (RECHTER_WERT - MITTE_WERT) > 8: #leicht links
            tank_drive.on(SpeedPercent(b), SpeedPercent(d))
            MANÖVER = tank_drive.on(SpeedPercent(b), SpeedPercent(d))
            """j += 1
            i = 0"""

        elif (RECHTER_WERT - LINKER_WERT) > 8 and (RECHTER_WERT - MITTE_WERT) <= 6: #stark links
            tank_drive.on(SpeedPercent(b1), SpeedPercent(a))
            MANÖVER = tank_drive.on(SpeedPercent(b1), SpeedPercent(a))
            """j += 1
            i = 0"""

        elif (RECHTER_WERT - LINKER_WERT) <= 8 and (RECHTER_WERT - MITTE_WERT) > 8: #geradeaus
            tank_drive.on(SpeedPercent(c), SpeedPercent(c))

        elif (RECHTER_WERT - LINKER_WERT) <= 8 and (RECHTER_WERT - MITTE_WERT) <= 8: #alle auf schwarz
            MANÖVER #er soll wenn alle auf schwarz sind seine vorherige kurve weiter machen... 

        else:
            continue
                
            

            

    #time.sleep(5)
    #tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
    #tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 3)

if __name__== "__main__":
    main()

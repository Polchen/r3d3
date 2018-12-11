#!/usr/bin/env python3
import time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import TouchSensor, LightSensor, ColorSensor

ls=LightSensor(INPUT_1) #
ls2=LightSensor(INPUT_2)
ls3=ColorSensor(INPUT_3)
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
#time.time = 1 hat auch irgendwie funkrioniert 

def main():
    a = -25 #inneres kurvenrad für starke kurve
    b1 = 5
    b = 25 #äußeres Kurvenrad
    c = 30
    d = 3 #inneres kurvenrad für leichte kurve
    #ca 40-50 i pro sekunde
    #i ist dafür da die Zeit zu messen, da bei jedem Durchlauf der Schleife,
    #also bei jedem Messvorgang, ein i hinzugefügt wird. Somit erkennbar, ca.
    #40-50 i die sekunde, dient als stabile Zeitmessung.
    #@ Xaver, ich hab jetzt nochmal geändert dass er wenn er die eine Kurve
    #fährt und sagen wir mit i bis 20 kommt aber dann wieder geradeaus oder
    #Kurve in die anderer Richtung fährt, sich i wieder resetet. Glaube ich
    #ist dann genauer. Bei jedem j oder geradeaus durchlauf i=0, bei i oder
    #geradeaus j=0.
    
    while True: #Zeilenumbrüche fehlen noch
        """if i >= 140:
            i = 0
        if j >= 140:
            j = 0"""
        if (ls2.reflected_light_intensity - ls.reflected_light_intensity) > 8 and (ls2.reflected_light_intensity - ls3.reflected_light_intensity) > 8: #leicht rechts
            tank_drive.on(SpeedPercent(d), SpeedPercent(b))
            """i = i+1
            j = 0"""

        elif (ls2.reflected_light_intensity - ls.reflected_light_intensity) > 8 and (ls2.reflected_light_intensity - ls3.reflected_light_intensity) <= 6: #stark rechts
            tank_drive.on(SpeedPercent(a), SpeedPercent(b1))
            """i = i+1
            j = 0"""
        
        elif (ls.reflected_light_intensity - ls2.reflected_light_intensity) > 8 and (ls.reflected_light_intensity - ls3.reflected_light_intensity) > 8: #leicht links
            tank_drive.on(SpeedPercent(b), SpeedPercent(d))
            """j += 1
            i = 0"""

        elif (ls.reflected_light_intensity - ls2.reflected_light_intensity) > 8 and (ls.reflected_light_intensity - ls3.reflected_light_intensity) <= 6: #stark links
            tank_drive.on(SpeedPercent(b1), SpeedPercent(a))
            """j += 1
            i = 0"""

        elif (ls.reflected_light_intensity - ls2.reflected_light_intensity) <= 8 and (ls.reflected_light_intensity - ls3.reflected_light_intensity) > 8: #geradeaus
            tank_drive.on(SpeedPercent(c), SpeedPercent(c))

        elif (ls.reflected_light_intensity - ls2.reflected_light_intensity) <= 8 and (ls.reflected_light_intensity - ls3.reflected_light_intensity) <= 8: #stop
            tank_drive.on(SpeedPercent(20), SpeedPercent(20)) #er soll wenn alle auf schwarz sind seine vorherige kurve weiter machen... wie?

        else:
            continue
                
            

            

    #time.sleep(5)
    #tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
    #tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 3)

if __name__== "__main__":
    main()

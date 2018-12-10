#!/usr/bin/env python3
import time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.sensor.lego import TouchSensor, LightSensor

ls=LightSensor(INPUT_1) #
ls2=LightSensor(INPUT_2)
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
#time.time = 1 hat auch irgendwie funkrioniert 

def main():
    a = -30 # Werte mit kleinen rädern! Mit großen deutlich weniger!
    b = 45 
    c = 50
    d = 5
    #ca 40-50 i pro sekunde
    #i ist dafür da die Zeit zu messen, da bei jedem Durchlauf der Schleife,
    #also bei jedem Messvorgang, ein i hinzugefügt wird. Somit erkennbar, ca.
    #40-50 i die sekunde, dient als stabile Zeitmessung.
    #@ Xaver, ich hab jetzt nochmal geändert dass er wenn er die eine Kurve
    #fährt und sagen wir mit i bis 20 kommt aber dann wieder geradeaus oder
    #Kurve in die anderer Richtung fährt, sich i wieder resetet. Glaube ich
    #ist dann genauer. Bei jedem j oder geradeaus durchlauf i=0, bei i oder
    #geradeaus j=0.
    
    while True:
        i = 0
        j = 0
        while True: #Zeilenumbrüche fehlen noch
            if i >= 140:
                i = 0
            if j >= 140:
                j = 0
            if (ls2.reflected_light_intensity - ls.reflected_light_intensity) > 8 and i < 40: #unter ca. 1 sec inneres rad nur langsamer
                tank_drive.on(SpeedPercent(d), SpeedPercent(b))
                i = i+1
                j = 0

            elif (ls2.reflected_light_intensity - ls.reflected_light_intensity) > 8 and i >= 40: #ab ca. 1 sec ein rad negativ
                tank_drive.on(SpeedPercent(a), SpeedPercent(b))
                i = i+1
                j = 0
            
            elif (ls.reflected_light_intensity - ls2.reflected_light_intensity) > 8 and j < 40:
                tank_drive.on(SpeedPercent(b), SpeedPercent(d))
                j += 1
                i = 0

            elif (ls.reflected_light_intensity - ls2.reflected_light_intensity) > 8 and j >= 40:
                tank_drive.on(SpeedPercent(b), SpeedPercent(a))
                j += 1
                i = 0
            
            else: #(ls2.reflected_light_intensity - ls.reflected_light_intensity) < 5:
                tank_drive.on(SpeedPercent(c), SpeedPercent(c))
                i = 0
                j = 0
            

    #time.sleep(5)
    #tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
    #tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 3)

if __name__== "__main__":
    main()

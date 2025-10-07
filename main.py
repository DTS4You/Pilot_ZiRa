######################################################
### Projekt: Pilot ZiRa                            ###
### Version: Slave                                 ###
### Datum  : 05.10.2025                            ###
######################################################
#from machine import Pin, Timer                              # type: ignore
from libs.module_init import Global_Module as MyModule
from time import sleep                     # type: ignore


TASTER_VORNE    = 0b00000010
TASTER_HINTEN   = 0b00001000
KONTAKT_RED     = 0b00010000
KONTAKT_GREEN   = 0b00100000

def set_led_to_color(color):
    for i in range(5):
        MyWS2812.set_led_obj(i, color)

# ------------------------------------------------------------------------------
# --- Main Function                                                          ---
# ------------------------------------------------------------------------------

def main():

    print("=== Start Main ===")
    
    try:
        print("Start Main Loop")
 
        set_led_to_color("def")

        gpio = MyGPIO.GPIO()
        
        while (True):

            value_io = gpio.get_input()
            #print(bin(value_io))
            #gpio.set_output(value_io)
            if value_io & TASTER_VORNE:
                pass
            
            if value_io & TASTER_HINTEN:
                if value_io & KONTAKT_GREEN:
                    set_led_to_color("green")
                elif value_io & KONTAKT_RED:
                    set_led_to_color("red")
                else:
                    set_led_to_color("def")
            
            sleep(0.2)

    except KeyboardInterrupt:
        print("Keyboard Interrupt")
    finally:
        print("Exiting the program")   

    print("=== End of Main ===")

# ==============================================================================
# ==============================================================================
    
# ###############################################################################
# ### Main                                                                    ###
# ###############################################################################

if __name__ == "__main__":
    
    if MyModule.inc_gpio:
        print("I2C_GPIO -> Load-Module")
        import libs.module_gpio as MyGPIO
    else:
        print("I2C_GPIO -> nicht vorhanden")

    if MyModule.inc_ws2812:
        print("WS2812 -> Load-Module")
        import libs.module_ws2812_v2 as MyWS2812         # Modul WS2812  -> WS2812-Ansteuerung
        #print("WS2812 -> Setup")
        MyWS2812.setup_ws2812()
        ### Test ###
        print("WS2812 -> Run self test")
        MyWS2812.self_test()
    else:
        print("WS2812 -> nicht vorhanden")

    if MyModule.inc_decoder:
        print("Decode -> Load-Module")
        import libs.module_decode as MyDecode
        #print("Decode -> Setup")
        MyDecode.decode_setup()
        ### Test ###
        #print("Decode -> Test")
        #MyDecode.decode_input("Test")
    else:
        print("Decode -> nicht vorhanden")

    if MyModule.inc_serial:
        print("Serial-COM -> Load-Module")
        import libs.module_serial as MySerial
        #print("Serial-Con -> Setup")
        MySerial.sercon_setup()
        ### Test ###
        #print("Serial-Con -> Test")
        #MySerial.sercon_write_out("Start Test")
    else:
        print("Serial-COM -> nicht vorhanden")

    main()      # Start Main $$$

# Normal sollte das Programm hier nie ankommen !
print("___ End of Programm ___")
print("§§§> !!! STOP !!! <§§§")

# ##############################################################################

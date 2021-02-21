#!/usr/bin/env python3

import ev3dev.ev3 as ev3
import sys
from time import sleep




class Robot:
    """
    -- TEMPLATE --
    This class provides logic for moving the sensor and scrolling the bar code cards
    """
    btn = ev3.Button()
    abc = [None]*10
    light_motor = ev3.LargeMotor('outD') 
    scrool_motor = ev3.LargeMotor('outA')

  



    def debug_print(*args, **kwargs):
        print(*args, **kwargs, file=sys.stderr)


        
    def sensor_step(self):
        """
        Moves the sensor one step to read the next bar code value
        """
        # implementation
        #32.101
        
        self.light_motor.run_to_rel_pos(position_sp=-33, speed_sp=60, stop_action='hold')
        self.light_motor.wait_while('running')


    
    def sensor_reset(self):
        """
        Resets the sensor position
        """
           
        self.light_motor.run_to_rel_pos(position_sp=355, speed_sp=100, stop_action='hold')
        self.light_motor.wait_while('running')
        sleep(0.4)
        
        

    def scroll_step(self):
        """
        Moves the bar code card to the next line.
        # """
        self.scrool_motor.run_to_rel_pos(position_sp=62, speed_sp=100, stop_action='hold')
        self.scrool_motor.wait_while('running')
        sleep(0.4)
    
    def read_value(self) -> int:
        """
        Reads a single value, converts it and returns the binary expression
        :return: int
        """
        # implementation
        ls = ev3.LightSensor('in3')
        ls.mode = 'REFLECT'
        
        
        light_value=ls.value()
        if(light_value>540):
            light_value=0
        else:
            light_value=1
        
        
        
        return light_value

    def special(self):
        self.light_motor.run_to_rel_pos(position_sp=-3, speed_sp=80, stop_action='hold')
        self.light_motor.wait_while('running')
        sleep(0.1)

    def start_pos(self):
        self.light_motor.reset()

    def turn_to_first(self):
        self.light_motor.run_to_abs_pos(position_sp=0, speed_sp=80, stop_action='hold')


    
    def reading(self) -> int:
        """
        Reads a single value, converts it and returns the binary expression
        :return: int
        """
        # implementation
        ls = ev3.LightSensor('in3')
        ls.mode = 'REFLECT'
        
        
        light_value=ls.value()
       
        if(light_value>520):
            light_value=0
        else:
            light_value=1
        
        
        
        return light_value




        
            


        


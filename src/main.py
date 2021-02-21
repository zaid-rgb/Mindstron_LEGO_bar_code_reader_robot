#!/usr/bin/env python3
from time import sleep
from hamming_code import *
from stack_machine import StackMachine
from robot import Robot




def run():
    # the execution of all code shall be started from within this function

    robo_object = Robot()
    ham_object = HammingCode()
    stk_object = StackMachine()

    


    while(1):
        robo_object.start_pos()
        decoded_word = [None]*5
        decoded_word = tuple(decoded_word)
        
        steps = 8
        while (1):
            
            for i in range(30):
                if robo_object.reading()==1:
                    break
                
                robo_object.special()

               
                 
            if robo_object.read_value()==0:
                robo_object.turn_to_first()
                break      

            

            abc = [None] * 10 
            for i in range(10):
                robo_object.sensor_step()

                abc[i]=robo_object.read_value()
                 
                
                sleep(0.4)
            
        
        
            robo_object.debug_print('Scanned',abc)
            
            
            robo_object.sensor_reset()
            
            abc = tuple(abc)
            decoded_word, result = ham_object.decode(abc)
            steps = steps - 1
            if decoded_word!=None:
                if decoded_word[0] ==1:
                    robo_object.debug_print('This is an operand',decoded_word)
                elif decoded_word[0] ==0:
                    robo_object.debug_print('This is an Instruction',decoded_word)
                    

                
                    
                robo_object.debug_print(stk_object.do(decoded_word))
                robo_object.debug_print('Overflow bit', stk_object.overflow)
                
                
                
                
                sleep(0.3)


            if decoded_word==(0,0,0,0,0):
                break

            robo_object.scroll_step() 

        if decoded_word==(0,0,0,0,0):
            robo_object.debug_print('program ended')
            break    
        robo_object.debug_print('Top element of the stack',stk_object.top())
        for k in range(len(stk_object.stack)):
            robo_object.debug_print(stk_object.stack[k])

        robo_object.debug_print("The page is finished")
        for i in range(steps+1):
            robo_object.scroll_step()
        sleep(30)

      
 


        


    



if __name__ == '__main__':
    run()

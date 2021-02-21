#!/usr/bin/env python3

from enum import IntEnum
from typing import Callable, Tuple
from ctypes import c_ubyte



# IMPORTANT NOTE: DO NOT IMPORT THE ev3dev.ev3 MODULE IN THIS FILE

class SMState(IntEnum):
    """
    Return codes for the stack machine
    """
    RUNNING = 1
    STOPPED = 2
    ERROR = 3


class StackMachine:
    """
    -- TEMPLATE --
    Implements the stack machine according to the specification
    """
    stack = []
    def __init__(self):
        """ Initialises the stack machine by setting its overflow flag and its callback function for the CHK instruction.

        """
        self.stack.clear()
        self.overflow = False



    def do(self, code_word: Tuple[int, int, int, int, int]) -> SMState:
        """
        Processes the entered code word by either executing the instruction or pushing the operand on the stack.
        :param code_word: 5-tuple
        :returns: SMState
        """

        STP = (0,0,0,0)
        DUP = (0,0,0,1)
        DEL = (0,0,1,0)
        SWP = (0,0,1,1)
        ADD = (0,1,0,0)
        SUB = (0,1,0,1)
        MUL = (0,1,1,0)
        DIV = (0,1,1,1)
        EXP = (1,0,0,0)
        MOD = (1,0,0,1)
        SHL = (1,0,1,0)
        SHR = (1,0,1,1)
        LTH = (1,1,0,0)
        IEQ = (1,1,0,1)
        NOT = (1,1,1,0)
        AND = (1,1,1,1)


        stack_temp = int(''.join(map(str, code_word[1:5])), 2) << 0
   
        
        stack_temp = c_ubyte(stack_temp)
        

        first_bit = code_word[0]



        if first_bit == 1:

            if len(code_word)!=5:
                return SMState.ERROR
            else:
                self.stack.append(stack_temp)
                return SMState.RUNNING


        elif first_bit == 0:


            if code_word[1:] == STP:
                return SMState.STOPPED


            elif code_word[1:] == DUP:
                if self.top()!= None:
                    stack_temp = self.stack.pop().value
                    self.stack.append(c_ubyte(stack_temp))
                    self.stack.append(c_ubyte(stack_temp))
                    return SMState.RUNNING
                else:
                    return SMState.ERROR

            elif code_word[1:] == DEL:
                if self.top()!= None:
                    stack_temp = self.stack.pop()
                    return SMState.RUNNING
                else:
                    return SMState.ERROR


            elif code_word[1:] == SWP:
                if len(self.stack)<2:
                    return SMState.ERROR
                else:
                    a1 = self.stack.pop().value
                    b1 = self.stack.pop().value

                    self.stack.append(c_ubyte(a1))
                    self.stack.append(c_ubyte(b1))

                    return SMState.RUNNING

            elif code_word[1:] == ADD:
                #Overflow
                if len(self.stack)<2:
                    return SMState.ERROR
                else:
                    a1 = self.stack.pop()
                    b1 = self.stack.pop()
                    
                   
                    stack_temp = b1.value + a1.value
                
                    if stack_temp >255:

                        self.overflow = True
                        print("Overflow")

                    self.stack.append(c_ubyte(stack_temp))
                    return SMState.RUNNING


            elif code_word[1:] == SUB:
                if len(self.stack)<2:
                    return SMState.ERROR
                else:
                    a1 = self.stack.pop()
                    b1 = self.stack.pop()
                    stack_temp = b1.value - a1.value
                    if stack_temp < 0:
                        self.overflow = True
                        print("Overflow")

                    self.stack.append(c_ubyte(stack_temp))
                    return SMState.RUNNING

            elif code_word[1:] == MUL:
                #overflow
                if len(self.stack)<2:
                    return SMState.ERROR
                else:
                    
                    a1 = self.stack.pop()
                    b1 = self.stack.pop()
                    
                  
                
                   
                    stack_temp = (b1.value * a1.value)
                  

                    if stack_temp > 255:
                        self.overflow = True
                        print("Overflow")

                    self.stack.append(c_ubyte(stack_temp))
                    return SMState.RUNNING

            elif code_word[1:] == DIV:
                if len(self.stack)<2:
                    return SMState.ERROR
                else:
                    
                    a1 = self.stack.pop()
                    
                    b1 = self.stack.pop()
                    
                    if a1!=0:
                        print (type(stack_temp))
                        stack_temp = b1.value // a1.value

                        self.stack.append(c_ubyte(stack_temp))
                        return SMState.RUNNING
                    else:
                        return SMState.ERROR
            #error also here
            elif code_word[1:] == EXP:
                #overflow
                if len(self.stack)<2:
                    return SMState.ERROR
                else:
                    a1 = self.stack.pop()
                    b1 = self.stack.pop()
                    

                    stack_temp = (b1.value ** a1.value)
                    if stack_temp > 255:
                        self.overflow = True
                        print("Overflow")

                    self.stack.append(c_ubyte(stack_temp))
                    return SMState.RUNNING

            elif code_word[1:] == MOD:
                if len(self.stack)<2:
                    return SMState.ERROR
                else:
                    a1 = self.stack.pop()
                    b1 = self.stack.pop()
                    stack_temp = b1.value % a1.value

                    self.stack.append(c_ubyte(stack_temp))

                    return SMState.RUNNING

            elif code_word[1:] == SHL:

                if len(self.stack)<2:
                    return SMState.ERROR
                else:
                    a1 = self.stack.pop()
                    b1 = self.stack.pop()
                    stack_temp = b1.value << a1.value
                    if stack_temp > 255:
                        self.overflow = True
                        print("Overflow")

                    self.stack.append(c_ubyte(stack_temp))
                    return SMState.RUNNING
            elif code_word[1:] == SHR:

                if len(self.stack)<2:
                    return SMState.ERROR
                else:
                    a1 = self.stack.pop()
                    b1 = self.stack.pop()
                    stack_temp = b1.value >> a1.value

                    self.stack.append(c_ubyte(stack_temp))
                    return SMState.RUNNING

            elif code_word[1:] == LTH:

                if len(self.stack)<2:
                    return SMState.ERROR
                else:
                    a1 = self.stack.pop().value
                    b1 = self.stack.pop().value
                    if(b1 < a1):
                        stack_temp = c_ubyte(1)
                    else:
                        stack_temp = c_ubyte(0)

                    self.stack.append(stack_temp)

                    return SMState.RUNNING

            elif code_word[1:] == IEQ:
                if len(self.stack)<2:
                    return SMState.ERROR
                
                else:
                    a1 = self.stack.pop().value
                    b1 = self.stack.pop().value
                    if (b1 == a1):
                        stack_temp = c_ubyte(1)
                    else:
                        stack_temp = c_ubyte(0)


                    self.stack.append(stack_temp)
                    return SMState.RUNNING

            elif code_word[1:] == NOT:
                
                if len(self.stack)<1:
                    return SMState.ERROR
                else:
                    a1 = self.stack.pop()

                    stack_temp = ~a1.value

                    self.stack.append(c_ubyte(stack_temp))

                    return SMState.RUNNING

            elif code_word[1:] == AND:
                if len(self.stack)<2:
                    return SMState.ERROR
                else:
                    a1 = self.stack.pop()
                    b1 = self.stack.pop()
                    stack_temp = b1.value & a1.value

                    self.stack.append(c_ubyte(stack_temp))

                    return SMState.RUNNING
        else:
            return SMState.ERROR




    def top(self) -> Tuple[int, int, int, int, int, int, int, int]:
        """
        Returns the top element of the stack.
        :returns: 8-tuple or None
        """
        # implementation
        final = [None] * 8
        if len(self.stack)!= 0:
            final.clear()
            final.extend("{0:08b}".format((self.stack[-1]).value))
            for i in range(len(final)):
                final[i] = int(final[i])
            return (tuple(final))

        else:
            return (None)



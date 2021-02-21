#!/usr/bin/env python3

from enum import IntEnum
from typing import Tuple



# IMPORTANT NOTE: DO NOT IMPORT THE ev3dev.ev3 MODULE IN THIS FILE

class HCResult(IntEnum):
    """
    Return codes for the Hamming Code interface
    """
    VALID = 1
    CORRECTED = 2  # whenever ANY bit has been corrected
    UNCORRECTABLE = 3


class HammingCode:
    """
    -- TEMPLATE --
    Provides decoding capabilities for the specified Hamming Code
    """

    def decode(self, encoded_word: Tuple[int, int, int, int, int, int, int, int, int, int]) -> Tuple[
        Tuple[int, int, int, int, int], HCResult]:
        """
        Checks the channel alphabet word for errors and attempts to decode it.
        :param encoded_word: 10-tuple
        :returns: (5-tuple, HCResult) or (None, HCResult)
        """
        #over all parity

        op=int(0)
        if (sum(encoded_word)%2==0):
            op = 0
        else:
            op = 1
        


        #Removing last bit
        without_last_bit=encoded_word[0:9]

        #parity-check matrix H

        parity_matrix =((1,0,0,0,0,1,0,0,0),(0,1,0,1,1,0,1,0,0),(0,1,1,1,0,0,0,1,0),(1,0,1,1,1,0,0,0,1))

        #Task 2 Number 4


        HT = [
        [1, 0, 0, 1], [0, 1, 1, 0], [0, 0, 1, 1], [0, 1, 1, 1], [0, 1, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0],
        [0, 0, 0, 1]]

        S = [0] * 4
              # Creating the syndrome vector S

        for i in range(len(S)):
            for j in range(0, 9):
                S[i] += without_last_bit[j] * HT[j][i]


            S[i] = S[i] % 2

        #Syndrome vector calculated by multiplying HT and without_last_bit


        #Task 2 Number 5

        decoded_word = list(encoded_word[0:5])

        if (op == 0 or op == 1) and (S == [0, 0, 0, 0]):


            return (tuple(decoded_word), HCResult.VALID)

        elif (op == 1) and (S != [0, 0, 0, 0]):

            for i in range(5):
                if HT[i] == S:
                    if decoded_word[i] == 1:
                        decoded_word[i] = 0
                    else:
                        decoded_word[i] = 1
                    break
            return(tuple(decoded_word), HCResult.CORRECTED)

        
        else:
            return (None, HCResult.UNCORRECTABLE)


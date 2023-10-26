#!/usr/bin/python3
"""
UTF-8 Validation - determines if
a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data) -> bool:
    """
    Returns True if data is a valid UTF-8 encoding, else return False
    :param data:e
    :return:
    """
    #initialize num_bytes to 0
    #to keep track of no of bytes remaining to be processed
    num_bytes = 0
    #iterate through each byte using for loop
    for byte in data:
        #set mask variable to 1 shifted by 7 bits
        #thus setting leftmost bt to 1 and the rest 0
        #this checks if the bite is the start of a UTF-8 sequence
        mask = 1 << 7
        #if num_bytes is 0 it means it's the start of a new character
        if not num_bytes:
            #check if byte has leftmost it set
            #if set, it' part of a multibyte sequence
            while byte & mask:
                #code counts how many consequtive bits are set
                #to determine the no of bytes in the sequence
                num_bytes += 1
                mask >>= 1
            #if num_bytes is still 0 the byte is either
            #a single byte char (ASCII) or invalid data
            #therefore loop continues to next byte
            if not num_bytes:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        #if num bytes is not 0 then current byte is part
        #of multi-byte sequence.
        #it check if bytes two most significant bts are 10
        #as per UTF-8 encoding rules
        #else, it's invalid thereby returning false
        else:
            if byte >> 6 != 0b10:
                return False
        #decrement num_bytes counter showing one byte in the
        #multibyte sequence has been processed
        num_bytes -= 1
    #if num_bytes is 0 after loop, then data list
    #has been processed, thereby function returns true
    #indicating input is valid UTF-8
    return num_bytes == 0

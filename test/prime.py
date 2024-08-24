#Written by Zach Fletcher

#sieve of Eratosthenes

import math
import numpy as np


def primeGen(beginning, end):


    end = end+1 #includes ending val in function

    
    if beginning < 0 or end < 0:
        return "please enter positive integers"
    if beginning < 0 and end < 0:
        return "please enter positive integers"
    #checks for positive inputs, as prime numbers are all positive

    if end < beginning:
        switchvar = beginning
        beginning = end
        end = switchvar
        switchvar = 0 #zeroes out switchvar at the end. 
        #ensures values are in correct order

    array1 = np.array([range(beginning, end, 1)]) #creates a array of all values between beginning value and ending value

    array2 = np.delete(array1 , np.where(array1 <= 1)) # filters all values equal to or smaller than 1 out, neither are prime numbers. if no such numbers exist both arrays are identical.

    output = [1 for all in range(0, len(array2))] #sets all true/false to true to start.
    
    #could filter out all even numbers to improve performance, but honestly performance is not an issue.

    print(output)
    
    checkNumber = 2 #gives starting value to check numbers against. This is somewhat redundant, but redundancies are good.
    arrayLocation = 0 #gives starting point IN ARRAY
    print(array2)
    print(output[arrayLocation]) #makes sure input is correct

    while (arrayLocation <= len(array2)): #iterates through every number in array irrespective of array length
    
        if (output[arrayLocation] == 1): #checks current location to see if it could be a prime number. if not, skip
            
            for array1 in range(array2[arrayLocation] * array2[arrayLocation], end, array2[arrayLocation]): #finds the whole range of non-primes originating from starter prime and puts them in a range.
                output = False # sets whether or not it is a prime to false

        print(checkNumber) #makes sure input is correct
        checkNumber += 1 #iterates one forward
        arrayLocation += 1
    
    

    for checkNumber in range(beginning, end):
        if output[checkNumber]:
            print(checkNumber)

   
    return "complete"





def sortNumber(*tupleInputVal):

    arrayLocation = 0 #starts search function at zero 
    processLocation = 0 #starts sorting at first digit

    inputVal = list(tupleInputVal)

    print(type(inputVal))
    print(len(inputVal)-1)
    print(inputVal)

    outputArray = [] #defining blank output array (actually a list)

    while (processLocation < len(inputVal)):
        print("current digit number is",processLocation)
        arrayLocation = processLocation #prevents endless resorting of first digit

        smallestVal = inputVal[arrayLocation] #sets initial smallest value to be the starting digit.
        print(smallestVal)
        while (arrayLocation < len(inputVal)): #goes through each remaining digit of the sequence to find smallest

            if inputVal[arrayLocation] < smallestVal: #checks if current digit is smaller than stored smallest digit 

                smallestVal = inputVal[arrayLocation]
                smallestLocation = arrayLocation

            print("array searching position is",arrayLocation,"current smallest value is",smallestVal)

            arrayLocation = arrayLocation + 1 #cycles to next number in the sequence

        
        if inputVal[processLocation] != inputVal[smallestLocation]:  #make sure to not overwrite any data we don't want to  
            
        
            placeHolder = inputVal[processLocation]

            inputVal[processLocation] = smallestVal

            inputVal[smallestLocation] = placeHolder

            placeHolder = 0 # zero out placeholder

        outputArray.append(smallestVal)

        print("testing value",inputVal[smallestLocation])
        print(inputVal)
        





        processLocation = processLocation + 1

        
        print("current sorted array is",outputArray)

            
    
    
    

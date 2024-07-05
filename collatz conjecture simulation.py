import numpy
import matplotlib.pyplot as plt
import json

a = int(input("Enter the number till which you want the collatz conjecture:"))
n = a
storage = []

if(n > 0):
    while True:
        storage_obj = {a : storage}
        if(n%2 != 0):
            n = 3*n+1
            print(n,"\n")
            storage.append(n)
        elif(n%2 == 0):
            n = int(n/2)
            print(n,"\n")
            storage.append(n)
        if(n == 1):
            print("After this point, the code falls into a loop of 4-2-1. Hence the program is ended.")
            ypoints = numpy.array(storage)
            plt.plot(ypoints)
            plt.show()
            actual_storage_obj = (storage_obj)
            with open('data.json', 'w') as file:
                json.dump(actual_storage_obj, file)
            break
        False
else:
    print("Input needs to be greater than 0.")            

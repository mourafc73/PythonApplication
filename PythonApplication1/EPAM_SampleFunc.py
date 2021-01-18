
#Write a function:
#def solution(A)
#that, given an array A of N integers, returns the smallest positive integer (greater than 0) 
#that does not occur in A.
#For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#Given A = [1, 2, 3], the function should return 4.
#Given A = [−1, −3], the function should return 1.
#Write an efficient algorithm for the following assumptions:

#N is an integer within the range [1..100,000];
#each element of array A is an integer within the range [−1,000,000..1,000,000].
#Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(Ap):
    # write your code in Python 3.6
    B = set(Ap)
    for values in range (1,1000000):
        if not values in B:
            x=values
            print(x)
            break
            
        else: 
            print( str(values) + " - in B" )
    
    return x       


class Car(object):
    def __init__(self,make,model,color):
        self.make=make;
        self.model=model;
        self.color=color;
        self.owner_number=0 
    def car_info(self):
        print("make: ",self.make)
        print("model:", self.model)
        print("color:",self.color)
        print("number of owners:",self.owner_number)
    def sell(self):
        self.owner_number=self.owner_number+1


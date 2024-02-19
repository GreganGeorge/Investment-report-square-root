import math
x=float(input("Enter a positive number : "));
tolerance=0.000001;
estimate=0.1
while True:
    estimate=(estimate+x/estimate)/2
    difference=abs(x-estimate**2)
    if difference<=tolerance:
        break
print("The program's estimate:",estimate);
print("Python's estimate:",math.sqrt(x))


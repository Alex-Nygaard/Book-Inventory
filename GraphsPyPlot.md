# Practice with Python and Pyplot

## Question 1

```.py
import matplotlib.pyplot as pyplot
from random import randint
def question1():
    x = [i for i in range(1,1000)]

    y = [randint(1, 100) for i in x]
    
    # Plot the values, using dot points
    pyplot.plot(x, y, ".")

    pyplot.xlabel("x")
    pyplot.ylabel("$y = x^2$")
    pyplot.show()
```

## Question 2

```.py
def question2():
    ### Easier way, using built in sum() function ###
    #y_avg = sum(y) / len(y) 

    total_val = 0
    for i in y:
        total_val += i
    y_avg = total_val / len(y)

    print(y_avg)
```


## Question 3

```.py
import matplotlib.pyplot as pyplot
from math import sin
def question3():
    # Values from -10 to 10 with a 0.1 step interval
    x = [i/10 for i in range(-100,100)]

    y = [14 * sin(0.5*i) for i in x]

    pyplot.plot(x,y)
    pyplot.xlabel("x")
    pyplot.ylabel("$y = 14 * sin(0.5*x)$")

    pyplot.show()
```


## Question 4

```.py
import matplotlib.pyplot as pyplot
from math import e
def question4():
    x = [i/10 for i in range(-100,100)]

    # Sigmoid function
    y = [1/(1+e**-i) for i in x]

    pyplot.plot(x,y)
    pyplot.xlabel("x")
    pyplot.ylabel("y = 1/(1+e^-x)")

    pyplot.show()
```


## HL Question 1

```.py
from random import randint
import matplotlib.pyplot as pyplot

# BUBBLE SORTING ALGORITHM
def bubbleSort(nums):
    length = len(nums)

    while True:
        switched = False
        for i in range(length - 1):
            num1 = nums[i]
            num2 = nums[i+1]
            if (num1 > num2):
                # Switching
                nums[i] = num2
                nums[i+1] = num1
                switched = True

        # If no switch takes place, break the while loop
        if (switched == False):
            return nums


# HL QUESTION 1
def HLquestion1():
    x = [i for i in range(1,1000)]

    nums = [randint(1, 100) for i in x]
    nums = bubbleSort(nums)


    # Plot the values, using dot points
    pyplot.plot(x, nums, ".")

    pyplot.xlabel("x")
    pyplot.ylabel("Sorted values")
    pyplot.show()
```


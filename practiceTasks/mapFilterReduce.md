# Map, filter, reduce function in Python
Map, filter and reduce are three semi-builtin functions in Python.
Below I explain their function, how they work and examples of how to use them

### Map function
The map function is used to repeatedly apply a given function to a set of values or data. The syntax is `map(FUNC, LIST)`, where FUNC is the function to be applied and LIST is an iterable object with values.

A handy use case of such a function is when repeatedly doing the same mathematical operations to many values. For example, when calculating the area of several circles with different radii. 

The code for such as problem can look like:
```.py
# Area of circles
import math

def area(r):
    return math.pi * (r**2)

radii = [2, 5, 7.1, 0.3, 10]

print(
    list(map(area,radii))
)
```
The `map()` function returns a map object as well, but this can be converted to a list with the `list()` function built in with python.


### Filter function
The filter function is used to reduce the number of values in a list based on a conditional expression. The syntax is `filter(FUNC, LIST)`, where FUNC is the function that returns either TRUE or FALSE and LIST is an iterable object with values.

An example of how this can be done is as follows:
```.py
import statistics

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)

print( "Higher than avg,",
    list(filter(lambda x: x > avg, data))
)
```

Here the statistics module is imported to get the mean of the `data` list. The lambda function `lambda x: x > avg` is passed in as the FUNC argument, and returns true if x is greater than the average. If the lambda function returns True, that value x is kept in the list. If it returns False, the value is removed.

Another use of the filter function is to remove blank data. Passing in `None` as the FUNC argument in the filter function removes all the values matching with None. This includes empty strings, empty lists and tuples and zero.
```.py
# Removing missing data
countries = [
    "", "Argentina", "", "Brazil", "Chile", "", 
    "Columbia", "", "Ecuador", "", "", "Venezuela"
]

print(
    list(filter(None, countries))
)
```
This code gives a list with only the valid countries.

### Reduce function
The reduce function is a bit more complicated. It applies a function to the first two values of the list, then iterates through the rest of the list, giving the PREVIOUS output as one argument and the next value in the list as the second argument. To visualize this:
```
Data: [a1, a2, a3, ... , an]
Function: f(x,y)

reduce(f, data):
  Step 1: val1 = f(a1, a2)
  Step 2: val2 = f(val1, a3)
  Step 3: val3 = f(val2, a4)
  ...
  Step n-1: val(n-1) = f(val(n-2), an)
  Return val(n-1)
```
Alternatively:
Returns `f(f(f(a1, a2), a3), a4), ... , an)`

The syntax of the reduce function is `reduce(FUNC, LIST)`

A good example of the usage of this funtion can be seen through multiplying all the values of a list together, as done in the code below:
```.py
from functools import reduce

# Multiply all numbers in a list
data = [2,3,5,7,11,13,17,19,23,29]
multiplier = lambda x,y: x * y

print(
    reduce(multiplier, data)
)
```

The lambda function is passed as the FUNC argument and the data variable is passed as the list argument.

However as mentioned in the video, the founder of Python rather recommends using a separate for-loop instead of reduce for increased readability.


# Finding prime numbers with python

### Main objective:
Creating a program that finds all the prime numbers up to a given value **as fast as possible**.
Iterative improvements of this algorithm is shown through 3 functions that are improved versions of the previous. 

### Sub-tasks
There are three main ways of solving this problem, all methods having different levels of efficiency. These three methods are outlined below and includes code snippets with explanations.


## Method 1: Bruteforcing the prime
Bruteforcing the prime numbers includes checking **all** possible factors of a number, and seeing if any give a remainder of 0 when dividing the number being checked. If the condition inside the for-loop below is true, it is evident that the number being checked, `x`, is NOT a prime. See code below for how to do this:

```.py
for i in range(2, x):
  if x % i == 0:
    return False
```

If no factors are found, the function returns `True`, meaning `x` is a prime number.


## Method 2: Testing only integers up to square root of `x`
This method significantly reduces the amount of numbers required to test if the number `x` is a prime. This is done by Only testing the integers up until the square root of `x`.

The reason this is possible, can be illuminated when looking at the example of 36. The factors of 36 are as follows:
* 1 x 36
* 2 x 23
* 3 x 12
* 4 x 9
* **6 x 6**
* *9 x 4*
* *12 x 3*
* *23 x 2*
* *36 x 1*

The key values here are **6 x 6**. This is the square root of 36, and after this the factors highlighted in *cursive* are merely a repeat of the factors before **6 x 6**. Thus, we can conclude that every factor after the square root of the number does not have to be checked. If the square root is not an integer, one must round the value down to the closest integer.

The loop for this solution would look like this:
```.py
max_divisor = math.floor(math.sqrt(x))

for i in range(2, 1 + max_divisor):
  if x % i == 0:
    return False
```

Where `max_divisor` represents the square root of `x`. (In the range() function, the square root is also checked, thus the +1)

In this solution the `math` library was also imported to use the functions
* `floor` for rounding down the square root to the closest integer
and
* `sqrt` for getting the square root of a number

## Method 3: Improving method 2 by removing even numbers
The last method is essentially identical to method 2, however with the difference being that all even numbers are removed when checking for factors.

This change is implemented in two ways. 
Firstly, the program checks if the number `x` = 2 or if `x` is greater than 2 and x is even. If either of these are true, the function returns a False, meaning `x` is not a prime number.
The second change is the step in the `range()` function in the for loop. Instead of checking every number in the `range(2, 1 + max_divisor)` as in method 2, the for loop rather uses `range(3, 1 + max_divisor, 2)`, starting from 3, going to the square root and only including EVERY OTHER integer. This results in excluding every even number for the checking.

The most important changes being made here can be seen in code as follows:

```.py
# First eliminate the possibility of x being 2 and x being even.
if x == 2:
    return True
if x > 2 and x % 2 == 0:
    return False
    
# Second, using a step of 2 in the for-loop
for i in range(3, 1 + max_divisor, 2):
    if x % i == 0:
        return False
```

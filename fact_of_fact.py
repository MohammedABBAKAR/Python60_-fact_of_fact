
# todo Factorial of Factorials

# ? Create a function that takes an integer n and returns the factorial of factorials.
# ? See below examples for a better understanding:
# * Examples

# * fact_of_fact(4) ➞ 288
# * # 4! * 3! * 2! * 1! = 288

# * fact_of_fact(5) ➞ 34560

# * fact_of_fact(6) ➞ 24883200

# Notes

# N/A
import math


def fact_of_fact(n):
    if n ==1:
        return 1
    else:
      return math.factorial(n) * fact_of_fact( n-1)
print(fact_of_fact(5))







import math

def fact_of_fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= math.factorial(i)
    return result

# Test cases
fact_of_fact_4 = fact_of_fact(4)
fact_of_fact_5 = fact_of_fact(5)
fact_of_fact_6 = fact_of_fact(6)

fact_of_fact_4, fact_of_fact_5, fact_of_fact_6

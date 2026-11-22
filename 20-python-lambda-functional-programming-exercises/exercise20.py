# ========question========
# Exercise 20: Monadic Chaining
#
# Problem Statement: Implement a Maybe class that wraps a value (or None) and provides a .bind(func) method. bind applies func to the wrapped value if it is not None, wrapping the result in a new Maybe; if the value is None, it returns Maybe(None) immediately without calling func. Chain several lambda transformations and show that a None at any step short-circuits the rest of the chain.
#
# Purpose: The Maybe monad is the functional programming solution to the problem of None-propagation. Instead of sprinkling if x is not None: guards throughout your code, you chain transformations and let the monad handle the short-circuit logic invisibly. This pattern appears in Haskell as Maybe, in Scala as Option, and in Python libraries such as returns and pymonad.
#
# Given Input: Two chains starting from Maybe(10) and Maybe(None), each passing through the same three lambda transformations.
#
# Expected Output:
#
# Maybe(10).bind(double).bind(add_three).bind(safe_sqrt) = Maybe(4.69...)
# Maybe(None).bind(double).bind(add_three).bind(safe_sqrt) = Maybe(None)
#
# Source: https://pynative.com/python-lambda-functional-programming-exercises/


# ========hints========
# Check parameters, return values, and scope before writing the function body.


# Write your code below.


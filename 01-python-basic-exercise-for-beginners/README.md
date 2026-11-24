# Python beginner exercises

40 practice questions, in the order of [PYnative](https://pynative.com/python-basic-exercise-for-beginners/). Prompts are reworded; examples follow the source. No solutions included.

Open this file in VS Code and press **Ctrl+Shift+V** for Markdown Preview. Click **Reveal hint** only when needed. Hints are visible in the raw Markdown source.

Write your answers in exercise001.py, exercise002.py, etc. Your existing exercise001.py is preserved.

## Exercise 1. Arithmetic Product and Conditional Logic

Accept two integers in a function. Return their product when it is at most 1000; otherwise return their sum.

Given Input:

- Case 1: number1 = 20, number2 = 30

- Case 2: number1 = 40, number2 = 30

Expected Output:

- The result is 600

- The result is 70

<details>
<summary>Reveal hint</summary>

Work out the product before choosing the return value.

</details>

## Exercise 2. Cumulative Sum of a Range

For each integer from 0 through 9, display it, the preceding integer, and their sum. Start the previous value at 0.

Given Input: Range: numbers = range(10)

Expected Output:

```text
Printing current and previous number sum in a range(10)
Current Number 0 Previous Number 0 Sum: 0
Current Number 1 Previous Number 0 Sum: 1
Current Number 2 Previous Number 1 Sum: 3
....
Current Number 8 Previous Number 7 Sum: 15
Current Number 9 Previous Number 8 Sum: 17
```

<details>
<summary>Reveal hint</summary>

Keep the previous value between iterations.

</details>

## Exercise 3. String Indexing and Even Slicing

Display the characters at positions 0, 2, 4, and so on in a string.

Given Input: String: "pynative"

Expected Output:

```text
Original String is  pynative
Printing only even index chars
p
n
t
v
```

<details>
<summary>Reveal hint</summary>

String positions begin at zero; think about a step size.

</details>

## Exercise 4. String Slicing and Substring Removal

Make a function that returns the part of a string left after removing its first n characters.

Given Input:

- remove_chars("pynative", 4)

- remove_chars("pynative", 2)

Expected Output:

- tive

- native

<details>
<summary>Reveal hint</summary>

Consider where the retained substring begins.

</details>

## Exercise 5. Variable Swapping (The In-Place Method)

Exchange the values of a and b without introducing a temporary variable.

Given Input: a = 5, b = 10

Expected Output:

```text
Before Swap: a = 5, b = 10
After Swap: a = 10, b = 5
```

<details>
<summary>Reveal hint</summary>

Python supports simultaneous assignment.

</details>

## Exercise 6. Calculating Factorial with a Loop

Calculate the factorial of a supplied number with a for loop.

Given Input: number = 5

Expected Output: The factorial of 5 is 120

<details>
<summary>Reveal hint</summary>

Choose an initial running product that does not change a multiplication.

</details>

## Exercise 7. List Manipulation: Add and Remove

Start with five fruits, add fig at the end, then delete the item at position 1.

Given Input: fruits = ["apple", "banana", "cherry", "date", "elderberry"]

Expected Output: ['apple', 'cherry', 'date', 'elderberry', 'fig']

<details>
<summary>Reveal hint</summary>

Look at list methods for adding an item and removing by position.

</details>

## Exercise 8. String Reversal

Produce a reversed version of a supplied string.

Given Input: text = "Python"

Expected Output: Reversed: nohtyP

<details>
<summary>Reveal hint</summary>

Think about traversing a sequence backwards.

</details>

## Exercise 9. Vowel Frequency Counter

Count vowel occurrences in a sentence, treating uppercase and lowercase alike.

Given Input: sentence = "Learning Python is fun!"

Expected Output: Number of vowels: 6

<details>
<summary>Reveal hint</summary>

Normalise letter case before testing vowel membership.

</details>

## Exercise 10. Finding Extremes (Min/Max) in a List

Report the smallest and largest integers in a list.

Given Input: nums = [45, 2, 89, 12, 7]

Expected Output: Largest: 89 Smallest: 2

<details>
<summary>Reveal hint</summary>

Python has built-ins for finding extreme values.

</details>

## Exercise 11. Removing Duplicates from a List

Build a list containing each distinct value from an input list once.

Given Input: data = [1, 2, 2, 3, 4, 4, 4, 5]

Expected Output: Unique List: [1, 2, 3, 4, 5]

<details>
<summary>Reveal hint</summary>

Think about a collection that forbids duplicates; decide whether order matters.

</details>

## Exercise 12. List Comparison and Boolean Logic

Return a Boolean indicating whether a list's first and final values match.

Given Input:

- numbers_x = [10, 20, 30, 40, 10]

- numbers_y = [75, 65, 35, 75, 30]

Expected Output:

```text
Given list: [75, 65, 35, 75, 30] | result is False
Given list: [10, 20, 30, 40, 10] | result is True
```

<details>
<summary>Reveal hint</summary>

Compare the two boundary positions.

</details>

## Exercise 13. Filtering Lists with Conditional Logic

Display the multiples of 5 found in a supplied list.

Given Input: num_list = [10, 20, 33, 46, 55]

Expected Output:

```text
Divisible by 5:
10, 20, 55
```

<details>
<summary>Reveal hint</summary>

Divisibility means the remainder is zero.

</details>

## Exercise 14. Substring Frequency Analysis

Count occurrences of the substring Emma in a supplied sentence.

Given Input:

- str_x = "Emma is good developer. Emma is a writer"

Expected Output: Emma appeared 2 times

<details>
<summary>Reveal hint</summary>

Look for a string method that counts substrings.

</details>

## Exercise 15. Nested Loops for Pattern Generation

Print five rows: row n contains the number n repeated n times.

Given Input: Range: 1 to 5

Expected Output: (The pattern shown above)

<details>
<summary>Reveal hint</summary>

Separate the row number from the number of repetitions.

</details>

## Exercise 16. Numerical Palindrome Check

Determine whether an integer reads identically in both directions.

Given Input:

- Case 1: number = 121

- Case 2: number = 125

Expected Output:

```text
Number 125 is not palindrome number
Number 121 is palindrome number
```

<details>
<summary>Reveal hint</summary>

Compare the original digits with their reversed order.

</details>

## Exercise 17. Merging Lists with Parity Filtering

Combine the odd values of the first list with the even values of the second list.

Given Input:

- list1 = [10, 20, 25, 30, 35]

- list2 = [40, 45, 60, 75, 90]

Expected Output: [25, 35, 40, 60, 90]

<details>
<summary>Reveal hint</summary>

Filter each source list using its own parity rule.

</details>

## Exercise 18. Integer Digit Extraction and Reversal

Display an integer's digits from right to left, separated by spaces. Practise extracting digits arithmetically.

Given Input: number = 7536

Expected Output: 6 3 5 7

<details>
<summary>Reveal hint</summary>

Base 10 arithmetic can isolate and remove the last digit.

</details>

## Exercise 19. Multi-Tiered Income Tax Calculation

Calculate tax using these fictional brackets: the first 10,000 is untaxed; the next 10,000 is taxed at 10%; everything above 20,000 is taxed at 20%.

Given Input: income = 45000

Expected Output: Total income tax to pay is 6000

<details>
<summary>Reveal hint</summary>

Apply each rate only to the part of income inside its bracket.

</details>

## Exercise 20. Nested Loops for Multiplication Tables

Display a 10-by-10 multiplication grid for the integers 1 through 10.

Given Input: Range: 1 to 10

Expected Output:

```text
1  2  3  4  5  6  7  8  9  10 		
2  4  6  8  10 12 14 16 18 20 		
... (up to 10)
```

<details>
<summary>Reveal hint</summary>

One loop controls rows; another controls columns.

</details>

## Exercise 21. Downward Half-Pyramid Pattern

Draw five rows of stars, decreasing from five stars in the first row to one in the last.

Given Input: Rows: 5

Expected Output:

```text
* * * * * 
* * * * 
* * * 
* * 
*
```

<details>
<summary>Reveal hint</summary>

The number of stars falls by one on each row.

</details>

## Exercise 22. Custom Exponentiation Function

Implement exponent(base, exp) using repeated multiplication; return the calculated power.

Given Input: base = 2, exp = 5

Expected Output: 2 raises to the power of 5: 32

<details>
<summary>Reveal hint</summary>

Maintain a running product; consider an exponent of zero.

</details>

## Exercise 23. Check Palindrome Number

Test an integer for palindrome symmetry again. Try mathematical digit reversal as an alternative to exercise 16.

Given Input: number = 121

Expected Output:

```text
Original number 121
Yes. given number is palindrome number
```

<details>
<summary>Reveal hint</summary>

Preserve the original number before working through its digits.

</details>

## Exercise 24. Generate Fibonacci Series

Display 15 Fibonacci terms, beginning with 0 and 1; each later term adds the preceding two.

Given Input: Terms = 15

Expected Output: 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

<details>
<summary>Reveal hint</summary>

Keep track of two neighbouring terms.

</details>

## Exercise 25. Check Leap Year

Read a year and decide whether it is a leap year. Multiples of 4 qualify, except century years must also be multiples of 400.

Given Input: year = 2024

Expected Output: 2024 is a leap year

<details>
<summary>Reveal hint</summary>

Check century exceptions as well as the four-year rule.

</details>

## Exercise 26. Merging Two Dictionaries

Combine the entries of two dictionaries into one dictionary.

Given Input:

```text
dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "job": "Engineer"}Code language: Python (python)
```

Expected Output:

```text
{'name': 'Alice', 'age': 25, 'city': 'New York', 'job': 'Engineer'}
```

<details>
<summary>Reveal hint</summary>

Look at dictionary merging operations; consider duplicate keys.

</details>

## Exercise 27. Finding Common Elements (Intersections)

Use sets to identify values shared by two lists.

Given Input:

```text
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]Code language: Python (python)
```

Expected Output: Common Elements: {4, 5}

<details>
<summary>Reveal hint</summary>

Think about set intersection.

</details>

## Exercise 28. Odd/Even List Splitter

Separate a list's integers into one list of even values and another of odd values.

Given Input: numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]

Expected Output:

```text
Even numbers: [12, 34, 10, 8, 2]
Odd numbers: [7, 21, 5, 3, 19]
```

<details>
<summary>Reveal hint</summary>

Use the remainder after division by two.

</details>

## Exercise 29. Word Length Analysis

Choose five words, then display each word with its character length.

Given Input: words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

Expected Output:

```text
Apple - 5 Banana - 6 Cherry - 6 Date - 4 Elderberry - 10
```

<details>
<summary>Reveal hint</summary>

Look for the built-in sequence length operation.

</details>

## Exercise 30. Word Frequency Counter (The Histogram)

Build a dictionary mapping each word in a paragraph to its occurrence count.

Given Input: text = "apple banana apple cherry banana apple"

Expected Output: {'apple': 3, 'banana': 2, 'cherry': 1}

<details>
<summary>Reveal hint</summary>

Keep one counter per distinct word.

</details>

## Exercise 31. Print Alternate Prime Numbers

Find primes up to 20 and display alternate entries, starting with the first prime: 2, 5, 11, 17.

Given Input: Limit = 20

Expected Output: 2, 5, 11, 17

<details>
<summary>Reveal hint</summary>

First identify the primes, then take alternate positions.

</details>

## Exercise 32. Dictionary of Squares (Mapping Logic)

Map every integer from 1 through 10 to its square in a dictionary.

Given Input: Range: 1 to 10

Expected Output:

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
```

<details>
<summary>Reveal hint</summary>

Each dictionary entry associates a number with its square.

</details>

## Exercise 33. Character Replacer (Data Sanitization)

Read a sentence and replace each space with an underscore.

Given Input: "I love coding in Python"

Expected Output: I_love_coding_in_Python

<details>
<summary>Reveal hint</summary>

Look for a string replacement method.

</details>

## Exercise 34. Print Reverse Number Pattern

Print descending number rows: first 5 through 1, then 4 through 1, continuing down to a single 1.

Given Input: Rows = 5

Expected Output:

```text
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
```

<details>
<summary>Reveal hint</summary>

Both the starting value per row and the values within a row decrease.

</details>

## Exercise 35. Digit Detection in Strings

Examine a user-supplied string character by character with a for loop; report whether any character is a digit.

Given Input: input_string = "Python3"

Expected Output: The string 'Python3' contains digits: True

<details>
<summary>Reveal hint</summary>

A string character has a method for checking whether it is a digit.

</details>

## Exercise 36. Capitalize First Letter (Title Case)

Uppercase the first letter of every word in a string without calling title().

Given Input: text = "hello world from python"

Expected Output: Hello World From Python

<details>
<summary>Reveal hint</summary>

Break the sentence into words, transform each, then reassemble it.

</details>

## Exercise 37. Simple Countdown Timer

Use a while loop for a countdown from a starting value. Follow the example by printing positive values, then Blast off! at zero.

Given Input: start_count = 5

Expected Output: 5 4 3 2 1 Blast off!

<details>
<summary>Reveal hint</summary>

Update the counter so the loop terminates; time.sleep can add a delay.

</details>

## Exercise 38. File Creation and Basic I/O

Create notes.txt, write the three example lines on separate lines, then read and display the file.

Given Input: Lines to write:

- “Hello, this is my first note.”

- “Python file handling is simple.”

- “End of file.”

Expected Output:

```text
notes.txt

Hello, this is my first note.
Python file handling is simple.
End of file.
```

<details>
<summary>Reveal hint</summary>

Use a context manager for files and include line breaks. Write mode replaces existing contents.

</details>

## Exercise 39. External File Word Counter

Read an existing text file and report its total word count.

Given Input:

An external file sample.txt containing: “Coding is the language of the future.”

Expected Output: The file contains 7 words.

<details>
<summary>Reveal hint</summary>

Read the text, separate it into words, and count them. Handle a missing file.

</details>

## Exercise 40. Introduction to Classes (OOP)

Define a Car class holding make, model, and year. Give it a start_engine() method that announces which car has started.

Given Input: Make: “Toyota”, Model: “Camry”, Year: 2022

Expected Output: The 2022 Toyota Camry's engine is now running!

<details>
<summary>Reveal hint</summary>

An initializer stores instance attributes; methods access them through self.

</details>

# Python — Day 1

## Topics practiced

- Variables
- Strings
- Integers
- `print()`
- `type()`
- `if / else`
- Comparison operators
- Indentation

## Practice

Created variables to represent an IP address and the number of failed login attempts.

```python
ip = "192.168.1.10"
attempts = 2
```
Checked the data types using type().

Created a simple security condition to detect a possible brute-force attack:

if attempts >= 3:
    print("Possible brute force attack")
else:
    print("No worries, here doesn't happen anything at the moment")

The condition was tested with different values of attempts.

## What I learned
Strings are text values and are written inside quotes.
Integers represent whole numbers.
= assigns a value to a variable.
== compares values.
>= means greater than or equal to.
Python uses indentation to define code blocks.
if and else allow a program to make decisions.

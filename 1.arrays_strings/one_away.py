"""
Cracking the Coding Interview
Excercise solved by Jeremy Winterberg
15/06/18

1.5 One Away: There are three types of edits that can be performed on strings:
    - insert a char, remove a char, or replace a char
    Given two strings, write a function to check if they are one edit (or zero
    edits) away
    EXAMPLE
    pale, ple   -> true
    pales, pale -> true
    pale, bale  -> true
    pale, bake  -> false
"""


def one_away(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        print("String lengths differ by more than one char")
        return False


W1 = "pale"
W2 = "ple"
W3 = "bake"

one_away(W1, W2)  # should be true
one_away(W1, W3)  # should be false

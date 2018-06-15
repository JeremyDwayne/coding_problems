"""
Cracking the Coding Interview
Excercise solved by Jeremy Winterberg
06/15/2018

1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a
    palindrome. A palindrome is a word of phrase that is the same forwards and backwards.
    A permutation is a rearrangement of letters. The palindrome does not need to be limited to
    just dictionary words.

    EXAMPLE
    Input:  Tact Coa
    Output: True (permutations: "taco cat", "atco cta", etc.)
"""

def palindrome_permutation(string):
    # Put string into a dict, and count how many of each char exist in the string
    string = string.lower().replace(' ', '')
    table = dict()
    for char in string:
        if char not in table:
            table[char] = 1
        else:
            table[char] += 1

    # check if all entries are even or at the most 1 entry is uneven (center char)
    # construct new string to create palindrome to return. May not be a real word.
    odd_count = 0
    new_string = ""
    for key, val in table.items():
        if val % 2 == 1:
            new_string = new_string[:len(new_string)//2] + key + new_string[len(new_string)//2:]
            odd_count += 1
            if odd_count > 1:
                return False, string + " is not a palindrome"
        else:
            new_string = key + new_string
            new_string = new_string + key

    return True, new_string

def main():
    str1 = "Tact Coa"   # True
    str2 = "Hannah"     # True
    str3 = "hanionah"   # False
    print(palindrome_permutation(str1))
    print(palindrome_permutation(str2))
    print(palindrome_permutation(str3))


main()

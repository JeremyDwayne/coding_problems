"""
 Cracking the Coding Interview
 Excercise solved by Jeremy Winterberg
 06/09/2018

 1.2 - Check Permutation: Given two strings, write a method to decide if one
       is a permutation of the other.

 Initial thoughts:
   1. Check if the strings are the same length, put the chars into array and
      sort, check if they are the same.
   2. Or, store each char into a hash counting how many of each char appears
      in one string, then subtract count for the second string.. if there are
      any with counts other than zero it's not a permutation.
      However, this approach is not efficient and would be a poor implementation.
"""

def is_permutation(str1, str2):
    """is_permutation

    :param str1:
    :param str2:
    """
    #if they're not the same length, they're not permutations
    if len(str1) != len(str2):
        return False

    # I decided to xor the two strings as sets
    # This will remove common characters and return a set of the remaining chars
    # if there are remaining chars, they're not permutations
    if set(str1) ^ set(str2):
        return False
    return True


def main():
    """main"""
    permutation_str1 = "hello"
    permutation_str2 = "lehlo"

    non_str1 = "whisper"
    non_str2 = "canyons"

    print("Is", permutation_str1, "a permutation of", permutation_str2,
          is_permutation(permutation_str1, permutation_str2))
    print("Is", non_str1, "a permutation of", non_str2,
          is_permutation(non_str1, non_str2))

main()

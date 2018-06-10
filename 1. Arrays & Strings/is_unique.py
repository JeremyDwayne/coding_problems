#!/usr/bin/env python3.6
# Cracking the Coding Interview
# Excercise solved by Jeremy Winterberg
# 06/09/2018

# 1.1 - Is Unique: Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?


# First thoughts:
#   Create some sort of hash table to store each letter as we go through.
#   Then you can look-up in the table if the key exists already in O(1) complexity.

def is_unique(word):
  lookup_table = dict()

  for c in word:
    num = ord(c)
    if c in lookup_table:
      return False
    else:
      lookup_table[c] = 1
  return True

def main():
  unique = "qwertyuiopasdfghjklzxcvbnm"
  non_unique = "qwertyasdfghjklqwerty"

  print("Is", unique, "unique?", is_unique(unique))
  print("Is", non_unique, "unique?", is_unique(non_unique))

  # Output
  # Is qwertyuiopasdfghjklzxcvbnm unique? True
  # Is qwertyasdfghjklqwerty unique? False

main()

# If I wasn't allowed to use a dict / hash table / data structure I would do a nested loop on the string
# to check the i'th char against the i+1'th char. This raises the complexity to O(n^2) however.
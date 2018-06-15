"""
 Cracking the Coding Interview
 Excercise solved by Jeremy Winterberg
 06/15/2018

 1.3 URLify: Write a method to replace all spaces in a string with '%20'.
             You may assume that the string has sufficient space at the end to
             hold the additional characters, and that you are given the "true" length
             of the string.

             EXAMPLE
             Input: "Mr John Smith    ", 13
             Output "Mr%20John%20Smith"
 """

def urlify(inpt):
    """ find spaces and replace with html code %20 for url friendliness """
    output = ""

    # strip out trailing whitespace, python doesn't care about array size
    inpt = inpt.rstrip()
    for i, char in enumerate(inpt):
        if ord(char) == 32:
            output += '%20'
        else:
            output += inpt[i]
    return output


def main():
    """ main """
    print(urlify("Mr John Smith    "))


main()

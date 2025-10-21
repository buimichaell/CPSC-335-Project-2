# Project 2
# Algorithm 2 - String Run Encoding
# ===================================
# Names:
# - Michael Bui
# - Natalia Garcia
# ===================================
# *** Psedocode ***
# def StrRunEnc(string) # input is a string
#   current = first char in string
#   count = number of similar character
#   new_string = empty string
#   if string is lowercase # string is all lowercase
#       for each char in string 
#           if current == char
#               count += 1
#           else 
#               add character to new_string
#
#           if count > 1
#               add count and car to newstring
#           current = char # update current char to next
#   return new_string
# ======================================          

"""Function that return a string with the number of similar characters
   and the similar character."""
def StrRunEncode(string):
    return new_string
# Project 2
# Algorithm 2 - String Run Encoding
# ===================================
# Member Names:
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
def StrRunEncode(str_input):
    curr = str_input[0] # initialized to first character of input
    count = 0
    new_string = "" # empty string to hold new string
    
    # handles error if input is not string
    if not str_input: 
        return ""
    
    if str_input.islower(): # checks if input is lowercase
        # iterates through each character in the string
        for char in str_input:
            if curr == char:
                count += 1
            else: 
                # executes when count is greater than 1
                if count > 1:
                    # converts count to string & adds to new string
                    new_string += str(count)
                # adds current character to new string    
                new_string += curr 
                
                count = 1 # resets count
                curr = char # updates current character

        if count > 0:
            intostr = str(count) # convert to string
            # add count & current character to new string
            new_string += f"{intostr}{curr}" 
            count = 0 # resets count   
    return new_string

# File to read input from
SAMPLE_INPUT = "input.txt"

with open(SAMPLE_INPUT, "r") as file:
    lines = file.read()
    print(StrRunEncode(lines))
# RegEx Module.
# Python has a built-in package called re, which can be used to work with Regular Expressions.
# Import the re module :
import re

# RegEx in Python.
# Search the string to see if it starts with "The" and ends with "Spain" :
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

# RegEx Functions.
# The re module offers a set of functions that allows us to search a string for a match :
# findall - returns a list containing all matches.
# search - returns a Match object if there is a match anywhere in the string.
# split - returns a list where the string has been split at each match.
# sub - replaces one or many matches with a string.

# Metacharacters.
# [] - a set of characters. Example : "[-m]"
# \ - signals a special sequence. Example : "\d"
# . - any character. Example : "he..o"
# ^ - starts with. Example : "^hello"
# $ - ends with. Example : "planet$"
# * - zero or more occurrences. Example : "he.*o"
# + - one or more occureneces. Example : "he.+o"
# ? - zero or one occurences. Example : "he.?o"
# {} - exactly the specified number of occurences. Example : "he.{2}o"
# | - either or. Example : "falls|stays"
# () - capture and group. 

# Sets.
# [arn] - returns a match where one of the specified characters (a, r, or n) is present.
# [a-n] - returns a match for any lower case character, alphabetically between a and n.
# [^arn] - returns a match for any character EXCEPT a, r, and n.
# [0123] - returns a match where any of the specified digits (0, 1, 2, or 3) are present.
# [0-9] - returns a match for any digit between 0 and 9.
# [0-5][0-9] - returns a match for any two-digit numbers from 00 and 59.
# [a-zA-Z] - returns a match for any character alphabetically between a and z, lower case OR upper case.
# [+] - in sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string.

# The findall() Function.
# The findall() function returns a list containing all matches :
import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# Return an empty list if no match was found :
import re
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

# The search() Function.
# The search() function searches the string for a match, and returns a Match object if there is a match.
# Search for the first white-space character in the string :
import re
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

# If no matches are found, the value None is returned :
import re
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

# The split() Function.
# The split() function returns a list where the string has been split at each match :
import re
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# Split the string only at the first occurrence :
import re
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

# The sub() Function.
# The sub() function replaces the matches with the text of your choice.
# Replace every white-space character with the number 9 :
import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# Replace the first 2 occurrences :
import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

# Match Object.
# Do a search that will return a Match Object :
import re
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) # this will print an object.

# The Match object has properties and methods used to retrieve information about the search, and the result.
# .span() returns a tuple containing the start-, and end positions of the match :
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

# .string returns the string passed into the function :
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

# .group() returns the part of the string where there was a match :
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
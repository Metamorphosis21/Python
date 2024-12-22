
# Formatting strings
# Concatenating and repeating strings
# Striping whitespaces
# Changing character case
# Comparison of strings
# Searching for a substring
# Replacing substrings
# Splitting and joining strings

# Character and character testing
# 1. isalnum() - Returns True if the string contains only alphanumeric characters (i.e., digits and letters).
# 2. isalpha() - Returns True if the string contains only alphabetic characters (i.e., letters).
# 3. isdecimal() - Returns True if the string contains only decimal integer characters (that is, base 10 integers) and does not contain a + or - sign.
# 4. isdigit() - Returns True if the string contains only digits (e.g., '0', '1', '2').
# 5. isidentifier() - Returns True if the string represents a valid identifier.
# 6. islower() - Returns True if all alphabetic characters in the string are lowercase characters (e.g., 'a', 'b', 'c').
# 7. isnumeric() - Returns True if the characters in the string represent a numeric value without a + or - sign and without a decimal point.
# 8. isspace() - Returns True if the string contains only whitespace characters.
# 9. istitle() - Returns True if the first character of each word in the string is the only uppercase character in the word.
# 10. isupper() - Returns True if all alphabetic characters in the string are uppercase characters (e.g., 'A', 'B', 'C').

# Regular Expression
import re

# re.fullmatch() - Determine if the regular expression matches the entire string.
pattern = '011245'
print("Match" if re.fullmatch('[A-Z][a-z]*', 'E') else "No match")

# re.sub(pattern, replacement, string) - Replace all occurrences of the pattern in the string with the replacement string.
print(re.sub(r'_', ' ', 'This_is_basic_string_'))
print(re.sub(r'_', ' ', 'This_is_basic_string_',count = 2))

# re.split(pattern, string, maxsplit) - Split the string into a list of substrings.
print(re.split(',','This,is,basic,string,to,check,spilt, method'))
print(re.split(',','This,is,basic,string,to,check,spilt, method',maxsplit = 3))

# re.search(pattern, string) - Search for the first occurrence of the pattern in the string.
res = re.search('to','This is basic string to check search method')
print(res.group())

# Notes++
##### Strings #####
# Def: a string is a sequence of characters. They are immutable - any modifications on the string creates a new string. They allow for indexing, slicing and iteration. They are unicode meaning
# they can store chars from any lang and special chars. 

s = 'Hello'
first_char = s[0]  # 'H'
last_char = s[-1]  # 'o'

s = 'Hello'
sub_s = s[1:4]  # 'ell'

s = 'Hello World'
s_split = s.split()  # ['Hello', 'World']

words = ['Hello', 'World']
s_joined = ' '.join(words)  # 'Hello World'

s = "some string/"

s.strip()
s.strip('/')
str(s) # uses the \n
repr(s) # This is nice for debugging

##### Format specifier #####
num = 5
formatted_str = f"{num:>3d}"

num = 3.14159
formatted_str = f"{num:0.2f}"

num = 7
formatted_str = f"{num:03d}"
print(f"'{formatted_str}'")
# Output: '007'

text = "Hello"
formatted_str = f"{text:^10s}" # Center aligned
print(f"'{formatted_str}'")
# Output: '  Hello   '

ratio = 0.4567
formatted_str = f"{ratio:.2%}"
print(f"'{formatted_str}'")
# Output: '45.67%'

num = 1234567890
formatted_str = f"{num:,d}"
print(f"'{formatted_str}'")
# Output: '1,234,567,890'

num = 10
formatted_str = f"{num:b}" # Binary
print(f"'{formatted_str}'")
# Output: '1010'

num = 255
formatted_str_lower = f"{num:x}" # Hexidecimal 
formatted_str_upper = f"{num:X}"
print(f"'{formatted_str_lower}', '{formatted_str_upper}'")
# Output: 'ff', 'FF'

# Questions 
"""
Easy
- Reverse a String: Write a function to reverse a string.
- Check Palindrome: Write a function to check if a string is a palindrome.
- Count Vowels: Write a function to count the number of vowels in a string.
- Remove Spaces: Write a function to remove all spaces from a string.
- Check Anagram: Write a function to check if two strings are anagrams.

Medium
Longest Substring Without Repeating Characters: Write a function to find the length of the longest substring without repeating characters.
String to Integer: Write a function to convert a string to an integer.
Find Duplicate Characters: Write a function to find all duplicate characters in a string.
String Compression: Write a function to perform basic string compression using the counts of repeated characters.
Longest Common Prefix: Write a function to find the longest common prefix among a list of strings.

Hard
KMP Algorithm: Implement the KMP algorithm for pattern searching in a string.
Minimum Window Substring: Write a function to find the minimum window substring which contains all characters of another string.
Longest Palindromic Substring: Write a function to find the longest palindromic substring.
Group Anagrams: Write a function to group anagrams from a list of strings.
Z Algorithm: Implement the Z algorithm for pattern searching in a string.
Edit Distance: Write a function to calculate the edit distance between two strings.
Rabin-Karp Algorithm: Implement the Rabin-Karp algorithm for pattern searching in a string.
Word Break: Write a function to determine if a string can be segmented into a space-separated sequence of one or more dictionary words.
Permutations of a String: Write a function to generate all permutations of a given string.
Rotate String: Write a function to determine if one string is a rotation of another.
"""
# Count the number of times 'a' shows up in a string 
from collections import Counter 
word = "apples hcjaa aplha techno james"
g = Counter(words)
print(g.get('a'))

# Reverse a String: Write a function to reverse a string.
def rev_string(s):
  return(s[::-1])

# Check Palindrome: Write a function to check if a string is a palindrome.
def check_palindrome(s):
  return(s == s[::-1])

# Count Vowels: Write a function to count the number of vowels in a string.
def count_vowels(s):
  v = [c for c in s.lower() if c in "aeiou"]
  return(len(v))
# Or
def count_vowels(s):
  return sum(1 for char in s.lower() if char in 'aeiou')

# Remove Spaces: Write a function to remove all spaces from a string
def remove_spaces(s):
  reutrn(s.replace(" ", ""))

# Check Anagram: Write a function to check if two strings are anagrams.
def is_anagram(s1, s2):
  return(sorted(s1) == sorted(s2))
# s1: aabcccc s2: aabcccc sorted strings are easy to check but not as optimized 
# Or more optimized in time complexity but may lack in space complexity: 
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    def build_dict(s):
        s_dict = {}
        for c in s:
            s_dict[c] = s_dict.get(c, 0) + 1 # If there is no val for c then add s_dict.get(c, 0) to 1 which will yield 0 + 1
        return s_dict

    s1_dict = build_dict(s1)
    s2_dict = build_dict(s2)

    for key, value in s1_dict.items():
        if s2_dict.get(key, 0) != value:
            return False
        
    return True
# Or more optimized in both time complexity and space complexity: 
def is_anagram(s1, s2):
  if len(s1) != len(s2):
        return False
    
    count = {}

    for char in s1:
        count[char] = count.get(char, 0) + 1
    
    for char in s2:
        if char in count:
            count[char] -= 1
            if count[char] == 0:
                del count[char]
        else:
            return False
    
    return len(count) == 0

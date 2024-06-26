##### Strings #####
s = "some string/"

s.strip()
s.strip('/')
str(s) # uses the \n
repr(s) # prints the newline chat \n. This is nice for debugging

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
"""

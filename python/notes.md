# General Python Notes
__Locale__ -  Refers to the set of cultural and linguistic conventions used by a computer program to format and display data such as dates, times, numbers, and currency in a way
that is familiar to users from a particular region or language.

```python
import locale

# Set locale to US English
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Format a number according to the current locale
number = 1234567.89
formatted_number = locale.format_string("%d", number, grouping=True)
print(formatted_number)  # Output: '1,234,567'

# Set locale to German
locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')
```
__Garbage Collector__ - is a part of the Python memory management system that automatically frees up memory by removing objects that are no longer needed by the program. This helps prevent memory leaks and ensures that your program doesn't use more memory than necessary. It uses a concept of reference counting. Every Python has a ref count which keeps track of how many refs point to that
object. When the ref count drops to zero the object is no longer needed and Python can safly delete it. 

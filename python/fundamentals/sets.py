""" Def: unordered collection of unique elements. While a set is mutable (You can add or remove elements), elements in a set must be immutable, meaning they cannot be changed, 
but the set itself is mutable, so you can add or remove elements. They can not be indexed. Printing out puts won't always be in the same order. 

Use Cases: 
- Removing Duplicates: From a list of elements.
- Membership Testing: Checking if an element exists in a collection.
- Set Operations: Performing mathematical operations like union, intersection, etc.
- Filtering Data: Based on unique criteria.
- Tagging: Managing unique tags for objects.

"""

my_set = {1, 2, 3}
my_set.update({1, 2, 3})
my_set.add(4)
my_set.remove(2) # raises a KeyError exception when the item to delete is not found in the set
my_set.discard(2) # does not raise any exceptions and does nothing if the item is not found in the set.

# Set Math Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
intersection_set = set1 & set2
difference_set = set1 - set2
sym_diff_set = set1 ^ set2


##### Questions:
"""
# Medium Difficulty
Basic Set Operations: Write a function that takes two lists and returns their union, intersection, and difference as sets.
Remove Duplicates: Write a function that removes duplicates from a given list using sets.
Unique Characters: Given a string, write a function to determine if it has all unique characters using a set.
Set Comprehension: Create a set of squares of numbers from 1 to 10 using set comprehension.
Symmetric Difference: Write a function that finds the symmetric difference between two sets.
Find Common Elements: Given two lists, write a function that returns a list of elements that are common to both lists using sets.
Subset Check: Write a function to check if one set is a subset of another.
Unique Words: Write a function that takes a sentence and returns the unique words in it.
Set Equality: Write a function to check if two sets are equal.
Remove Items: Given a list, write a function to remove specified elements using a set.

# Hard Difficulty
Pair Sum Problem: Write a function to find all pairs of integers in a list that sum up to a given number using sets.
Anagram Check: Write a function that checks if two strings are anagrams of each other using sets.
Common Characters: Write a function to find all common characters in a list of strings using sets.
Set Partition: Write a function that partitions a set into two sets such that the sum of elements in both sets is equal, if possible.
Longest Consecutive Sequence: Given a list of integers, write a function to find the length of the longest consecutive sequence using sets.
Valid Parentheses: Write a function to check if a string containing just the characters '(', ')', '{', '}', '[' and ']' is valid using sets.
Set Operations: Given multiple lists, write a function to perform various set operations (union, intersection, difference) on them.
Unique Subsets: Write a function to generate all unique subsets of a set.
Jaccard Similarity: Write a function to calculate the Jaccard similarity between two sets.
Maximum Subset: Write a function to find the largest subset such that all elements in the subset are pairwise relatively prime.

# Really Hard Difficulty
Permutation Check: Write a function to check if one string is a permutation of another using sets.
Set Cover Problem: Write a function to solve the set cover problem where you need to cover a universal set with the minimum number of subsets.
Word Break Problem: Given a string and a dictionary of words, write a function to determine if the string can be segmented into a space-separated sequence of dictionary words using sets.
Distinct Subsequences: Write a function to find the number of distinct subsequences of a given string using sets.
Set Intersection: Given a collection of sets, write a function to find the intersection of all sets.
Graph Coloring: Write a function to determine if a graph can be colored with two colors such that no two adjacent nodes have the same color using sets.
Minimal Spanning Tree: Write a function to find the minimal spanning tree of a graph using sets.
Topological Sorting: Write a function to perform topological sorting on a directed acyclic graph (DAG) using sets.
Hamiltonian Path: Write a function to determine if a Hamiltonian path exists in a graph using sets.
N-Queens Problem: Write a function to solve the N-Queens problem using sets to track column and diagonal conflicts.

"""

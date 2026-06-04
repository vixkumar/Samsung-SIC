"""
def find_two(nums):
    x = y = 0
    for i in rnage(1, len(nums)):
"""

import string

def word_count(S, x):
    count = 0
    for i in range(0, len(S)):
        if S[i] ==x:
          count +=1
    return count

S = list(input("input a sentence: ").split())
x = input("Enter a word to match : ")

S = [word.strip(string.punctuation).lower() for word in S]
x = x.lower()

c = word_count(S, x)
print(f"In S, '{x}' appears {c}times.")


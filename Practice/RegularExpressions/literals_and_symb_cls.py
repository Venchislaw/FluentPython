import re


text = "Bread, Dead, Instead, Eat"
match = re.findall(r"[eE]a[dt]", text)
print(match)  # bam!
# ['ead', 'ead', 'ead', 'Eat']

"""
[] works as "or" operator
"""

# now let's find all words starting with digit

text = "H3llo, 1m 7rogramming 4ere!"
match = re.findall(r"\b[0-9].*", text)
print(match)  # ['1m 7rogramming 4ere!']

# okay... I was sitting and wondering:
# why code below returns []

text = "H3llo, 1m 7rogramming 4ere!"
match = re.findall(r"^[0-9].*", text)
print(match)  # []

# it doesn't work as it uses ^ anchor
# it works only for beginning of the string, not for each word


# in this case ^ works as "not" operator
match = re.findall(r"[^0-9]", text)
print(match)


# Regular Expressions also have flags
# Such flags can change behaviour of RE
text = "안녕 세계"
# in this case ^ works as "not" operator
match = re.findall(r"\w", text, re.ASCII)
print(match)  # []
# but:
match = re.findall(r"\w", text)
print(match)  # ['안', '녕', '세', '계']

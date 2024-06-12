"""
Learning Regular Expressions through Introducing Python book
"""

import re

# we use regex to find/match/filter strings by pattern

input_string = "Hello world!"
result = re.match("Hello", input_string)
print(bool(result))

# for longer regex we can compile pattern
hello_pattern = re.compile("Hello")
print(bool(hello_pattern.match(input_string)))

"""
Match function searches pattern in the beginning
Personally I'm not sure it's that useful
As we have .startswith(pattern)
"""

# I converted it to bool, but we can see
# part that matched

m = re.match("Hello", input_string)

if m:
    print(m.group())

# however match can be used not only for
# checking beginning of the string


new_pattern = re.compile(".*world")

print("-" * 60)

try:
    print(new_pattern.match(input_string).group())
except:
    print("Smth went wrong")

print("-" * 60)
new_input_str = "Hello world world!"

try:
    print(new_pattern.match(new_input_str).group())
except:
    print("Smth went wrong")

print("-" * 60)

# In this use case it's slightly different from .search()
# as search looks for the first match in string

# In search we don't specify .* as .search() searches
# In any part of the string

m = re.search("world!", input_string)

if m:
    print(m.group())
else:
    print("No substring found")

# Knowing match() it's pretty easy to understand search()

"""
findall() returns list of all matches
"""

m = re.findall("l", input_string)
print(f"{len(m)} matches found: {m}")

m = re.findall("l.?", input_string)
print(m)

# regex functions similar to ordinary python ones

# similar to replace()
input_str_transformed = re.sub("l", "L", input_string)
print(input_str_transformed)

# similar to split()
input_str_splitted = re.split("L", input_str_transformed)
print(input_str_splitted)

# deeper article on RE:
# https://docs.python.org/3/library/re.html

"""
Summing up:

we could use .findall() for all our use cases via
special symbols.

^ and $ etc. (btw. these are called anchors)
"""

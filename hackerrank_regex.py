#You are given a string . It consists of alphanumeric characters, spaces and symbols(+,-).
#Your task is to find all the substrings of  that contains  or more vowels.
#Also, these substrings must lie in between  consonants and should contain vowels only.









#solution follows below
import re

sol = re.findall(r'[^aiueo]([aiueoAIUEO]{2,})(?=[^aiueo])', input())

if sol:
    for s in sol:
        print(s)
else:
    print(-1)

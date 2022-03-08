def remove_vowels(string):
    for c in string.lower():
        if c in vowels:
            string=string.replace(c,'')
    return string

string=input('Enter the input string : ')

vowels=('a','e','i','o','u')

string=remove_vowels(string)

print('The string after removing vowels is : '+string)

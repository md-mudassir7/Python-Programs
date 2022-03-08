str_1 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."
 
spaces_and_letters = ""
 
# this for loop reduces the string to letters, numbers, and spaces
for char in str_1:
    if char.isalnum() or char.isspace() or char == "-" or char == "'":
        spaces_and_letters += char
 
# .split() is used to put the words the into a list
words = spaces_and_letters.split()
print(spaces_and_letters)
number_of_words = len(words)
 
# print(words)
print(number_of_words)
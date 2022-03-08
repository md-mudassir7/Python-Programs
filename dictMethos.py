famous_songs = {"Queen": "Bohemian Rhapsody",
                "Bee Gees": "Stayin' Alive",
                "U2": "One",
                "Michael Jackson": "Billie Jean",
                "The Beatles": "Hey Jude",
                "Bob Dylan": "Like A Rolling Stone"}  # 1 and 2
print(len(famous_songs))  # 3
for key in famous_songs.keys():  # 4
    print(key)
print(famous_songs.values())  # 5
for key, value in famous_songs.items():  # 6
    print(key, value)
print(famous_songs.get("Promise of the Real", "That is not a key that appears in the dictionary."))  # 7
print(famous_songs)
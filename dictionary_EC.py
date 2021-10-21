"""
This file will open a text file containing the Book of John,
break it into lines and strip the lines of spaces.  Once that is 
done, the lines will be broken up into words, which will then 
be looped through to either be added to as a key to a dictionary 
or increase the count of the key that corresponds to that word.
"""

# Opening the file
txt_file = open("book of John text.txt", "r")

# Creating an empty dictionary to append to
d = dict()

# Beginning the loop to iterate through the lines
for line in txt_file:

    # Remove the white space on either side of the lines
    clean_line = line.strip()

    # Now split the lines up at blank spaces to get the words
    words = clean_line.split(" ")

    # Now we write the loop to iterate through words
    # and either add them to the dictionary or increment
    # its count by one in the dictionary
    for word in words:
        if word in d:
            d[word] = d[word] + 1

        else:
            d[word] = 1

for key in list(d.keys()):
    if (
        key == "Father"
        or key == "God"
        or key == "Christ"
        or key == "Spirit"
        or key == "life"
        or key == "man"
        or key == "spirit"
    ):
        print(key, ":", d[key])

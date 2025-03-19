def longest_word(file_name):
    with open(file_name,"r") as file:
        words = file.read()
    word_list = words.split()
    longest = word_list[0]
    for w in word_list[1:]:
        if len(longest)<len(w):
            longest = w
    return longest
print(longest_word("myfile.txt"))
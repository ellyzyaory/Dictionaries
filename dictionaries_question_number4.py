def word_frequencies(mylist):
    count = {}
    for character in mylist.split():
        count.setdefault(character, 0)
        count[character] += 1
    return count

if __name__=="__main__":
    user_input = input("Enter a sentence: ")
    print(word_frequencies(user_input))


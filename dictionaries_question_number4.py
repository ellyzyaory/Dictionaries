def word_frequencies(mylist):
    count = {}
    for word in mylist.split():
        count.setdefault(word, 0)
        count[word] += 1
    return count

if __name__=="__main__":
    user_input = input("Enter a sentence: ")
    print(word_frequencies(user_input))


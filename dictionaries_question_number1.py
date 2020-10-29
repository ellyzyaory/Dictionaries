def remove_keys(mydict, keylist):
    for keys in keylist:
        if keys in mydict:
             mydict.pop(keys)
    return mydict

if __name__ == "__main__":
    dictionary = {"Indonesia":"Jakarta", "Japan":"Tokyo", "Russia":"Moscow"}
    print(dictionary)
    key = input("Enter the keys to remove items (Seperated by a comma): ").split(",")
    print(remove_keys(dictionary, key))

def find_value(mydict, val):
    world = []
    for key, value in mydict.items():
        if value == val:
            world.append(key)
    return world

if __name__ == "__main__":
    dictionary = {"Indonesia":"Jakarta", "Japan":"Tokyo", "Russia":"Moscow"}
    print(dictionary)
    user_input = input("Enter a city from the following choice: ")
    print(find_value(dictionary, user_input))


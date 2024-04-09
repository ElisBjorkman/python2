

def count_letters(sentence):
    dictionary =  {}

    sentence.lower()

    for letter in sentence:


        if letter in dictionary:
            dictionary[letter] += 1

        else:
            dictionary[letter] = 1


    return dictionary



print(count_letters("Test"))




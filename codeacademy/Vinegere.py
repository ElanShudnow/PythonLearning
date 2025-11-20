import string
alphabet = string.ascii_lowercase

message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!"
keyword = "friends"

def vinegere_decode(message, keyword):
    new_message = ""
    index = 0
    for letter in message:
        if letter in alphabet:
            character_index_in_alphabet = alphabet.index(letter)
            if index >= len(keyword):
                index = 0
            keyword_index_in_alphabet = alphabet.index(keyword[index])
            new_index_in_alphabet = (character_index_in_alphabet + keyword_index_in_alphabet) % 26
            offset_index_in_alphabet = alphabet[new_index_in_alphabet]
            new_message += offset_index_in_alphabet
            
            index += 1
        else:
            new_message += letter
    return new_message

print(vinegere_decode(message, keyword))


import string
alphabet = string.ascii_lowercase

message = "you were able to decode this? nice work! you are becoming quite the expert at crytography!"
keyword = "friends"

def vinegere_encode(message, keyword):
    new_message = ""
    index = 0
    for letter in message:
        if letter in alphabet:
            character_index_in_alphabet = alphabet.index(letter)
            if index >= len(keyword):
                index = 0
            keyword_index_in_alphabet = alphabet.index(keyword[index])
            new_index_in_alphabet = (character_index_in_alphabet - keyword_index_in_alphabet) % 26
            offset_index_in_alphabet = alphabet[new_index_in_alphabet]
            new_message += offset_index_in_alphabet
            
            index += 1
        else:
            new_message += letter
    return new_message

print(vinegere_encode(message, keyword))






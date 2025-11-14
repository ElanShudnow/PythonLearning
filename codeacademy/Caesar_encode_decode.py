import string
alphabet = string.ascii_lowercase

#message = "This is a message!  This should be encrypted.  Hope you can dencrypt it..."
message1 = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
message2 = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
message_unknown_offset = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

def caesar_decode(message, offset):
    new_message = ""
    for letter in message:
        if letter in alphabet:
            current_index_in_alphabet = alphabet.index(letter)
            new_index_in_alphabet = (current_index_in_alphabet + offset) % 26
            offset_index_in_alphabet = alphabet[new_index_in_alphabet]
            new_message += offset_index_in_alphabet
        else:
            new_message += letter
    return new_message

print(caesar_decode(message1, 10))
print(caesar_decode(message2, 14))

for attempt in range(1,27):
    #print(caesar_decode(message_unknown_offset, attempt))
    print("Offset: {}".format(attempt))
    print("\t {}".format(caesar_decode(message_unknown_offset, attempt)))







def caesar_encode(message, offset):
    new_message = ""
    for letter in message:
        if letter in alphabet:
            current_index_in_alphabet = alphabet.index(letter)
            new_index_in_alphabet = (current_index_in_alphabet - offset) % 26
            offset_index_in_alphabet = alphabet[new_index_in_alphabet]
            new_message += offset_index_in_alphabet
        else:
            new_message += letter
    return new_message


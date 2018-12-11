#  Copyright (c) 2018 Paul König. All rights reserved.
#
#  python Version 3.7; should work on 3.x
#
#  encoding: utf-8
#
#
#  *****************************************************
import time
import random
import string

filename: str = 'Twist/twist1.txt'


class DataProcessing:

    def __init__(self, str_or_filename, dic_file):
        if ".txt" in str_or_filename:
            self.text = DataProcessing.list_take_apart(DataProcessing.inputread(str_or_filename))
        else:
            self.text = DataProcessing.list_take_apart(DataProcessing.string_import(str_or_filename))
        self.dictionary = DataProcessing.dictionary_import(dic_file)
        self.encrypted = []
        self.decrypted = []

    @staticmethod
    def inputread(file):
        results = []
        with open(file) as f:
            for line in f:
                for word in line.split():
                    results.append(word)
                    results.append(' ')
        return results

    @staticmethod
    def string_import(input_string):
        buffer = []
        output = []
        for character in input_string:
            if character.isalpha():
                buffer.append(character)
            else:
                output.append(buffer)
                buffer = []
                output.append([character])
        output.append(buffer)
        return output

    @staticmethod
    def dictionary_import(file):
        results = []
        with open(file) as f:
            for line in f:
                for word in line.split():
                    results.append(word)
        return results

    @staticmethod
    def list_take_apart(text_raw_list):
        buffer = []
        text_output = []
        for text_part in text_raw_list:
            for character in text_part:
                if character.isalpha():
                        buffer.append(character)
                elif not character.isalpha():
                    if not buffer == []:
                        text_output.append(buffer)
                        buffer = []
                    text_output.append([character])
        if not buffer == []:
            text_output.append(buffer)
        return text_output

    def encode_helper(self):
        for part in self.text:
            if len(part) <= 1:
                self.encrypted.append(''.join(part[0]))
            elif len(part) == 2:
                self.encrypted.append(''.join(part[0] + part[-1]))
            elif len(part) == 3:
                self.encrypted.append(''.join(part))
            else:
                random_elements = part[1:-1]
                random.shuffle(random_elements, random.random)
                self.encrypted.append(''.join(part[0] + ''.join(random_elements) + part[-1]))

    def decode_helper(self):
        alphabet = list(string.ascii_lowercase + "ö" + "ü" + "ä")
        for part in self.text:
            local_dictionary = []
            buffer = []
            twist_character = []
            local_wordlist = []
            if len(part) <= 3:
                buffer = ''.join(part)
            else:
                for item in self.dictionary:
                    if len(item) == len(part) and item[0].lower() == part[0].lower() \
                            and item[-1].lower() == part[-1].lower():
                        local_dictionary.append(item.lower())
                for item in local_dictionary:
                    list(item)
                    puffer = []
                    for letter in alphabet:
                        for character in item[1:-1]:
                            if character == letter:
                                puffer.append(letter)
                    local_wordlist.append(puffer)
                for character in alphabet:
                    for twistlist_character in part[1:-1]:
                        if twistlist_character == character:
                            twist_character.append(twistlist_character)
                for item in local_wordlist:
                    if item == twist_character:
                        buffer = part[0] + local_dictionary[local_wordlist.index(item)][1:-1] + part[len(part) - 1]
            self.decrypted.append(buffer)

    def do_translation(self):
        self.encode_helper()
        self.decode_helper()


def start(file_or_str_input, dictionary):
    global text_translate
    text_translate = DataProcessing(file_or_str_input, dictionary)
    DataProcessing.do_translation(text_translate)


if __name__ == "__main__":  # local test
    start_time = time.time()
    start(filename, "woerterliste.txt")
    print(''.join(str(e) for e in text_translate.encrypted) +
                  '\n' + ''.join(str(e) for e in text_translate.decrypted))
    print("runtime: {:.4f} s".format(time.time() - start_time))

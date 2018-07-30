# -----------------------------------------------------------------------------
# Name:  Max Kagan wordstats
# Purpose: Counts unique words from a txt file
#
# Author: Max Kagan
# Date: 7/15/2018
# -----------------------------------------------------------------------------
"""
Takes a txt input file and counts unique words

Using a global dictionary variable, this program loops over individual
lines in a file and counts each unique words then adds to a total
of times the word has been seen in the file
"""

# The following imports are needed for the draw_cloud function.
import tkinter
import tkinter.font
import random
import string

word_count = {}
"""
:var word_count A global dictionary to hold the values found by the
count_words function"""


# The draw_cloud function is only needed for the optional part:
# to generate a word cloud.
# You don't need to change it.


def draw_cloud(input_count, min_length=0):
    """
    Generate a word cloud based on the input count dictionary specified.

    Parameters:
    input_count (dict): represents words and their corresponding counts.
    min_length (int):  optional - defaults to 0.
         minimum length of the words that will appear
         in the cloud representation.
    Only the 20 most common words (that satisfy the minimum length criteria)
    are included in the generated cloud.
    """
    root = tkinter.Tk()
    root.title("Word Cloud Fun")
    # filter the dictionary by word length
    filter_count = {
        word: input_count[word] for word in input_count
        if len(word) >= min_length}
    max_count = max(filter_count.values())
    ratio = 100 / max_count
    frame = tkinter.Frame(root)
    frame.grid()
    current_row = 0
    for word in sorted(filter_count, key=filter_count.get, reverse=True)[0:20]:
        color = '#' + str(hex(random.randint(256, 4095)))[2:]
        word_font = tkinter.font.Font(size=int(filter_count[word] * ratio))
        label = tkinter.Label(frame, text=word, font=word_font, fg=color)
        label.grid(row=current_row % 5, column=current_row // 5)
        current_row += 1
    root.mainloop()


# Enter your own helper function definitions here

def count_words(filename):
    """Takes a line of a txt file then creates/updates a global dictionary
     consisting of the count of unique words

     :param filename a single line from the text file that is read in main
     :returns A list representation of the original line of
     strings from the file"""
    # build and return the dictionary for the given filename
    input_string = str(filename)
    input_string = input_string.lower()
    input_string = input_string.split()
    for word in input_string:
        exclude = set(string.punctuation)
        word = ''.join(ch for ch in word if ch not in exclude)
        word = ''.join([number for number in word if not number.isdigit()])
        if word != '':
            if word not in word_count.keys():
                word_count.update({word: 1})
            elif word in word_count.keys():
                word_count[word] += 1
    return input_string


def report(word_dict):
    """     Takes the large global dictionary and creates and output both
         in console and a file reporting on the longest word found and the
         top 5 words most reproduced in the file

         :param word_dict The dictionary of words and wordcounts created by
         count words funciton
         :return A console output and a .txt output"""
    # report on various statistics based on the given word
    # count dictionary
    print("Please wait a moment while output is generated....")
    for key in sorted(word_count):
        with open('out.txt', 'a', encoding='utf-8') as my_file:
            my_file.write("%s: %s\n" % (key, word_count[key]))
    list_of_keys = list(word_dict.keys())
    list_of_keys.sort(key=len, reverse=True)
    print("Longest word in file: " + list_of_keys[0])
    print('Top five most used words are:')
    sorted_value_dictionary_tuple = sorted(word_count.items(),
                                           key=lambda x: x[1], reverse=True)
    sorted_value_dictionary = sorted_value_dictionary_tuple[0:5]
    for key, value in sorted_value_dictionary:
        print("{}: {}".format(key, value))


def main():
    # get the input filename and save it in a variable
    file_input_location = input("Please enter a file destination")
    with open(file_input_location, 'r', encoding='utf-8') as my_file:
        for line in my_file:
            count_words(line)
        report(word_count)
        draw_cloud(word_count)


# save the dictionary in the variable word_count

# call report to report on the contents of the dictionary word_count

# If you want to generate a word cloud, uncomment the line below.
# draw_cloud(word_count)


if __name__ == '__main__':
    main()

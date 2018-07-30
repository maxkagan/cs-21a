# -----------------------------------------------------------------------------
# Name: Max Kagan aggregator.py
# Purpose:     CS 21A - implement a simple general purpose aggregator
#
# Author: Max Kagan
# -----------------------------------------------------------------------------
"""
Implement a simple general purpose aggregator

Usage: aggregator.py filename topic
filename: input  file that contains a list of the online sources (urls).
topic:  topic to be researched and reported on
"""

import urllib.request
import urllib.error
import re
import sys


def write_to_file(output_string, match_target):
    """
    Writes a formatted string to an output file
    Parameters:
    valid_matches (string) - data received from the format_and_search_data
                             function
    link_searched (string) - the link we searched through that contains
                             desired data
    Return:
    True or False (Bool) - True if results were found and outputted to file
                           False if results were not found and the output
                           file only contains a empty string
    """

    filename = match_target + 'summary.txt'
    if output_string == '':
        with open(filename, 'a', encoding='utf-8') as my_file:
            my_file.write("")
            my_file.close()
            return False
    else:
        with open(filename, 'a', encoding='utf-8') as my_file:
            my_file.write(output_string)
            my_file.close()
    return True


def generate_output_strings(valid_matches, link_searched):
    """
     Creates string to be used in file output generation
     Parameters:
     valid_matches (string) - data received from the format_and_search_data
                              function
     link_searched (string) - the link we searched through that contains
                              desired data
     Return:
     formatted_output (string) - a string that beautifies the output and is
                                 read directly on file output generation
     """
    end_line = '----------------------------------------\n'
    if valid_matches == '':
        return valid_matches
    else:
        formatted_output = ("Source url:" + '\n' + link_searched + '\n' +
                            (valid_matches + '\n') + end_line + '\n')
    return formatted_output


def format_and_search_data(parsed_html, match_target):
    """
    capture references to the given word found in the given html code
    Parameters:
    parsed_html (string) - the formatted string data from the html string
    match_target (string) - the word we are searching for
    Return:
    formatted_data (string) -  Words found between '>' and '<' characters
                               from the html source string input
    """
    formatted_data = ''
    # extract text inside brackets containing the match target
    regex = r'>([^><]*\b{}\b.*?)<'.format(match_target)
    try:
        valid_match = re.findall(regex, parsed_html, re.IGNORECASE | re.DOTALL)
    except:
        valid_match = False
    if valid_match:
        formatted_data = '\n'.join(valid_match)
    return formatted_data


def read_link(desired_link):
    """
    Reads a url and returns html source code if able to connect to the
    web server and decode the received data

    Parameters:
    desired_link (string) - String representation of a URL that we will
                          attempt to extract html source code from
    Return:
    read_data (string) - the decoded html file if the link was able to be read
                         and decoded using UTF-8
    """
    url_file = str(desired_link)
    try:
        with urllib.request.urlopen(desired_link) as opened_file:
            read_file = opened_file.read().decode('UTF-8')
            return read_file
    except urllib.error.URLError as url_err:
        print('Error opening url: ', url_file, url_err)
    except UnicodeDecodeError as decode_err:
        print('Error decoding url: ', url_file + '\n', decode_err)


def main():
    """
    Reads an input file as an argument and matches search targets as the
    second parameter
    :return: An output file with the name 'match_target" + summary.txt
    """
    # Check to see if correct number of arguments have been entered by the user
    if len(sys.argv) != 3:
        print("Error: Invalid number of arguments" + '\n')
        print('Usage: aggregator.py filename topic')
        return
    # Exceptions are caught and displayed by the functions called
    with open(sys.argv[1], 'r', encoding='utf-8') as my_file:
        match_target = sys.argv[2]
        desired_output = ''
        for line in my_file:
            page_data = read_link(line)
            search_results = format_and_search_data(page_data, match_target)
            desired_output = desired_output + generate_output_strings(
                search_results, line)
        return write_to_file(desired_output, match_target)


if __name__ == '__main__':
    main()

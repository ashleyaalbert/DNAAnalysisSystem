# Imports from other algorithm files
import os
from parse import query_parse, parse
from substring import longest_common_substring
from subsequence import LongCommSubSeq
from edit_distance import edit_distance
from substring_alignment import sub_alignment

def main():
    query_file = ''
    seq_file = ''
    # gets the current folder's absolute path
    current_folder = os.path.dirname(os.path.abspath(__file__))
    print("Welcome to the DNA Analysis System!")
    if input("Use the default DNA query / sequence files? (y/n): ") in ['y','Y']:
        # gets the correct file paths
        query_file = os.path.join(current_folder, 'DNA_query.txt')
        seq_file = os.path.join(current_folder, 'DNA_sequences.txt')
    else:
        print("Please enter the file name for the following:")
        query_file_input = input("Query sequence: ")
        query_file = os.path.join(current_folder, query_file_input)
        seq_file_input = input("Sequences to be searched aginst query: ")
        seq_file = os.path.join(current_folder, seq_file_input)

    # Select algorithm
    alg = select_alg(query_parse(query_file), parse(seq_file))

    # Compare query with other sequences using 'alg'
    do_alg(alg, query_parse(query_file), parse(seq_file))

def select_alg(s, t):
    # Display menu of algorithms
    print("Please select an algorithm to match sequences with: ")
    print("(1) Longest Common Substring")
    print("(2) Longest Common Subsequence")
    print("(3) Edit Distance")
    print("(4) Needleman-Wunsch Algorithm")
    print("(5) Substring Alignment and Frequency Algorithm")
    # TODO: Other algorithms
    algorithm = input("Enter corresponding number of algorithm of choice: ")

    # TODO: parse text files
    # TODO: Adjust with other algorithm function calls

    if algorithm == '1':
        # longest_common_substring()
        return longest_common_substring
    elif algorithm == '2':
        # LongCommSubSeq
        return LongCommSubSeq
    elif algorithm == '3':
        # Edit Distance
        return edit_distance
    elif algorithm == '4':
        # NeedleMan-Wunsch
        return
    elif algorithm == '5':
        # Substring alignment (idk what to call this)
        return sub_alignment
    else:
        print("Invalid input. Try again!")
        select_alg()

# TODO: printouts of comparisons...
# TODO: will each algorithm give a score 0-1? Each alg give a different output?
# TODO: need to give what dna matches the best specifically (give the gene)
def do_alg(alg, s, t):
    scores = []

    #print(t)

    min = ''
    for key in t.keys():
        scores.append(alg(s, t[key]))
        if (scores[-1] == max(scores)): min = key

    print("\n\nMOST SIMILAR:\n" + key)

main()
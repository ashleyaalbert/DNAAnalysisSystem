# Imports from other algorithm files
from parse import query_parse, parse

from substring import longest_common_substring
from subsequence import LongCommSubSeq
from edit_distance import edit_distance
from substring_alignment import sub_alignment

def main():
    query_file = ''
    seq_file = ''
    if input("Use the default DNA query / sequence files? (y/n) ") in ['y','Y']:
        query_file = 'DNA_query.txt'
        seq_file = 'DNA_sequences.txt'
    else:
        print("Please enter the file name for the following:")
        query_file = input("Query sequence: ")

        seq_file = input("Sequences to be searched aginst query: ")

    # Select algorithm
    alg = select_alg(query_parse(query_file), parse(seq_file))

def select_alg(s, t):
    # Display menu of algorithms
    print("Please select an algorithm to match sequences with: ")
    print("(1) Longest Common Substring")
    print("(2) Longest Common Subsequence")
    print("(3) Edit Distance")
    print("(4) Needleman-Wunsch Algorithm")
    print("(5) Substrng Alignment and Frequency Algorithm")
    # TODO: Other algorithms
    algorithm = input("Enter corresponding number of algorithm of choice: ")

    # TODO: parse text files
    # TODO: Adjust with other algorithm function calls

    if algorithm == '1':
        # longest_common_substring()
        return do_alg(longest_common_substring, s, t)
    elif algorithm == '2':
        # LongCommSubSeq
        return do_alg(LongCommSubSeq, s, t)
    elif algorithm == '3':
        # Edit Distance
        return do_alg(edit_distance, s, t)
    elif algorithm == '4':
        # NeedleMan-Wunsch
        return
    elif algorithm == '5':
        # Substring alignment (idk what to call this)
        return do_alg(sub_alignment, s, t)
    else:
        print("Invalid input. Try again!")
        select_alg()

# TODO: printouts of comparisons...
# TODO: will each algorithm give a score 0-1? Each alg give a different output?
def do_alg(alg, s, t):
    scores = []

    #print(t)

    for key in t.keys():
        scores.append(alg(s, t[key]))

    print('\n\nSCORES:\n', scores)

main()
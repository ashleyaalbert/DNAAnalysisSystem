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
    print("\nWelcome to the DNA Analysis System!")
    if input("\nUse the default DNA query / sequence files? (y/n): ") in ['y','Y']:
        # gets the correct file paths
        query_file = os.path.join(current_folder, 'DNA_query.txt')
        seq_file = os.path.join(current_folder, 'DNA_sequences.txt')
    else:
        fnames = os.listdir(current_folder)
        while query_file == '':
            print("\nPlease enter the file name for the following:")
            query_file_input = input("Query sequence: ")

            if query_file_input not in fnames: 
                print("\nThis file does not exist.")
            else:
                query_file = os.path.join(current_folder, query_file_input)

                if os.path.getsize(query_file) == 0 or query_parse(query_file) == '':
                    print("This file is empty.")
                    query_file = ''

        while seq_file == '':
            seq_file_input = input("\nSequences to be searched aginst query: ")

            if seq_file_input not in fnames:
                print("\nThis file does not exist.")
            else:
                seq_file = os.path.join(current_folder, seq_file_input)

                if os.path.getsize(seq_file) == 0 or parse(seq_file) == '':
                    print("This file is empty.")
                    seq_file = ''

    run = True
    while(run):
        # Select algorithm
        alg = select_alg(query_parse(query_file), parse(seq_file))
        # Compare query with other sequences using 'alg'
        do_alg(alg, query_parse(query_file), parse(seq_file))
        if input("Would you like to enter another algorithm or quit? (y/n): ") in ['y','Y']:
            continue
        else:
            print("Thank you for using the DNA Analysis System!")
            run = False

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
def do_alg(alg, s, t):
    scores = []

    #print(t)

    maxK = ''
    print("All Scores:")
    for key in t.keys():
        scores.append(alg(s, t[key]))
        if (scores[-1] == max(scores, key=lambda x:x[1])): maxK = key
        print("\nSCORE: ("+str(scores[-1][1])+") : " + key + ("" if scores[-1][0] == "" else str(scores[-1][0])) )

    print("\n\nMOST SIMILAR:\n" + maxK)

main()
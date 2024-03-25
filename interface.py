# Imports from other algorithm files
from subsequence import LongCommSubSeq

def main():
    print("Please enter the file name for the following:")
    query_file = input("Query sequence: ")

    seq_file = input("Sequences to be searched aginst query: ")

    # Select algorithm
    alg = select_alg()

def select_alg():
    # Display menu of algorithms
    print("Please select an algorithm to match sequences with: ")
    print("(1) Longest Common Substring")
    print("(2) Longest Common Subsequence")
    print("(3) Edit Distance")
    print("(4) Needleman-Wunsch Algorithm")
    # TODO: Other algorithms
    algorithm = input("Enter corresponding number of algorithm of choice: ")

    # TODO: parse text files
    # TODO: Adjust with other algorithm function calls
    if algorithm == 1:
        # LongCommSeq()
        return
    elif algorithm == 2:
        # LongCommSubSeq
        return
    elif algorithm == 3:
        # Edit Distance
        return
    elif algorithm == 4:
        # NeedleMan-Wunsch
        return
    else:
        print("Invalid input. Try again!")
        select_alg()

main()
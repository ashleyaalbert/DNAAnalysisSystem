'''
Using dynamic programming, we can calculate the longest non-contiguous 
substring between two strings
'''

def LongCommSubSeq(query, input):
    # Define the lengths of both inputs
    m = len(query)
    n = len(input)

    # Create arrays to store the lengths of common subproblems and the tracking of characters added to the LCS
    c = [[0] * (n + 1) for _ in range(m + 1)]  # Substring length array
    b = [[''] * (n + 1) for _ in range(m + 1)]  # Tracking array

    # Iterate through each letter in the query
    for i in range(1, m + 1):
        # Iterate through each letter in the input
        for j in range(1, n + 1):

            # If the letters match, increase the value for the LCS
            if query[i - 1] == input[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 'diag'  # Diagonal indicates the addition of a character to the LCS
            
            # If the letters don't match, take the maximum of the previous LCS values
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = 'up'  # Up arrow indicates skipping a character in query

            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = 'left'  # Left arrow indicates skipping a character in input

    # Reconstruct the LCS string by iterating through table b
    # until a basecase is reached (when i == 0 or j == 0)
    lcs = ""
    i, j = m, n
    while i > 0 and j > 0:
        if b[i][j] == 'diag':
            lcs = query[i - 1] + lcs
            i -= 1
            j -= 1
        elif b[i][j] == 'up':
            i -= 1
        else:
            j -= 1

    return lcs

# Testing
# query = 'springtime'
# s1 = 'pioneer'
# s2 = 'CGGACAT'
# print('The longest common substring is:', LongCommSubSeq(query, s1))
# print('s2-CGGACAT: The longest common substring is:', LongCommSubSeq(query, s2))

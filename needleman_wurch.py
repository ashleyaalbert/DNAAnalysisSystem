def needleman_wurch(query, input):
    query
    input

    seq1Length = len(query)  #Seq1 will be the vertical sequence
    seq2Length = len(input)  #Seq2 will be the horizontal sequence
    init_mat = []                                  

    #Scoring system
    match = 1
    mismatch = -1
    gap = -1

    #Initialising the matrix to 0:
    for i in range(seq1Length+1):                            #Adding +1 as one extra column needed to hold the initialised values
        temp = []
        for j in range(seq2Length+1):                        
            temp.append(0)
        init_mat.append(temp)                       #init_mat: len(seq1)+1 rows and len(seq2)+1 columns whic are 0's

    for j in range(seq2Length+1):
        init_mat[0][j] = gap*j                      #Multiplying 0,1,2... with the gap in order to initialise the matrix 1st row

    for i in range(seq1Length+1):
        init_mat[i][0] = gap*i                      #Multiplying 0,1,2... with the gap penalty in order to initilaise the matrix 1st column

    #Fill matrix
    for i in range(1,seq1Length+1):
        for j in range(1, seq2Length+1):
            if query[i-1] == input[j-1]:
                init_mat[i][j] = max(init_mat[i][j-1]+gap, init_mat[i-1][j]+gap, init_mat[i-1][j-1]+match)
            else:
                init_mat[i][j] = max(init_mat[i][j-1]+gap, init_mat[i-1][j]+gap, init_mat[i-1][j-1]+mismatch)
                
    #Backtracking:
    seq1_align = ""                                 #seq1 is going to be appended to this string
    seq2_align = ""                                 #seq2 is going to be appended to this string

    i = seq1Length                                           #i = seq1Length 
    j = seq2Length                                           #j = seq2Length

    while (i>0 or j>0):

        #Checking if it is a match. If it is a match, then append and jump to the diagonal value directly:
        if query[i-1] == input[j-1]:
            seq1_align += query[i-1]
            seq2_align += input[j-1]
            i -= 1
            j -= 1

        #No match:
        elif query[i-1] != input[j-1]:
            temp_list = [init_mat[i-1][j-1], init_mat[i-1][j], init_mat[i][j-1]]        #Creating a temp_list in order to find the maximum values from top, diagonal and left in order to backtrack

            #If the maximum value is the 0th indexed position, i.e., the diagonal value:
            if max(temp_list) == temp_list[0]:
                seq1_align += query[i-1]
                seq2_align += input[j-1]
                i -= 1
                j -= 1

            #If the maximum value is the 1st indexed position, i.e., the top value:
            elif max(temp_list) == temp_list[1]:
                seq1_align += query[i-1]
                seq2_align += "-"
                i -= 1

            #If the maximum value is the 2nd indexed position, i.e., the left vlaue:
            elif max(temp_list) == temp_list[-1]:
                seq1_align += "-"
                seq2_align += input[j-1]
                j-=1


    seq1_align = seq1_align[::-1]                   #Reverse the string seq1_align
    seq2_align = seq2_align[::-1]                   #Reverse the string seq2_align

    #Storing the match, mismatch and gap symbols in match_string:
    match_string = ""
    for i in range(len(seq1_align)):
        if seq1_align[i] == seq2_align[i]:
            match_string += "|"
        elif seq1_align[i] != seq2_align[i]:
            if (seq1_align[i] == "-" or seq2_align[i] == "-"):
                match_string += " "
            else:
                match_string += "*"

    #Calculating the alignment score:
    alignment_score = 0
    for i in range(len(match_string)):
        if match_string[i] == "|":
            alignment_score += 1
        elif (match_string[i] == "*" or match_string[i] == " "):
            alignment_score += -1
            
               # Normalize the alignment score
    max_length = max(len(seq1_align), len(seq2_align))
    normalized_score = alignment_score / max_length
    
    return(normalized_score)
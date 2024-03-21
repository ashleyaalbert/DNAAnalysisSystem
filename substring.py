def longest_common_substring(string1, string2):
  len1 = len(string1)
  len2 = len(string2)

  # table to store the length of the common substring ending at each position
  substring_table = [[0] * (len2 + 1) for _ in range(len1 + 1)]

  # variables for length and ending index
  max_length = 0
  ending_index = 0

  for i in range(1, len1 + 1):
      for j in range(1, len2 + 1):
          if string1[i - 1] == string2[j - 1]:
              substring_table[i][j] = substring_table[i - 1][j - 1] + 1
              if substring_table[i][j] > max_length:
                  max_length = substring_table[i][j]
                  ending_index = i
          else:
            substring_table[i][j] = 0

  # longest common substring from the ending index and its length
  longest_substring = string1[ending_index - max_length: ending_index]

  return longest_substring
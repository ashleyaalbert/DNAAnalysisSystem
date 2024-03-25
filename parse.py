# function to parse the large dna file
def parse(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        my_dna = {}
        for line in lines:
          if line[0] == '>':
            key = line[1:]
            my_dna[key] = ""
          else:
            my_dna[key] = my_dna[key] + line.strip()

    return my_dna

# function to parse the query dna file
def query_parse(filename):
  with open(filename, 'r') as file:
    lines = file.readlines()
    query_string = ""
    for line in lines:
      query_string += line.strip()

  return query_string
   
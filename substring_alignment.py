from collections import Counter

def get_freqs(seq):
    freqs = Counter(seq)
    return {key: count / len(seq) for key, count in freqs.items()}

def get_substrings(seq, k):
    return set([seq[i:i+k] for i in range(len(seq) - k + 1)])

def sequence_match_score(s, t, k):
    s_substrings = get_substrings(s, k)
    t_substrings = get_substrings(t, k)
    unique = s_substrings | t_substrings
    shared = s_substrings & t_substrings
    return len(shared) / len(unique)

def freqs_similarity(s, t):
    s_freqs = get_freqs(s)
    t_freqs = get_freqs(t)
    sum_freqs = sum([abs(s_freqs[i] - t_freqs[i]) for i in s_freqs])
    return 1 - (sum_freqs / len(s_freqs))

def sub_alignment(s, t):
    return (sequence_match_score(s, t, 9) + freqs_similarity(s, t)) / 2


# Test
# print(sub_alignment('ACGTGGTTCATTGA','ATGCCCGTAATGC'))
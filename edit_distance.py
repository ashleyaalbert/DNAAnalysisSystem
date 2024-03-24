def displayMatrix(m):
    for r in m:
        print(r)

def edit_distance(s, t): # Full recursive soltuion
    if len(t) == 0: return len(s)
    if len(s) == 0: return len(t)
    if s[0] == t[0]: return edit_distance(s[1:], t[1:])
    return 1 + min(edit_distance(s[1:], t),
                   edit_distance(s, t[1:]),
                   edit_distance(s[1:], t[1:]),
                   )

def edit_distance_BU(s, t): # Bottom-up approach
    len_s = len(s)
    len_t = len(t)

    d = [[0]*(len_s+1) for _ in range(len_t+1)]

    for ss in range(len_s+1): d[0][ss] = ss
    for tt in range(len_t+1): d[tt][0] = tt

    for i in range(1,len_t+1):
        for j in range(1,len_s+1):
            d[i][j] = min(d[i-1][j] + 1,
                        d[i][j-1] + 1,
                        d[i-1][j-1] + (0 if s[j-1] == t[i-1] else 1)
                        )
    displayMatrix(d)
    return d[len_t][len_s]

def get_score(s, t):
    edit_dist = edit_distance(s, t)
    if edit_dist == 0: return 1
    return 1 - (edit_dist / max(len(s), len(t)))


# Some tests
print(get_score('ACGTGGTTCATTGA','ATGCCCGTAATGC'))        

print(edit_distance_BU('baseball','football'))
print(edit_distance('baseball','football'))

print(edit_distance_BU('ball','bal'))
print(edit_distance_BU('cars','crs'))
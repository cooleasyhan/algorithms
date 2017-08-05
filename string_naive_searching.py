def search(txt, pat):
    m = len(txt)
    n = len(pat)
    for i in range(m - n + 1):
        for j in range(n):
            if txt[i+j] != pat[j]:
                break
        if j == n -1:
            print('Pattern', pat, 'found at index', i)
    
search('THIS IS A TEST TEXT TEST', 'TEST')
            


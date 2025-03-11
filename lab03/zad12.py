def anagram(s1, s2):
    l1 = sorted(s1)  
    l2 = sorted(s2)
    return l1 == l2

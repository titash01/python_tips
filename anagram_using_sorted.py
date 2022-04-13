def are_anagrams(s1,s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1.lower()) == sorted(s2.lower())


print(are_anagrams('garden','dAnger'))
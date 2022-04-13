# two strings are same if they have same letters.

def are_anagrams(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    freq1 = {}
    freq2 = {}

    for ch in s1.lower():
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1
    
    for ch in s2.lower():
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1

    print(freq1,freq2)

    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
        return True
    

print(are_anagrams("danger","gArden"))
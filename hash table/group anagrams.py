def group_anagrams(li):
    anagram={}
    for string in li:
        s="".join(sorted(string))
        if s in anagram:
            anagram[s].append(string)
        else:
            anagram[s]=[string]
    return list(anagram.values())




print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )
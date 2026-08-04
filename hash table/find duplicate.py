def find_duplicates(list):
    ans=[]
    dict={}
    for i in list:
        if i in dict:
            ans.append(i)
            continue
        else:
            dict[i]=True
    return ans


print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
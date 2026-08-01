#find the frequency of each character in the string
def char_frequency(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

print(char_frequency("aabbbccdddddeeeefffff"))
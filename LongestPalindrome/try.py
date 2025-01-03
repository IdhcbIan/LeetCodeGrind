s = "o"


def logestPalindrome(s):
    best = ""
    for i in range(0, len(s)):
        for ii in range(0, len(s)+1):
            #print(s[i:ii])

            slice = s[i:ii]

            if slice == slice[::-1] and len(slice)>len(best):
                best = slice
    
    return best

print(logestPalindrome(s))

#++++++++++++++++++++++++++++++++++
# sabpii
# Wasam
#++++++++++++++++++++++++++++++++++

def uniqueMorseRepresentations(words):
    def rd(l):
        ans = []
        for elem in range(len(l)):
            if l[elem] not in l[elem+1:]:
                ans.append(l[elem])
        return ans    
    dictionary = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 
                  'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 
                  'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
                  'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 
                  'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 
                  'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
                  'y': '-.--', 'z': '--..'}
    ans = []
    for elem in words:
        s = ""
        for elem2 in elem:
            s += dictionary[elem2]
        ans.append(s)
    ans = rd(ans)
    return len(ans)


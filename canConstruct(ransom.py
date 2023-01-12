#=============================
# 1stbavb

# By Wasam
#=============================

def canConstruct(ransomNote, magazine):
    magazine = list(magazine)
    magazine.sort()
    ransomNote = list(ransomNote)
    ransomNote.sort()
    final_copy = [elem for elem in ransomNote]
    tracker = ""
    ans = []
    while ransomNote!=[]:
        tracker = ransomNote[0]
        if tracker in magazine:
            del ransomNote[0]
            del magazine[magazine.index(tracker)]
            ans.append(tracker)
        else:
            break
    print(ans, final_copy, magazine)
    
    if ans == final_copy: return True
    return False    
        
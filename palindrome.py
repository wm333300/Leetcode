#=============================
# Palindrome
# By Wasam
#=============================


def pal(s):
    def str_clean(st):
        check_str = "abcdefghijklmnopqrstuvwxyz"
        ans = ""
        for elem in  st.lower():
            if elem in check_str:
                ans += elem
        return ans
    
    main_s = ""
    comp_s = ""
    clean_str = str_clean(s)
    half_len = len(clean_str) // 2
    
    if (len(clean_str) == 1): return False
    
    if (len(clean_str) % 2 == 0): 
        main_s = clean_str[:half_len]
        comp_s = list(clean_str[half_len:])
        
    if (len(clean_str) % 2 == 1):
        main_s = clean_str[:half_len]
        comp_s = list(clean_str[half_len + 1:])
        
    comp_s.reverse()
    comp_s = "".join(comp_s)
    
    return (main_s == comp_s)

def pal_efficient(s):
    check_dict = {"a","b","c","d","e","f","g","h","i","j"
                  ,"k","l","m","n","o","p","q","r","s","t"
                  ,"u","v","w","x","y","z","0","1","2","3"
                  ,"4","5","6","7","8","9"}
    lower_str = s.lower()
    cleaned_str = [elem for elem in lower_str if elem in check_dict]
    cl_length = len(cleaned_str)
    main_s = list(cleaned_str[:cl_length//2])
    comp_s = []
    if (cl_length % 2 == 0): comp_s = list(cleaned_str[cl_length//2:])
    if (cl_length % 2 == 1): comp_s = list(cleaned_str[(cl_length//2)+1:])
    comp_s.reverse()
    return (comp_s == main_s)
    


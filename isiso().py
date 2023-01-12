#=============================
# isIsomorphic(self, s, t)
# By Wasam
#=============================
    
def isIsomorphic(s, t):
    def gen_index_stack(st):
        stack = []
        str_lst = list(st)
        for elem in str_lst:
            if elem not in stack:
                stack.append(elem)
        return stack
    
    def gen_index_lst(stri, stk):
        answer = []
        for elem in stri:
            answer.append(stk.index(elem))
        return answer    
    index_stk_s = gen_index_stack(s)
    index_stk_t = gen_index_stack(t)
    index_lst_s = gen_index_lst(s, index_stk_s)
    index_lst_t = gen_index_lst(t, index_stk_t)
    return (index_lst_s == index_lst_t)
        
        
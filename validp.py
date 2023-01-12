#=============================
# Valid Parentheses
# By Wasam
#=============================

def valid_parentheses(s):
    
    check = False
    open_curr = ""
    close_curr = ""
    open_str = "([{"
    cl_str = ")]}"
    open_list = []
    cl_list = []
    
    ind = 0
    while (ind < len(s)):
        if ((open_curr == "") and (close_curr != "")):
            check = False
        elif ((open_curr != close_curr) and (close_curr != "")):
            check = False
        elif (open_curr == close_curr):
            check = True
            ind += 1 
        elif (s[ind] in open_str):
            open_curr = s[ind]
            open_list.append(open_curr)
            ind += 1
        elif (s[ind] in cl_str):
            close_curr = s[ind]
            cl_list.append(open_curr)
            ind += 1
        else:
            check = True
    return check
            
    
    
    
def p(s):
    
    op_stack = []
    code_dict = {"(" : ")",
                 "[" : "]",
                 "{" : "}"}
    for elem in s:
       
        if elem in list(code_dict.keys()):
            op_stack.append(elem)
        elif ((len(op_stack) < 1) and (elem in list(code_dict.values()))):
            return False
        elif (elem == code_dict[op_stack[-1]]):
            del op_stack[-1]
        else: 
            return False
    if (op_stack != []):
        return False
    else:
        return True
    
tests = ["()",
         "()[]{}",
         "(]",
         "(())",
         "))))",
         "([])",
         "([)]",
         "((((",
         ")(",
         "[([]])"]
   
checks = []
for elem in tests:
    checks.append(p(elem))
print(checks)

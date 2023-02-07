# Wasam Hexadecimal

def toHex(num):
    answer = ""
    if num < 0: 
        num += 4294967296
    while num > 0:
        adder = num%16
        if adder >= 10:
            answer += "abcdef"[adder-10]
        else:
            answer += str(adder)
        num //= 16
    answer = "".join(list(answer)[::-1])
    
    return answer
    
        
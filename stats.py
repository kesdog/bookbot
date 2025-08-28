# methods for book project

def word_count(text):
    arr= text.split()
    return len(arr)

def char_count(text):
    out={}
    for c in text:
        char=c.lower()
        if(char in out):
            out[char]=out[char]+1
        else:
            #print(f"new char found {char}")
            out[char]=1
    return out

def report(char_list):
    out=[]
    
    for p in char_list:
        out.append({"char": f"{p}" ,"num":char_list[p]})
    
    out.sort(reverse=True,key=sort_on)
    #print(out)
    return out
def sort_on(chars):
    return chars["num"]


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
            print(f"new char found {char}")
            out[char]=1
    return out


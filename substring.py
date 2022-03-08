def count_substring(string, sub_string):
    l2=[]
    length=len(string)
    index=0
    while index<length:
        i=string.find(sub_string,index)
        if i==-1:
            return len(l2)
        l2.append(i)
        index=i+1
    return len(l2)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

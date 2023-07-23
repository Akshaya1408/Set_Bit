def set_bit(num, bit):
    res=0  
    res|=(1<<num)
    res|=(1<<bit)
    return res

num=int(input())
bit=int(input())
print(set_bit(num,bit))
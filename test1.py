def padding(s,length,char=''):
    if len(s)>=length:
        return s
    else:
        str_padding=length-len(s)
        return s+(char *str_padding)
print(padding('hello',6,'&'))
print(padding('worldwide',8,'*'))
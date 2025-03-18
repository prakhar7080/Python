def convert(str1):
    if str1[:2] == "12" and str1[-2:] == "AM":
        return "00"+str1[2:-2]
    elif str1[:2] == "12" and str1[-2:] == "PM":
        return str1[:-2]
    elif str1[-2:] == "AM":
        return str1[:-2]
    else:
        return str(int(str1[:2])+12)+ str1[2:-2]
print(convert("01:59:55 PM"))
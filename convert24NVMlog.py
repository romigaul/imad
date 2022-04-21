#DATE   : 5/4/2022
#AUTHOR : imadumuh


import re 
 
a_file = open("24jamrandomservices.pcom")
# a_file = open("data.txt")
lines = a_file.readlines()
a_file.close()

def listToString(s): 
    # initialize an empty string
    str1 = "" 
    
    # return string  
    return (str1.join(s))

f = open("hasil.pcom", "w")
for line in lines:
    
    data = re.findall('(?<=\[).+?(?=\])', line)
    datastring = listToString(data)
    
    #convert line into string
    linestring = listToString(line).strip()
    # print(linestring[:4])
    linewithbracket = line.replace(datastring,'')
    linewithoutdata = linewithbracket.replace('[]','')
    
    # print(linewithoutdata.strip())
    
    
    if not data: #check if res returned empty list
        f.write(linestring+'\n')
    elif linestring[:4] != '00A4':
        f.write(linestring+'\n')
    elif linestring[:4] == '00A4':
        # print('00C00000 W(2:2)'+'['+datastring+']'+' (9000)') #print data after convert list to string
        f.write(linewithoutdata.strip()+'\n')
        f.write('00C00000 W(2:2) '+'['+datastring+']'+' (9000,91XX)'+'\n')
    else:
        f.write(linestring+'\n')
f.close()
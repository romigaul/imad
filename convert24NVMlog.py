#DATE   : 5/4/2022
#AUTHOR : imadumuh
import re 
from tkinter import *
from tkinter import filedialog


filepath = filedialog.askopenfilename(title="Open File Input")
inputfile = open(filepath, 'r')
# inputfile = open("data.txt")
lines = inputfile.readlines()
inputfile.close()

def listToString(list_value): 
    # initialize an empty string
    str1 = "" 
    
    # return string  
    return (str1.join(list_value))


# outputFile = open("hasil.pcom", "w")
outputFile = filedialog.asksaveasfile(title="savefile", defaultextension='.pcom') #pop up save dialog box

for line in lines:
    #regex finding data between squarebracket []
    data = re.findall('(?<=\[).+?(?=\])', line)
    datastring = listToString(data)
    
    #convert line into string
    linestring = listToString(line).strip()
    # print(linestring[:4])
    linewithbracket = line.replace(datastring,'')
    linewithoutdata = linewithbracket.replace('[]','')
    
    # print(linewithoutdata.strip())
    
    
    if not data: #check if res returned empty list
        outputFile.write(linestring+'\n')
    elif linestring[:4] != '00A4':
        outputFile.write(linestring+'\n')
    elif linestring[:4] == '00A4':
        # print('00C00000 W(2:2)'+'['+datastring+']'+' (9000)') #print data after convert list to string
        outputFile.write(linewithoutdata.strip()+'\n')
        outputFile.write('00C00000 W(2:2) '+'['+datastring+']'+' (9000,91XX)'+'\n')
    else:
        outputFile.write(linestring+'\n')
outputFile.close()
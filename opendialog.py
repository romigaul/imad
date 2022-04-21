#DATE   : 21/4/2022
#AUTHOR : imadumuh

import re 
from tkinter import filedialog

filepath = filedialog.askopenfilename(title="Open File Input")
file = open(filepath, 'r')
print(file.read())
file.close()

fileOutput = filedialog.asksaveasfile(defaultextension='.pcom')
fileOutput.write()
fileOutput.close()


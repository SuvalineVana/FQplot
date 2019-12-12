import sys
import os
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
fileRaw = sys.argv[1]
fileName = str(fileRaw)


Qscore_dict = {'!':0, '"':1, '#':2, '$':3, '%':4, '&':5, "'":6, '(':7, ')':8, '*':9, '+':10, ',':11, '-':12, '.':13, '/':14, '0':15, '1':16, '2':17, '3':18, '4':19, '5':20, '6':21, '7':22, '8':23, '9':24, ':':25, ';':26, '<':27, '=':28, '>':29, '?':30, '@':31, 'A':32, 'B':33, 'C':34, 'D':35, 'E':36, 'F':37, 'G':38, 'H':39, 'I':40}

lugemite_Qskoorid = []
with open(fileName) as f:
    lines = f.read().splitlines()
    desired_lines = lines[3::4]

for i in desired_lines:
    pikkus = list(range(1, len(i)+1))
    kvaliteet = []
    for j in i:
        kvaliteet.append(Qscore_dict[j])
    plt.plot(pikkus, kvaliteet)
    
plt.xlabel('aluspaar')
plt.ylabel('Kvaliteedi skoor')
plt.title("DNA kvaliteedi graafik")
#plt.legend()
strFile = "test.png"
if os.path.isfile(strFile):
   os.remove(strFile)   # Opt.: os.system("rm "+strFile)
plt.savefig(strFile , transparent=True)
sys.stdout.flush()
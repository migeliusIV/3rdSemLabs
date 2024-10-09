import math
import csv

def plotter(arr_x, arr_y):
    pass

path = "C:/Users/Migel/Desktop/E-81_3.csv"
array_f = []
array_Uc = []
array_w = []
array_Ucm = []

with open(path, newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=';', quotechar=' ')
    for i, row in enumerate(data):
        if i:
            array_f.append(int(row[0]))
            array_Uc.append(row[1])
            array_w.append(2 * 3.14 * int(row[0]))
            array_Ucm.append(float(row[1].replace(",", ".")) * ((2)**(1/2)))
            
            res = []
            res.append(str(array_f[i - 1]))
            res.append(str(array_w[i - 1]))
            res.append(str(array_Uc[i - 1]))
            res.append(str(array_Ucm[i - 1]))
            print(' '.join(res))
        else:
            pass
            #labeling
    
#arrar_f = []
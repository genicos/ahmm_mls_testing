import sys

from os import listdir
from os.path import isfile, join

output_dir = "outputs"

OUTfiles = [f for f in listdir(output_dir) if isfile(join(output_dir, f)) and f[0] == 'O']

total_lnl = 0
total_site_dist = 0
total_fit_dist = 0

for f in OUTfiles:
    OUT = open(output_dir+"/"+f,"r").readlines()
    for i in range(len(OUT)):
        line = OUT[i]
        if line[0] == 'U':
            lnl = float(line.split('\t')[-1])
            total_lnl += lnl
            
        if line[0] == 's':
            site = float(line.split('\t')[1])
            total_site_dist += abs(0.2 - site)
            
            fit1 = float(line.split(',')[0].split('\t')[-1])
            total_fit_dist += abs(1 - fit1)
            fit2 = float(line.split(',')[2].split(' ')[0])
            total_fit_dist += abs(0.98 - fit2)


total_lnl /= 48
total_site_dist /= 48
total_fit_dist /= 48

print(total_lnl)
print(total_site_dist)
print(total_fit_dist)


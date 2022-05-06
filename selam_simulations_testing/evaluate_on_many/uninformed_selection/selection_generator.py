import sys
import subprocess
from math import floor
from random import random
from time import sleep

print("Generating population conditions")

condition = int(sys.argv[1])


strength_range = 0.03
max_sites = 3

prop =        0.2
generations = "500"


selection = open("src/selections/selection"+str(condition), "w")
selections = ""



site_count = floor(random()*max_sites) + 1


for i in range(site_count):
    selection.write("S\tA\t0\t")

    a = 1 + strength_range * (random()*2 - 1)
    b = 1
    c = 1 + strength_range * (random()*2 - 1)
    
    max_val = max(a,b,c)

    site = str(random()*0.427)
    a = str(a/max_val)
    b = str(b/max_val)
    c = str(c/max_val)
        
    selection.write(site + "\t" + a + "\t" + b + "\t" + c + "\n")
    selections += site + "\t" + a + "\t" + b + "\t" + c + "\n"


selection.close()

# generate output files

output_string = generations+"\t0\t100\t0\tselam_outputs/selam_output"+str(condition)+"\n"
output = open("src/outputs/output"+str(condition), "w")

output.write(output_string)
output.close()


#generate demography file
demo = open("src/demographies/demography"+str(condition), "w")
demo.write("pop1\tpop2\tsex\t0\t1\n")
demo.write("0\t0\tA\t10000\t10000\n")
demo.write("0\ta0\tA\t"+str(prop)+"\t0\n")
demo.write("0\ta1\tA\t"+str(1-prop)+"\t0\n")
demo.close()

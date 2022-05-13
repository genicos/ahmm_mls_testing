import sys
import subprocess
from math import floor
from random import random
from time import sleep

print("Generating population conditions")

condition = int(sys.argv[1])


strength =    [.005, .01, .02, .05][condition % 4]
prop =        [.05,.1,.2,.5][(condition % 16)//4]
generations = ["100","200","500"][condition//16]


selection = open("src/selections/selection"+str(condition), "w")
selections = ""

selection.write("S\tA\t0\t")

a = 1
b = 1
c = 1 - strength

site = str(random()*0.427)
site = str(0.2)
a = str(a)
b = str(b)
c = str(c)
        
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

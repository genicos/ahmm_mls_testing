import sys

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

if len(sys.argv) < 3 or not isfloat(sys.argv[1]) or not sys.argv[2].isdigit():
    print("arguments required: <m>:float <t>:int")
    print("optional additional: <n>:int")

m = float(sys.argv[1])
if m < 0 or m > 1:
    print("m must be in range [0,1]")
t = int(sys.argv[2])
if t < 0:
    print("t must be positive")

n = 10000
if(len(sys.argv) > 3):
    n = int(sys.argv[3])


demography_file = open("panel_generation/demography", "w")
demography_file.write("pop1\tpop2\tsex\t0\t1\n")
demography_file.write("0\t0\tA\t"+str(n)+"\t"+str(n)+"\n")
demography_file.write("0\ta0\tA\t"+str(m)+"\t0\n")
demography_file.write("0\ta1\tA\t"+str(1-m)+"\t0\n")

output_file = open("panel_generation/output_file", "w")
output_file.write(str(t)+"\t0\t100\t0\tselam_output\n")

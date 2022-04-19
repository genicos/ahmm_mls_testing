import sys

output = open("OUT","r").readlines()
model_file = open("model_file", "r").readlines()

grid_file = open("grid_file", "w")

for i in range(len(output)):
    model = model_file[i*2][:-1]

    grid_file.write(model + "\t" + output[i])




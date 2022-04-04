import sys

if(len(sys.argv) < 5):
    print("ERROR: you must enter a model that the grid will center upon")
    print("parameters: <site_location> <fit coeff0> <fit coeff1> <fit coeff2>")

site = float(sys.argv[1])
fit0 = float(sys.argv[2])
fit1 = float(sys.argv[3])
fit2 = float(sys.argv[4])

grid_width = 0.02
grid_x_tick = 0.001
grid_height = 0.02
grid_y_tick = 0.001


model_file = open("model_file", "w")

x = site - grid_width/2
y1 = fit0 - grid_height/2
y2 = fit2 - grid_height/2

while (x < site + grid_width/2):
    
    y1 = fit0 - grid_height/2
    
    while(y1 < fit0 + grid_height/2):
        
        y2 = fit2 - grid_height/2

        while(y2 < fit2 + grid_height/2):

            model_file.write(str(x)+"\t"+str(y1)+"\t"+str(fit1)+"\t"+str(y2)+"\n\n");

            y2 += grid_y_tick
        y1 += grid_y_tick
    x += grid_x_tick

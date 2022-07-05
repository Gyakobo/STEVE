import h5py
import numpy as np
import pygame
import matplotlib.pyplot as plt

pygame.init() # Initialize Pygame


width   = 1300
height  = 1000

surface = pygame.display.set_mode((width, height))
gray = pygame.Color('gray15')


def map(x,in_min,in_max, out_min, out_max):
  return ((x - in_min) * (out_max - out_min) * 1.0) / (in_max - in_min) + out_min * 1.0

# Big, Small

color_range = {
    0: (np.matrix([137, 0, 0]),      np.matrix([217, 0, 0])), 
    1: (np.matrix([248, 0, 0]),      np.matrix([255, 83, 0])), 
    2: (np.matrix([255, 95, 0]),     np.matrix([240, 173, 0])),
    3: (np.matrix([255, 197, 0]),    np.matrix([223, 255, 29])),
    4: (np.matrix([190, 230, 38]),   np.matrix([190, 230, 38])),
    5: (np.matrix([110, 255, 143]),  np.matrix([21, 255, 231])),
    6: (np.matrix([7, 219, 210]),    np.matrix([0, 178, 255])),
    7: (np.matrix([0, 161, 255]),    np.matrix([0, 77, 255])),
    8: (np.matrix([0, 60, 255]),     np.matrix([0, 0, 236])),
    9: (np.matrix([0, 0, 219]),      np.matrix([0, 0, 105])) 
}

def return_tuple(array):
    return (array.item(0), array.item(1), array.item(2))

def color_length(index):
    return np.matrix([  color_range[index][0].item(0) - color_range[index][1].item(0), 
                        color_range[index][0].item(1) - color_range[index][1].item(1), 
                        color_range[index][0].item(2) - color_range[index][1].item(2) ])

def perc(t1, t2):
    return ((t2 - t1)*1.0) / (t2*1.0)

# color_range[0][0] - color_range[0][1] 
def color(range):
    if range > 1300:
        return return_tuple(color_range[0][0])
    elif (range <= 1300 and range > 1240):
        return return_tuple(color_range[0][1] + color_length(0) * map(range, 1240.0, 1300.0, 0.0, 1.0))
    elif (range <= 1240 and range > 1180):
        return return_tuple(color_range[1][1] + color_length(1) * map(range, 1180.0, 1240.0, 0.0, 1.0)) 
    elif (range <= 1180 and range > 1120):
        return return_tuple(color_range[2][1] + color_length(2) * map(range, 1120.0, 1180.0, 0.0, 1.0)) 
    elif (range <= 1120 and range > 1060):
        return return_tuple(color_range[3][1] + color_length(3) * map(range, 1060.0, 1120.0, 0.0, 1.0)) 
    elif (range <= 1060 and range > 1000):
        return return_tuple(color_range[4][1] + color_length(4) * map(range, 1000.0, 1060.0, 0.0, 1.0)) 
    elif (range <= 1000 and range > 940):
        return return_tuple(color_range[5][1] + color_length(5) * map(range, 940.0, 1000.0, 0.0, 1.0)) 
    elif (range <= 940 and range > 880):
        return return_tuple(color_range[6][1] + color_length(6) * map(range, 880.0, 940.0, 0.0, 1.0)) 
    elif (range <= 880 and range > 820):
        return return_tuple(color_range[7][1] + color_length(7) * map(range, 820.0, 880.0, 0.0, 1.0)) 
    elif (range <= 820 and range > 760):
        return return_tuple(color_range[8][1] + color_length(8) * map(range, 760.0, 820.0, 0.0, 1.0)) 
    elif (range <= 760 and range > 700):
        return return_tuple(color_range[9][1] + color_length(9) * map(range, 700.0, 760.0, 0.0, 1.0)) 

    return return_tuple(color_range[9][1])


file_name = "data.hdf5"

flag = True

# Code reference to draw a rectangle
# pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(30, 30, 60, 60))

start = 33269
stop =  start + 16

drawn = True

with h5py.File(file_name, 'r') as file:
    keys = list(file.keys())
    
    # List keys
    print("Keys: %s" % keys)
    
    data = file.get('Data').get('Table Layout')
    dataset1 = np.array(data)
    #print(dataset1)

    displace_down = 0
    displace_right = 0

    y_axis = []
    x_axis = []

    minute = 0

    increment = start


    while flag:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    flag = False
        
        if drawn:
            for j in range(0, 5 * 24):        
                for i in range(start, stop+1):
                    
                    pygame.draw.rect(surface, color(dataset1[increment][21]), pygame.Rect(displace_right, displace_down, 4 + displace_right, 17 + displace_down))
                    x_axis.append(minute)
                    y_axis.append(dataset1[increment][21])
                    minute += 15
                    displace_down += 17
                    
                    if i == stop:
                        displace_down = 0 

                    increment += 1

                displace_right += 4 
                    
                if j == 4:
                    displace_right = 0 

            pygame.display.flip()
            
            drawn = False
            
    plt.plot(x_axis, y_axis)
    plt.xlabel('Time in 15 minute intervals')
    plt.ylabel('Ion Temperature')    
    plt.show() 
        
            


'''
0) 1300 - 1240
#890000 - #d90000
(137, 0, 0) - (217, 0, 0)


1) 1240 - 1180
#f80000 - #ff5300
(248, 0, 0) - (255, 83, 0)


2) 1180 - 1120
#ff5f00 - #f0ad00
(255, 95, 0) - (240, 173, 0)


3) 1120 - 1060
#ffc500 - #dfff1d
(255, 197, 0) - (223, 255, 29)


4) 1060 - 1000
#bee626 - #7aff82
(190, 230, 38) - (190, 230, 38)


5) 1000 - 940
#6eff8f - #15ffe7
(110, 255, 143) - (21, 255, 231)


6) 940 - 880
#07dbd2 - #00b2ff
(7, 219, 210) - (0, 178, 255)


7) 880 - 820
#00a1ff - #004dff
(0, 161, 255) - (0, 77, 255)


8) 820 - 760
#003cff - #0000ec
(0, 60, 255) - (0, 0, 236)


9) 760 - 700
#0000db - #000069
(0, 0, 219) - (0, 0, 105)

'''


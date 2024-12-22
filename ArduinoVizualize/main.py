import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from source.vizual import serial_reading
from functools import partial

def serial_animating(subplot_1, data_list, serial_com, frame):
    data_list.append(serial_reading(serial_com))
    # data prepearing
    data_list.append([0.5]*10)
    data_list = data_list[-50:]
    # window prepearing
    subplot_1.plot(data_list)
    subplot_1.set_ylim([0, 1000])
    subplot_1.set_title("Robot 5")
    subplot_1.set_ylabel("Value")
    subplot_1.set_xlabel("Last 50-y packages")
    
def main():
    # data prepearing
    data_list = []
    serial_com = serial.Serial("COM13", 9600)
    # print(serial_com)             
    # main window prepearing
    fig = plt.figure()
    subplot_1 = fig.add_subplot(111)
    # microcontroller's reboot
    serial_com.setDTR(False)
    time.sleep(1)
    serial_com.flushInput()
    serial_com.setDTR(True)
    # vizualization
    ainm_res = animation.FuncAnimation(fig, 
                            func = partial(serial_animating, 
                                           subplot_1, 
                                           data_list, 
                                           serial_com),
                            frames = 100, 
                            interval = 300) 
    plt.show()
    # turn off
    serial_com.close()  

if __name__ == "__main__":
    main()


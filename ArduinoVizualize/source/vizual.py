import serial

def serial_reading(serial_com):
    # print(serial_com)
    data_undecoded = serial_com.readline()
    data_string = data_undecoded.decode("utf-8").strip('\r\n')
    
    try:
        data_float = float(data_string)
        return data_float     
    except:                            
        print("Error. String is not float-type.")  
        pass

import serial
ser = serial.Serial("/dev/ttyACM0",9600) # Connect to the Arduino


class listes(object):
    
    def make(self, lmax, char, liste):
      
        if len(liste) != lmax:
        
            ser.write(char)
            val = int(ser.readline())
            liste.append(val)
            
        else:
        
            del liste[:]
            ser.write(char)
            val = int(ser.readline())
            liste.append(val)
        
        return liste

class getval(object):
    
    def intval(self, char):
        
        ser.write(char)
        val = int(ser.readline())
        
        return val
    
    def strval(self, char):
        
        ser.write(char)
        val = ser.readline()
                
        return val
    
    def testco(self, char):
    
        ser.write(char)
        val = ser.readline()
        
        return val


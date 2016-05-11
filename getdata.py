import serial
ser = serial.Serial("/dev/ttyACM0",9600) # Connect to the Arduino


class listes(object):
    
    def make(self, lmax, char, liste): 
        """Takes the folliwing parametres and appends taken values to the list:
            lmax: max list lenth
            char: must be equal to the IF-'CHAR' on Arduino, CHAR been a letter from A to Z
            liste: predefined global list on main.py
        """
      
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


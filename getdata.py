import serial
ser = serial.Serial("/dev/ttyACM0",9600) # Connect to the Arduino



class listes(object):
    
    def make(self, lmax, char, typ, liste):
        """ Creates a list with the following parameters:
            lmax: Set max list lenght
            char: "Calls" the Arduino code that is set to the same character. Can only use characters from A to Z
            typ: 1 for int, 2 for float
            liste: Given list name       
        """
        if len(liste) != lmax:
        
            ser.write(char)
            
            if int == 1:
            
                val = int(ser.readline())
                liste.append(typ)
                
            else:
            
                val = ser.readline()
                liste.append(typ)
                
        else:
        
            del liste[:]
            ser.write(char)
            val = int(ser.readline())
            liste.append(typ)
        
        return liste

class getval(object):
    
    def intval(self, char):
    """ Get Arduino int value with following parameters
        char: "Calls" the Arduino code that is set to the same character. Can only use characters from A to Z
    
    """
        ser.write(char)
        val = int(ser.readline())
        
        return val
    
    def strval(self, char):
     """ Get Arduino str value with following parameters
        char: "Calls" the Arduino code that is set to the same character. Can only use characters from A to Z
    
    """
        ser.write(char)
        val = ser.readline()
                
        return val
    
    def testco(self, char):
     """ Test connection to the Arduino with following parameters
        char: "Calls" the Arduino code that is set to the same character. Can only use characters from A to Z. Preferably use char = 'A' !!
    
    """
        ser.write(char)
        val = ser.readline()
        
        return val


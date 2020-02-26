


# returns the sun sign of the given birthdate
def getSunsign(day,month):
    if month==1:
        if day > 20:
            return 'Aquarius'
        else:
            return 'Capricorn'
    if month==2:
        if day > 21:
            return 'Pisces' 
        else: return 'Aquarius'
    if month==3:
        if day > 21:
            return 'Aries'
        else: return 'Pisces'
    if month==4:
        if day > 21:
            return 'Taurus'
        else: return 'Aries'
    if month==5:
        if day > 21:
            return 'Gemini'
        else: return 'Taurus'
    if month==6:
        if day > 21:
            return 'Cancer'
        else: return 'Gemini'
    if month==7:
        if day > 21:
            return 'Leo'
        else: return 'Cancer'
    if month==8:
        if day > 21:
            return 'Virgo'
        else: return 'Leo'
    if month==9:
        if day > 21:
            return 'Libra'
        else: return 'Virgo'
    if month==10:
        if day > 21:
            return 'Scorpio'
        else: return 'Libra'
    if month==11:
        if day > 21:
            return 'Sagittarius'
        else: return 'Scorpio'
    if month==12:
        if day > 21:
            return 'Capricorn'
        else: return 'Sagittarius'
            
        
    
    
    
if __name__=="__main__":
    
    
 
    yourSign = getSunsign(10,7)
    mySign = getSunsign(5,9)
    momSign = getSunsign(7,10)
    
sunSign=[yourSign,mySign,momSign]
    

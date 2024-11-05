# A simple calculator app

class Calculator:

    def add( x, y ):
        return (x+y)
    
    def sub( x, y ):
        return (x-y)
    
    def mul( x, y ):
        return (x*y)
    
    def div( x, y ):
        #Infinite check
        if (y == 0):
            return 0
        return (x/y)
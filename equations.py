def exponent (numX):
    answer=1
    x=numX
    denom=1
    denomAdd=1
    for i in range(1,1000):
        answer+=x/denom
        x*=numX
        denomAdd+=1
        denom*=denomAdd
    return (answer)
	
def Ln(x:float)-> float:
    if x<=0:
        return float(0)
    else:
        YN=0
        result =x-1.0
        while((YN-result)>0.001 or (result-YN)>0.001):
            YN =result
            result = result + 2*((x-exponent(result))/(x+exponent(result)))
        return float(result)

def factorial(N): 
    F=1
    if N==0:  
        return 1
    elif N>0:
        for T in range(1, N+1):
            F=F*T
        return F

def XtimesY(x:float,y:float)-> float:
    try:    
        if(x>0):
            final=exponent(Ln(x)*y)
            return float('%0.6f' % final)
        else:
            return float(0)
    except:
        return float(0)
        
def sqrt(x:float,y:float)-> float:
    try:    
        if( x!=0 and y>0 ):
            x= 1/x
            final= XtimesY(y,x)
            return float('%0.6f' % final)
        elif( x==0 ):
            return float(0)
        else:
            return float(0)
    except:
        return float(0)
        
def calculate(x:float) -> float:
    try:
        finResult= exponent(x)XtimesY(7,x)(1/x)*sqrt(x,x)
        finResult=float('%0.6f' % finResult)
        return finResult
    except:
        return float(0)
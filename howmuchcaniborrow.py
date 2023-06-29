"""
Pmt = r * PV/(1-(1+r)0**-n)
Pmt is how much you pay back/mon is number of months
r is interest rate per month
n is number of months

"""

def computesPmt(PV, r, n):
    r/=100 # convert APR to a decimal
    r = r/12

    Pmt = r * PV/(1-(1+r)**-n)
    return Pmt

"""
Parameters
----------
PV : TYPE
DESCRIPTION.
r : TYPE
DESCRIPTION.
n : TYPE
DESCRIPTION.

Returns
-------
Pmt : TYPE float
DESCRIPTION. amt paid per month

"""
def computesPV(Pmt, r, n):
    r/=100 # convert APR to a decimal
    r = r/12
    PV = (1-(1+r)**(-n)) *Pmt/r
    return PV    
"""

    Parameters
    ----------
    Pmt : TYPE float
        DESCRIPTION. how much I can afford for monthly payment
    r : TYPE float
        DESCRIPTION. Interest rate APR
    n : TYPE integer
        DESCRIPTION. number of month

    Returns
    -------
    PV: TYPE float
        DESCRIPTION. amount of $$ I can afford to borrow
        
    formula:
    PV = (1-(1+r)**(-n) *Pmt/r

    """
  

# input the PV
import numpy as np

while(True):
    choice = int(input('enter choice 1 for PV, 2 for Pmt -> '))
    if (choice ==1 or choice ==2):
        break
    else:
        print(f"enter a 1 or a 2, you entered {choice}")


if choice == 1:    
    Pmt = input('enter Pmt:')
    Pmt = float(Pmt)
    # equivalently PV = float(input('enter PV: '))
    print(f"Pmt ={Pmt} \n")
    
    r = input("interest APR:")
    r = float(r)
    print(f"interest = {r: 0.3f} \n")
    
    n = int(input('how many months: '))
    print(f"n = {n} months \n")
    
    PV = computesPV(Pmt, r, n)
    PV = np.round(PV, 2)
    print(f"PV is ${PV: 0.2f}")
    
if choice == 2:
    
  PV = input('enter PV:')
  PV = float(PV)
  # equivalently Pmt = float(input('enter Pmt: '))
  print(f"PV ={PV} \n")
  
  r = input("interest APR:")
  r = float(r)
  
  print(f"interest = {r: 0.3f} \n")
  
  n = int(input('how many months: '))
  print(f"\nn = {n} months \n")
  
  Pmt = computesPmt(PV, r, n)
  Pmt = np.round(Pmt, 1)
  print(f"amount I can borrow is ${Pmt: 0.2f} per month")
   
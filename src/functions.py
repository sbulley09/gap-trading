# The defineGap function classifies a time period as either up or down gap or neither
#
# float lowT0 - the lowest value of the previous time period
# float highT0 - the highest value of the previous time period
# float tOpen - the opening value of the current time period
#
# returns a 1 for up-gap, -1 for down-gap, and 0 for neither
#

def defineGap(lowT0, highT0, t1Open):
  # Up Gap: open of T(1) > High of T(0)
  # Down Gap: open of T(1) < Low of T(0)
    if t1Open > highT0:
        return (1)
    elif t1Open < lowT0: 
        return (-1)
    else 

  
  return 0


# float previousExtreme - the high or low of the previous time period
# float currentOpen - the current opening value of the time period
#
# returns the gap percentage (open / extreme) - 1
def calculateGapSize(previousExtreme, currentOpen):
  return (currentOpen  / previousExtreme) - 1

# float closingValue - Value at which the gap will be considered closed
# float currentExtreme - Highest or Lowest value of the current time period
#
# returns true if the gap has closed, false if it remains open
def gapClosed(closingValue, currentExtreme):
  return false




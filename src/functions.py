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
  return 0


# float previousExtreme - the high or low of the previous time period
# float currentOpen - the current opening value of the time period
#
# returns the gap percentage (open / extreme) - 1
def calculateGapSize(previousExtreme, currentOpen):
  return (currentOpen  / previousExtreme) - 1

# float valueToClose - Value at which the gap will be considered closed
# float currentMin - Lowest value of the current time period
# float currentMax - Highest value of the current time period
# integer gapType - 1 if an up-gap, -1 if a down-gap
#
# returns true if the gap has closed, false if it remains open
def gapClosed(valueToClose, currentMin, currentMax, gapType):
  return false

# Array[Dictionary] inputData - Array of time periods of stock data
#   each Dictionary contains keys [open, low, high]
#
# returns outputData - information regarding gaps that closed and those that didn't
def process(inputData):
  # store first element of inputData in variable (Use as "previousPeriod")
  # for each time period in the inputData (start from second variable)
    # Check if there's a gap
    # If there is a gap
      # Add an object to a list of gaps to monitor
      # object should contain:
        # Time Period of gap (use the current index of the for-loop)
        # Gap Size


    # for each gap that we are monitoring
      # Check if it closes with this current time period's data
      # if it closes
        # calculate the number of periods to close
        # add object to "closed gaps" list (containing gapSize and periodsToClose)
        # remove the object from the list of gaps we are monitoring

    # Set "previousPeriod" = "currentPeriod"




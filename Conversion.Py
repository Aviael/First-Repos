def conversion():
    distance = input('How many miles do you drive? ')
    distance2 = float(distance)
    finalDistance = (distance2*1.609344)
    finalDistance2 = str(finalDistance)
    print(''+distance+' miles is equivalent to '+finalDistance2+' kilometers.')

try:
    conversion()
except:
    print("An error has occured. Please try again.")

    
input("Press enter to exit...")

oldTemp=1
oldHeart=2
oldBreath=3

while True:
    newTemp = int(raw_input("Temp: "))
    newHeart =  int(raw_input("Heart: "))
    newBreath =  int(raw_input("Breath: "))
    print 'new: ' + str(newTemp) + ' , ' + str(newHeart) + ' , ' + str(newBreath)

    check = newTemp - oldTemp
    check = newHeart - oldHeart
    check = newBreath - oldBreath
    
    print check


    if check != 0:
        print 'check !=0'
        oldTemp= newTemp
        oldHeart = newHeart
        oldBreath = newBreath
        print 'old:' + str(oldTemp) + ' , ' + str(oldHeart) + ' , ' + str(oldBreath)


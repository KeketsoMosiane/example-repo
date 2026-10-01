# triathlon events
swimming_time = int(input("Type in the time in minutes to complete swimming time: "))
cycling_time = int(input("Type in the time in minutes to complete cycling time: "))
running_time = int(input("Type in the time in minutes to complete running time: "))

total_time = swimming_time + cycling_time + running_time
if total_time < 100:
    print("Congatulation,You are awarded provincial colours!")
elif total_time > 100 and total_time <= 105:
    print("Congatulation,You are awarded Provincial half colours!")
elif total_time > 105 and total_time <= 110:
    print("Congatulation,You are awarded Provincial scroll!")
else:
    print("Better luck next time.")
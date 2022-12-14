import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
h = int(time.strftime('%H'))
print('\n', h)
if h >= 6 and h < 12:
    print("\n\nGood Morning !")
elif h >= 12 and h < 17:
    print("\n\nGood Afternoon !")
elif h >= 17 and h < 20:
    print("\n\nGood Evening !")
else:
    print("Good Night")
    

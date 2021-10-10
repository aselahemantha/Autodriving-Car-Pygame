import drive_car as dv

track_list = ["track1.png", "track2.png", "track3.png", "track4.png", "track5.png"]
while True:
    print('''
    AutoDriving Tesla CAR
    Author - AH
    Note - "If you want to quiz enter track num as 0"
    ''')
    track_num = int(input("Enter your track Number: "))
    if 0 > track_num > 6:
        print("Sorry. There is only 6 tracks")
    elif track_num == 0:
        break
    else:
        track_string = "images\\" + str(track_list[track_num])
        dv.track_int(track_string)
        break

from datetime import datetime
# from playsound import playsound


def time_validation(alrm):
    if len(alrm) != 11:
        return "Invalid Format!"
    else:
        if int(alrm[0:2]) > 12:
            return ("Invalid Hour Format!")
        elif int(alrm[3:5]) > 59:
            return ("Invalid Minute Format!")
        elif int(alrm[6:8]) > 59:
            return ("Invalid Second Format!")
        elif str(alrm[9:11]) not in ["am", "pm", "AM", "PM", "Am", "Pm", "aM", "pM"]:
            return ("Invalid AM/PM Format!")
        else:
            return ("Ok!")
alarm_time = input("Enter the alarm time in HH:MM:SS AM/PM format: ")
while True:
    validate = time_validation(alarm_time)

    if validate == "Ok!":
        print(f"Setting the alarm at {alarm_time}")
        break
    else:
        print(validate)



while True:
    current_time = datetime.now()

    current_hour_old = current_time.hour
    if int(current_hour_old) > 12:
        current_hour_new = current_hour_old - 12
        current_period = "PM"
    else:
        current_hour_new = current_hour_old
        current_period = "AM"
    current_minute = current_time.minute
    current_second = current_time.second

    alarm_hour = int(alarm_time[0:2])
    alarm_minute = int(alarm_time[3:5])
    alarm_second = int(alarm_time[6:8])
    alarm_period = alarm_time[9:11]

    

    if alarm_hour == current_hour_new and alarm_minute == current_minute and alarm_second == current_second and alarm_period == current_period:
        print("WAKE UPPPP!!!")
        # playsound('amazing_wake_up_sound.mp3')
        break

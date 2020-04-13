import sys
import re

def addMinutes(time, offset):

    # 720 minutes per 12 hours
    min_per_12hrs = 720

    # Enforce the time stamp pattern on the time argument
    if not re.match(r"^([1-9]|1[0,1,2]):([0-5][0-9]) [A,P]M$", time):
        print("Enter time in format [H]H:MM {AM|PM}")
        exit(1)

    # Enforce that offset is an integer
    offset = int(offset)

    print("Time: " + time + " , Type: " + str(type(time)))
    print("Offset: " + str(offset) + " , Type: " + str(type(offset)))

    hours = time.split(' ')[0].split(":")[0]
    minutes = time.split(' ')[0].split(":")[1]
    total_min = int(hours) * 60 + int(minutes)
    new_min = total_min + offset

    ampm = time.split(" ")[1]
    am_pm_flips = int(new_min / min_per_12hrs)

    new_time = new_min % min_per_12hrs
    new_hour = int( new_time / 60)
    if new_hour == 0:
        new_hour = hours
    new_min = new_time % 60

    print("AM/PM flips: " + str(am_pm_flips))

    final_time = str(new_hour) + ":" + str(new_min).zfill(2)
    print("New time: " + final_time)

if __name__ == "__main__":

    n = len(sys.argv)

    if n != 3:
        print("Requires 2 arguments")
        exit(1)

    time = sys.argv[1]
    offset = sys.argv[2]

    addMinutes(time, offset)
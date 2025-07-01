times = [
    "time1",
    "time2",
    "time3",
    "time4",
    "time5",
    "time6",
    "time7",
    "time8",
    "time9",
    "time10"
]

for i in range(10):
    if i < 4:
        print(" {} ".format(times[i]),end="=>")
    else:
        if i != 9:
            print(" {} ".format(times[i]),end="=-=")
        else:
            print(f" {times[i]}")
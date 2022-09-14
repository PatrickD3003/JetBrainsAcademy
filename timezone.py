days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
symbols = ["+", "-"]
i = 1
hour_to_minute = 60
london_hour = 10
london_minute = 30
now_time = london_hour * hour_to_minute + london_minute
one_day = 24 * hour_to_minute

change_time = input()
print(now_time)

if change_time[0] == symbols[0]:
    now_time += int(change_time[1:]) * hour_to_minute
    if now_time > one_day:
        i += 1
        print(days[i])
    else:
        print(days[i])

elif change_time[0] == symbols[1]:
    now_time -= int(change_time[1:]) * hour_to_minute
    if now_time < 0:
        i -= 1
        print(days[i])
    else:
        print(days[i])
elif int(change_time) == 0:
    print(days[i])

print(now_time)
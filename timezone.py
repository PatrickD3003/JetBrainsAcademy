# ceritanya patokan awal itu timezone london, jem 10:30 Tuesday
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
i = 1
hour_to_minute = 60
london_hour, london_minute = 10, 30
now_time = london_hour * hour_to_minute + london_minute
one_day = 24 * hour_to_minute

change_time = int(input())

now_time += change_time * hour_to_minute

def text(d, i, n, h):
    print(f"it is {d[i]}, {n // h}:{n % h} in this timezone right now")



if now_time > one_day:
    i += 1
    if i > len(days)-1:
        i = 0
    now_time -= one_day
    text(days, i, now_time, hour_to_minute)

elif now_time < 0:
    i -= 1
    now_time += one_day
    text(days, i, now_time, hour_to_minute)
else:
    text(days, i, now_time, hour_to_minute)

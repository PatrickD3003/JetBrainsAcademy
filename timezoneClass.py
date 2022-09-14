class TimeZone:
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    number_day = 0
    hour_to_minute = 60
    one_day = 24 * hour_to_minute
    def __init__(self, day, hour, minute):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.change_time = 0
        self.now_time = self.hour * self.hour_to_minute + self.minute

    def change_timezone(self):
        self.change_time = int(input())
        self.now_time += self.change_time * self.hour_to_minute

        if self.now_time > self.one_day:
            self.number_day += 1
            if self.number_day > len(self.days)-1:
                self.number_day = 0
            print(self.days[self.number_day])
            self.now_time -= self.one_day

        elif self.now_time < 0:
            self.number_day -= 1
            print(self.days[self.number_day])
            self.now_time += self.one_day
        
        else:
            print(self.days[self.number_day])
    
    def current_time(self):
        return f"it is {self.days[self.number_day]}, {self.now_time // self.hour_to_minute}:{self.now_time % self.hour_to_minute} in this timezone right now"

            

london = TimeZone(TimeZone.days[TimeZone.number_day], 10, 30)
london.change_timezone()
print(london.current_time())


    
        
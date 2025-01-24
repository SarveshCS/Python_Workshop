t1_hrs, t1_min = input("Enter time (ex, 2hrs 25min): ").split()
t2_hrs, t2_min = input("Enter time (ex, 2hrs 25min): ").split()
t1_hrs = int(t1_hrs[:-3])
t1_min = int(t1_min[:-3])
t2_hrs = int(t2_hrs[:-3])
t2_min = int(t2_min[:-3])

tmin = t1_min + t2_min
carry = 0
if tmin >= 60: carry = tmin // 60; tmin%=60
thrs = t1_hrs + t2_hrs + carry

print(f"{thrs}hrs {tmin}min")
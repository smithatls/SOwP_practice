speed = int(input())
hours = int(input())
for hour in range(1, hours + 1):
    speed2 = speed * hour
    print(f'{hour}, {speed2}')

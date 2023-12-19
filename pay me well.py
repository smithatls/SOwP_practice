hours_worked = int(input())
pay_rate = int(input())
MULTI = 1.5
HOURS = 40
payday = 0
if hours_worked > HOURS:
    payday = (HOURS + (hours_worked - HOURS) * MULTI) * pay_rate
else:
    payday = hours_worked * pay_rate
print(f'${payday:,.2f}')
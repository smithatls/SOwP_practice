sec = int(input())
if sec >= 86400:
    days = sec // 86400
    hours = (sec - days * 86400) // 3600
    minutes = (sec - hours * 3600 - days * 86400) // 60
    sec = sec - minutes * 60 - hours * 3600 - days * 86400
print(days, hours, minutes, sec)
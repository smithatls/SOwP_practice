y = int(input())
if y % 100 == 0:
    if y % 400 == 0:
        print('Yes')
elif y % 4 == 0:
    print('Yes!')
else:
    print('No(')
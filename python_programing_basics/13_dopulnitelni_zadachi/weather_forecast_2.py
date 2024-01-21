gradus = float(input())

if 0 <= gradus <= 4.9:
    print('unknown')

elif 5.00 <= gradus <= 11.9:
    print('Cold')

elif 12.00 <= gradus <= 14.9:
    print('Cool')

elif 15.00 <= gradus <= 20.00:
    print('Mild')

elif 20.1 <= gradus <= 25.9:
    print('Warm')

elif 26.00 <= gradus <= 35.00:
    print('Hot')

else:
    print('unknown')




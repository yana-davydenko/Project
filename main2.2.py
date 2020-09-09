x = int(input('Input the figure: _'))
y = int(input('Input the second figure: _'))

print('Summation:', (x + y))
print('Distraction:', (x - y))
if y == 0:
    print('Multiplication:', 0)
    print('Division is impossible')
else:
    print('Multiplication:', (x * y))
    print('Division:', round((x / y), 2)) #округление до второго знака
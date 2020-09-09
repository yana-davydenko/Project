x = int(input('Input the figure: _'))
y = int(input('Input the second figure: _'))

if y == 0:
    print('Summation:', (x + y))
    print('Substraction:', (x - y))
    print('Multiplication: 0')
    print('Division is impossible')
else:
    print('Summation:', (x + y))
    print('Substraction:', (x - y))
    print('Multiplication:', (x * y))
    print('Division:', round((x / y), 2)) #округление до второго знака





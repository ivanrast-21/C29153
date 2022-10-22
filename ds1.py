print('нажмите q чтоб выйти')
while True:
    s = input('введите знак (+,-,*,/)')
    if s == 'q': break
    if s in('+','-','*','/'):
        x = float(input('x= '))
        y = float(input('y= '))
        if s == '+':
            print("%.2f" % (x+y))

        if s == '-':
            print("%.2f" % (x-y))

        if s == '*':
            print("%.2f" % (x*y))

        if s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("вы делите на ноль")
    else:
        print('неверний знак')


import datetime
import keyboard
result = []
def divider(a, b, ):
     if a < b:
        raise ValueError("Ошибка")

     if b > 100:
        raise IndexError("Ошибка")
     return a/b
data = {10: 2, 2: 5, "123": 4, 18: 0, 20: 15, 8 : 4}
for key in data:
    try:
        res = divider(key, data[key])
    except ValueError:
        print('ошибка')
    except TypeError:
        print('ошибка')
    except ZeroDivisionError:
        print('ошибка')
    else:

        result.append(res)


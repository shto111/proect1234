print("Вы просыпаетесь в подвале, у вас связанны руки. Ваши действия: 1 - снять верёвку , любое другое число - Ничего не делать ")


try:
    x = 2
except NameError:
    print("Oops!  That was no valid number.  Try again...")

n = int(input())

if n == 1:
    print("Вы развязали руки и выдите что дверь из подвала открыта. Ваши действия: 1 - Выйти , любое другое число - ничего не делать")
else:
    print("Вы умираете в подвале от голода. :(")

q = int(input())
if q == 1:
    print("Вы выдите человека , который затащил вас в подвал. Ваши действия: 1 - Сбежать, другое число - Ударить его")
else:
    print("Вы не вышли, в итоге вы умираете от голода")
d = int(input())
if d == 1:
    print("Вы успешно сбегаете. УРААА!!!")
else:
    print("Вас избилим и посадили обратно в комнату и выбраться оттуда у вкас не получилось. :(")

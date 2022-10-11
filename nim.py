from random import randint
n = randint(4, 30)
print("Камней в куче:", n, "\n")
while 1:
    if n <= 4:
        n_comp = n - 1
    elif n % 4 == 0:
        n_comp = 3
    elif n % 4 == 3:
        n_comp = 2
    elif n % 4 == 2:
        n_comp = 1
    else:
        n_comp = randint(1, 3)
    n -= n_comp
    print("Компьютер взял камней:", n_comp,"\nОсталось камней:", n, "\n")
    if n == 1:
        print("\nКомпьютер выиграл")
        break
    while 1:
        try:        
            n_hum = int(input("Сколько камней берёте? "))
            if 1 <= n_hum <= 3:
                break
        except:
            pass
        print("Необходимо ввести число 1, 2, или 3")
    n -= n_hum
    print("Осталось камней:", n, "\n")
    if n == 1:
        print("Вы выиграли")
        break

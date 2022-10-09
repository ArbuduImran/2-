import random


class Casino:
    balanse = 1000
    print("добро пожаловать")
    print(f"ваш баланс = {balanse}$")

    def local_casino(self):
        while True:
            print('Запустить казино? (да или нет)')
            a = input('')
            if a == 'нет':
                print('вы вышли из казино!')
                break
            else:
                pass
            money = int(input("выберите сумму ставки\n"))
            if money > self.balanse:
                print("у вас не достаточно денег")
                continue
            choice = random.randint(1, 31)

            player = int(input("выберите одно число от 1 до 30   -   "))
            if player == choice:
                self.balanse += money
                print(f"Поздравляю вы выиграли - {money * 2}$ \n"
                      f"ваш баланс = {self.balanse}$")
            elif player != choice:
                self.balanse -= money
                print(f"Попробуйте еще раз <3 - {money}$\n")
            else:
                print("Вы где то допустили ошибку")


casino = Casino()
casino.local_casino()

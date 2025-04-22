import random

class Player:
    def __init__(self):
        self.balance = 100
        self.win = 0
        self.lose = 0

    def bet(self):
        print("Выбирете из 3 действий: \n1:Больше чем\n2:Меньше чем\n3:Равно")
        t = input()
        while t not in ["1", "2", "3"]:
            print("Выбирете из 3 действий: \n1:Больше чем\n2:Меньше чем\n3:Равно")
            t = input()
        t = int(t)
        r = input("Введите число на кроторое хотите поставить(1-6): ")
        while r not in ["1", "2", "3", "4", "5", "6"]:
            r = input("Введите число на кроторое хотите поставить(1-6): ")
        r = int(r)
        try:
            k = int(input(f"Введите вашу ставку(У вас {self.balance})"))
            while k < 0 or k > self.balance:
                k = int(input(f"Введите вашу ставку(У вас {self.balance})"))
            self.balance -= k
        except Exception as err:
            print(err)
            print("Саня даун тебя просили ввести ставку а не буквы и ставка не привышает баланс и не равна количеству твоих хромосом")
            k = 0
        return [t, r, k]




cheburekmoney = Casino()
misha = Player()
cheburekmoney.game(misha)
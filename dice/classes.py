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


class Casino:
    def __init__(self):
        self.win = 0
        self.lose = 0

    def game(self, obj:Player):
        while obj.balance > 0:
            m = obj.bet()
            dice = random.randint(1, 6)
            print(f"Выпало {dice}")
            if m[0] == 1:
                if dice > m[1]:
                    obj.balance += m[2] * 2
                    obj.win += 1
                    self.lose += 1
                else:
                    obj.lose += 1
                    self.win += 1
            elif m[0] == 2:
                if dice < m[1]:
                    obj.balance += m[2] * 2
                    obj.win += 1
                    self.lose += 1
                else:
                    obj.lose += 1
                    self.win += 1
            elif m[0] == 3:
                if dice == m[1]:
                    obj.balance += m[2] * 54
                    obj.win += 1
                    self.lose += 1
                else:
                    obj.lose += 1
                    self.win += 1
            print(f"Статистика казино:W {self.win} ,L {self.lose}")
            print(f"Статистика игрока:W {obj.win} ,L {obj.lose} ,На счету: {obj.balance}")
        print("Всего доброго, приходите ещё!")

cheburekmoney = Casino()
misha = Player()
cheburekmoney.game(misha)
print("yra vse vernylos")
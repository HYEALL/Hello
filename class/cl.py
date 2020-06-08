action = 0


class human:
    def meet(self, name, HP, MP):
        self.name = name
        self.HP = HP
        self.MP = MP
        print("안녕하세요")


class player(human):
    def __init__(self,AD):
        self.AD = AD

    def att(self,enemy):
        enemy.HP = enemy.HP - (player.AD - enemy.DP)


class npc(human):
    def meet(self):
        print("반갑습니다")


class enemy(human):
    def __init__(self, DP):
        self.DP = DP


player = player(30)
npc = npc()
enemy = enemy(10)


while True:
    action = input("행동을 입력해주세요")
    if action == "1":
        player.meet("유저", 100, 100)
        npc.meet()
        enemy.meet("적", 100, 100)
    elif action == "2":
        player.att(enemy)
        if enemy.HP == 0:
            break


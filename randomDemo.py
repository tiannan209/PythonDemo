# demo for random module
import random

for i in range(3):
    print(random.random())
    print(random.randint(10, 20))


members = ["tian", "tang", "ma", "Jason"]
leader = random.choice(members)
print(leader)


class Dice:
    def roll(self):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        return x, y


dice1 = Dice()
print(dice1.roll())

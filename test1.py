import random
class Cat:
    def __init__(self,name:str):
        self.name = name
        self.mood = random.randint(1, 100)
        self.energy = random.randint(1, 100)

    def chat(self):
        self.energy -= 10
        if self.mood>80:
            print(f"{self.name}主动蹭了蹭你，看起来很开心的样子૮₍˶•ᴗ•˶₎ა")
        elif self.mood<80 and self.mood>50:
            print(f"{self.name}趴在你旁边，大度的猫猫允许了人类的抚摸૮ ・ﻌ・ა")
        else:
            print("你蹲在猫窝旁呼唤了很久，猫猫完全没有回应，下次再尝试吧！")

    def sleep(self):
        self.energy += 50
        if self.energy > 100:
            self.energy = 100
        print("小猫在阳光下团成一团，看起来睡得很香")

    def work(self):
        self.mood -= 20
        self.energy -= 30
        if self.mood < 0:
            self.mood = 0
        print("外出打猎一天的猫猫骄傲回归！₍ᐢ·ᴗ·ᐢ₎")

cat1 = Cat('name')
name = input("输入小猫的名字吧：")
print(f"小猫:{name}૮ ・ﻌ・ა\n心情值:{cat1.mood}\n体力值:{cat1.energy}")
print("---------------------------------")

while True:
    print(f"{name}感到无聊了，接下来做什么好呢？")
    choice = input("1 聊天, 2 睡觉, 3 工作（请输入数字）")
    if choice == '1':
        cat1.chat()
    elif choice == '2':
        cat1.sleep()
    elif choice == '3':
        cat1.work()
    else:
        print("打错暗号了！猫猫似乎没理解你的意图")
    print(f"心情值:{cat1.mood}\n体力值:{cat1.energy}")

    print("---------------------------------")

    if cat1.energy<0:
        print("糟糕！小猫累倒了૮₍°□°₎ა\n铲屎官心惊胆战的过完了这个下午\n记得好好注意猫猫的体力！")
        break


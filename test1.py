import random
import requests

class Cat:
    def __init__(self,name:str):
        self.name = name
        self.mood = random.randint(1, 100)
        self.energy = random.randint(1, 100)
        self.ollama_url = "http://localhost:11434/api/generate"

    def chat(self):
        self.energy -= 10
        user_input = input(f"你对{self.name}说：")
        prompt = f"""你是一只名叫{self.name}的可爱的小猫，现在心情值{self.mood}分（0-100分，如果心情 > 80，打印开心回复；如果 < 50，打印敷衍回复。）。
                请回复主人的话，回复要体现出当前的心情状态，可以带猫猫表情，尽量简短有趣。

                主人说：{user_input}"""

        data = {
            "model": "gemma3:270m",
            "prompt": prompt,
            "stream": False,         #一次性完整回复
            "options": {
                "temperature": 0.8,  #随机性
                "max_tokens": 150    #回复长度
            }
        }

        response = requests.post("http://localhost:11434/api/generate", json=data)   #发送请求、获取回复
        reply = response.json()["response"].strip()                                      #转字典

        print(f"{self.name}：{reply}")    #回复

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

name = input("输入小猫的名字吧：")
cat1 = Cat(name)

print(f"小猫:{name}૮ ・ﻌ・ა\n心情值:{cat1.mood}\n体力值:{cat1.energy}")
print("---------------------------------")

while True:
    print(f"{name}感到无聊了，接下来做什么好呢？")
    choice = input("1 聊天(AI), 2 睡觉, 3 工作（请输入数字）")
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


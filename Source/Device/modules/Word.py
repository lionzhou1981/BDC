import os
import random


class Word:
    def __init__(self):
        self.words = {}
        number = 1
        while os.path.isfile("./words/{0}.txt".format(number)):
            f = open("./words/{0}.txt".format(number), 'r', encoding='UTF-8')
            word = None
            line = f.readline()
            while line:
                item = line.strip('\n').split(';')
                if len(item) == 1:
                    if word != None:
                        self.words[word["code"]] = word
                        word = None
                        continue
                else:
                    if word == None:
                        word = {"code": item[0], "sound": item[1], "data": {}}
                    else:
                        word["data"][item[0]] = item
                line = f.readline()
            f.close()
            number = number + 1
        print("Words started {0}".format(len(self.words)))

    def __del__(self):
        print("Words stopped")

    def random(self):
        index = random.randint(0, len(self.words) - 1)
        keys = list(self.words.keys())
        return self.words[keys[index]]

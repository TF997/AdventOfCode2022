datastream = open("input.txt", "r").read()

for i in range(len(datastream)):
    word = datastream[i: i + 14]
    if len(word) == len(set(word)):
        print(i+14)
        break

file = open("animals.txt", "r")
animals = []
while True:
    x = file.readline()
    if x.startswith("@"):
        x = x.upper()
        x = x.strip("@")
        x = x.strip("\n")
        animals.append(x)
    if x == "":
        break
file.close()


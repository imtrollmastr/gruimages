c = []
with open("countries.txt", "r") as countries:
    contents = countries.readlines()
    for i in contents:
        c.append(i.replace("\n", ""))
        print(c)
        with open("countries.txt", "wb") as countries:
            countries.write(bytes(str(c).encode("utf-8")))
input()
i = input()
nao = i.count("1")
sim = i.count("0")
print(["N" if nao >= sim else "Y"][0])
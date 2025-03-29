class LoggedDict(dict):
    pass

d = LoggedDict()
d["1"] = 1
d["2"] = 2

print(d)

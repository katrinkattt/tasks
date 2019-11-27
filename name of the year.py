m = ["metall", "metall", "voda", "voda","wood", "wood", "fair", "fair", "zemly", "zemly"]
a = ["krisa", "bik", "tigr", "zmey", "lochad", "obesiana", "petuch", "sobaka", "kaban"]
x = int(input())
x = x - 1900
print(m[x%10])
print(a[x%12])

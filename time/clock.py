n = int(input())
sutki = 86400

if n > sutki:
    print('sled day')
while n > sutki:
    n - sutki
chas = (n//60)//60
minut = (n-(chas*60*60))//60
sec = (n-(chas*60*60))-(minut*60)
print(chas, 'chasov')
print(minut,'minut')
print(sec, 'sekund')
if chas > 12:
    print(chas-12, 'chasov posle poludnya')

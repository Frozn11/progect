#generating random passwords
import secrets

simvols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
dlina = int(input('Введите желаемую длину пароля '))
sam_poral = ""

for i in range(dlina):
    sam_poral += ''.join(secrets.choice(simvols))
print(sam_poral)
import rsa

(public_key, private_key) = rsa.newkeys(1024)
print("\n", str(public_key))
print("\n", str(private_key), "\n")

pub_key = int(input("Задайте публичный ключ: "))
text = input("\n Введите текст сообщения:\n\n ")
message = text.encode("utf8")
crypt = rsa.encrypt(message, rsa.PublicKey(pub_key, 65537))
with open("text_crypt.txt","wb") as crypt_file:
	crypt_file.write(crypt)
	print("\nЗашифрованный текст:\n\n"+str(crypt)+"\nФайл: 'text_crypt.txt' сохранен!\n")
print("\nФайл: 'crypt.py' успешно сохранен!")

new_str = str(private_key)
new_str = new_str[11:(len(new_str)-1)]
# print(new_str)
new_list = new_str.split(', ')
n = int(new_list[0])
# print(n)
e = int(new_list[1])
d = int(new_list[2])
p = int(new_list[3])
q = int(new_list[4])

# print(n == private_key.n)
# print(e == private_key.e)
# print(d == private_key.d)
# print(p == private_key.p)
# print(q == private_key.q)

file = input("Введите имя файла: ")
with open(file, "rb") as read_crypt:
	read = read_crypt.read()
    
	message = rsa.decrypt(read, rsa.PrivateKey(n, e, d, p, q))
	print("\nРасшифрованный текст:\n\n" + str(message.decode("utf8")) + "\n")

print("Файл: 'key.py' успешно сохранен!\n")
import rsa
(public_key, private_key) = rsa.newkeys(1024)
print("\n", str(public_key))
print("\n", str(private_key), "\n")
with open("crypt.py","w") as crypt: 
	crypt.write('''
import rsa 
pub_key = int(input("Задайте публичный ключ: "))
text = input("\n Введите текст сообщения:\n\n ")
message = text.encode("utf8")
crypt = rsa.encrypt(message, rsa.PublicKey(pub_key,65537))
with open("text_crypt.txt","wb") as crypt_file:
	crypt_file.write(crypt)
	print("\nЗашифрованный:\n\n"+str(crypt)+"\n\Файл: 'text_crypt.txt' сохранен!\n")
''') 
print("\nФайл: 'crypt.py' успешно сохранен!")
with open("key.py","w") as key: 
	key.write('''
import rsa
file = input("Введите имя файла: ")
with open(file, "rb") as r:
	read = r.read()
	message = rsa.decrypt(read,rsa.'''+str(private_key)+''')
	print("\nРасшифрованный текст:\n\n", str(message.decode("utf8")), "\n")
''') 
print("Файл: 'key.py' успешно сохранен!\n")


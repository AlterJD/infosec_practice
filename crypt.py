
import rsa 
pub_key = int(input("Задайте публичный ключ: "))
text = input("\n Введите текст сообщения:\n\n ")
message = text.encode("utf8")
crypt = rsa.encrypt(message, rsa.PublicKey(pub_key,65537))
with open("text_crypt.txt","wb") as crypt_file:
	crypt_file.write(crypt)
	print("\nЗашифрованный:\n\n"+str(crypt)+"\n\Файл: 'text_crypt.txt' сохранен!\n")

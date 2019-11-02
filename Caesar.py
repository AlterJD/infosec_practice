# -*- coding: utf-8 -*-
#Шифр Цезаря
rusLetters = ['а','б','в','г','д','е','ё','ж','з','и','к','л','м','н','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я', \
    'А','Б','В','Г','Д','Е','Ё','Ж','З','И','К','Л','М','Н','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']

rusLetters2 = []

for i in range(len(rusLetters)):
    rusLetters2.append(rusLetters[i])

def change_rusLetters2():
    for _ in range(num):   #num - ключ-число, т.е смещение
        rusLetters2.append(rusLetters2[0])
        rusLetters2.remove(rusLetters2[0])

print('''Шифр Цезаря
Введите (1), чтобы зашифровать текст из потока ввода.
Введите (2), чтобы зашифровать текст из файла. 
Введите (3), чтобы расшифровать текст из файла.
Введите (4), чтобы расшифровать текст из потока ввода. ''')

try:

    option = int(input("[*] Выберите опцию:"))
    if option == 1:
        num = int(input("[*] Введите ключ-число [0 - %s]: " %(str(len(rusLetters)))))
        change_rusLetters2()
        msg = input("\n [*] Введите текст: \n [текст]")

        msgc = ""
        for i in msg:
            for j in range(len(rusLetters)):
                if i == rusLetters[j]:
                    msgc += rusLetters2[j]
        crypt = open("./text_crypt.txt", "w")
        print("\nЗашифрованный текст:" + msgc + "\n")
        crypt.write(msgc)
        crypt.close()
    
    elif option == 2:
        num = int(input("[*] Введите ключ-число [0 - %s]: " %(str(len(rusLetters)))))
        change_rusLetters2()
        print("\n [*] Поместите текстовый файл в папку и назоваите его text_to_crypt.txt ")

        crypt = open("./text_to_crypt.txt","r", encoding="utf-8")
        read = crypt.read()
        msgc = ""
        for i in read:
            for j in range(len(rusLetters)):
                if i == rusLetters[j]:
                    msgc += rusLetters2[j]
        crypt = open("./text_crypt.txt", "w")
        print("\nЗашифрованный текст:" + msgc + "\n")
        crypt.write(msgc)
        crypt.close()
    
    elif option == 3:
        num = int(input("[*] Введите ключ-число [0 - %s]: " %(str(len(rusLetters)))))
        change_rusLetters2()

        decrypt = open("./text_crypt.txt","r")
        read = decrypt.read()
        msgd = ""
        for i in read:
            for j in range(len(rusLetters)):
                if i == rusLetters2[j]:
                    msgd += rusLetters[j]
        
        print("\n[*] Расшифрованный текст:")
        print("[text] <<"+ str(msgd))
        answer = ("\n[*] Сохранить расшифрованный текст в файл:\n [да/нет]")

        if answer == 'нет' or answer == 'no':
            decrypt_w = open("./text_decrypt.txt","w")
            decrypt_w.write(msgd)
            decrypt_w.close()
            print("\n Файл './text_decrypt.txt' сохранен! ")
        else:
            pass
        decrypt.close()

    elif option == 4:
        num = int(input("[*] Введите ключ-число [0 - %s]: " %(str(len(rusLetters)))))
        change_rusLetters2()
        msg = input("\n [*] Введите зашифрованный текст: \n [текст]")

        msgd = ""
        for i in msg:
            for j in range(len(rusLetters)):
                if i == rusLetters2[j]:
                    msgd += rusLetters[j]
        print("\n[*] Расшифрованный текст:")
        print("[text] <<"+ str(msgd))

    else:
        print('Опция не выбрана!')
except ValueError:
    print("Введите нормальное число!")

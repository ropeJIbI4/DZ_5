# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

text = input("Введите словосочетание c абв :")
def delete(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)
text = delete(text)
print(text)
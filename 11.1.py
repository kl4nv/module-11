import requests

r = requests.get('http://vk.com')
print(r.status_code) #получаем код работоспособности сайта
print(r.cookies) #получаем cookie если есть
print('')

import pandas as pd

s = pd.Series({'aa': 1, "bb": 2, 'cc': 3}) #создаст экзмепляр из словаря
print(s)
print(s.array) #фактический массив, поддерживающий a Series

from PIL import Image

with Image.open("picture.jpg") as im1: # открываем картинку
    im1.rotate(45).show()              # и поворачиваем ее на 45градусов
    with Image.open('picture2.img') as im2:
        #Накладываем 2е изображение (im2) на 1е (im1) с учетом альфа-каналов(заполнены или нет пиксели)
        Image.alpha_composite(im1, im2)



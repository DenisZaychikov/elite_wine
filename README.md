# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Установка

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей: 
`pip install -r requirements.txt`


## Запуск

- Скачайте код
- Для генерации сайта `index.html`, воспользуйтесь командой `python3 script.py <аргумент>`.
  В качестве `аргумента` передайте свой текстовый файл. Например: `python3 script.py file.txt`.
  Текстовый файл должен находиться в одной папке с файлом `script.py`.
  Текстовый файл должен выглядеть примерно так:
  ```
  # Белые вина


  Название: Белая леди

  Сорт: Дамский пальчик

  Цена: 399

  Картинка: images/belaya_ledi.png

  Выгодное предложение


  Название: Ркацители

  Сорт: Ркацители

  Цена: 499

  Картинка: images/rkaciteli.png


  Название: Кокур

  Сорт: Кокур

  Цена: 450

  Картинка: images/kokur.png
  
  
  # Красные вина


  Название: Черный лекарь

  Сорт: Качич

  Цена: 399

  Картинка: images/chernyi_lekar.png


  Название: Хванчкара

  Сорт: Александраули

  Цена: 550

  Картинка: images/hvanchkara.png


  Название: Киндзмараули

  Сорт: Саперави

  Цена: 550

  Картинка: images/kindzmarauli.png


  # Напитки


  Название: Чача

  Сорт: 

  Цена: 299

  Картинка: images/chacha.png

  Выгодное предложение


  Название: Коньяк классический

  Сорт: 

  Цена: 350

  Картинка: images/konyak_klassicheskyi.png


  Название: Коньяк кизиловый

  Сорт: 

  Цена: 350

  Картинка: images/konyak_kizilovyi.png
  ```

- Запустите сайт `index.html` 

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
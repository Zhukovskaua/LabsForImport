import pickle

# Открываем файлик для чтения
text = open('5.p','rb')

# Загружаем объект
obj = pickle.load(text)

# Смотрим что получилось
print(dir(obj))

for lines in obj:
    line = [ch * count for ch, count in lines]
    print( "".join(line))
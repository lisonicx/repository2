a = ' '
print ('введите имя студента:')
name = str(input())
print ('введите фамилию студента:')
surname = str(input())
print ('введите год рождения студента:')
year = int(input())
print (name, '_', surname, '_', year)
a = name
name = surname
surname = a
year = year + 60
print (name, '_', surname, '_', year)

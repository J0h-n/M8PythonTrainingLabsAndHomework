drone_list = ["DJI Mavic 2 Pro", "DJI Mavic 2 Zoom", "DJI Mavic 2 Enterprise Advanced", "AUTEL Evo II Pro", "DJI Mini 2", "Autel Evo Nano", "Autel Evo Lite Plus", "Parrot Anafi", "Dji Inspire 2", "DJI Mavic 3", "DJI Mavic Air2s", "Ryze Tello", "Eachine Trashcan"]

drone_weight_list = [903, 900, 920, 980, 249, 249, 600, 540, 1500, 1000, 570, 130, 110]

#в drone по очереди попадает каждый дрон из списка drone_list
for drone in drone_list:
	print(drone)
#print(len(drone_list)==len(drone_weight_list))
#TODO1
#выведите все дроны производителя, название которого введет пользователь через input, и подсчитайте их количество. 
#учтите, что:
#1) DJI и Dji - это один и тот же производитель! такие случаи тоже должны обрабатываться
#2) при выводе исправьте название производителя, если допущена ошибка. правильный вариант названия: DJI, Autel
"""myTODO1"""
print("""\nmyTODO1""")
ansDrone = input('Введите производителя:')

ansList = list(filter(lambda x: ansDrone.lower() in x.lower(),drone_list))
if ansDrone:
  print(';'.join(ansList))
  print(f'Количество производителей: {len(ansList)}')
else:
  print("Нет таких производителей")
print("""myTODO1END""")

#TODO2
#подсчитайте количество моделей дронов каждого производителя из списка drone_list. производители: DJI, Autel, Parrot, Ryze, Eachine
"""myTODO2"""
print("""\nmyTODO2""")
numberList = [0]*5 #DJI:0, Autel:1, Parrot:2, Ryze:3, Eachine:4
for drone in drone_list:
  if "DJI" in drone:
    numberList[0]+=1
  elif "Autel" in drone:
    numberList[1]+=1
  elif "Parrot" in drone:
    numberList[2]+=1
  elif "Ryze" in drone:
    numberList[3]+=1
  elif "Eachine" in drone:
    numberList[4]+=1
nameList = 'DJI Autel Parrot Ryze Eachine'.split()
for i in range(len(nameList)):
  print(f'{nameList[i]}:{numberList[i]}')
print("""myTODO2END""")

#TODO3
#выведите все дроны из списка, которые нужно регистрировать (масса больше 150 г), и подсчитайте их количество. 
#сделайте то же самое для всех дронов, которые не нужно регистрировать
#для этого вам нужно параллельно обрабатывать два списка: drone_list и drone_weight_list:
#как работает zip, мы разберем на лекции про списки. пока что просто пользуйтесь
"""myTODO3"""
print("""\nmyTODO3""")
n1,n2 = 0,0 # регистрируем/не регистрируем
for drone, weight in zip(drone_list,  drone_weight_list):
  if weight >150:
      print(drone, weight)
      n1 += 1
  else:
    n2 += 1
print(f'Регистрируется: {n1}\nНе регистрируется: {n2}')
print("""myTODO3END""")  

#TODO4
#для каждого дрона из списка выведите, нудно ли согласовывать полет при следующих условиях:
#высота 100 м, полет над населенным пунктом, вне закрытых зон, в прямой видимости
#помните, что для дронов тяжелее 150 г согласовывать полет над населенным пунктом - обязательно!
"""myTODO4"""
print("""\nmyTODO4""")
for drone, weight in zip(drone_list,  drone_weight_list):
  if weight >150:
      print(f'Для дрона "{drone}"  обязательно согласовать полет над населенным пунктом')
  else:
      print(f'Для дрона "{drone}"  не обязательно согласовать полет над населенным пунктом')
    
print("""myTODO4END""") 
#TODO5*
#модифицируйте решение задания TODO1:
#теперь для введенного пользователем производителя вы должны вывести строку, содержащую перечисление моделей и БЕЗ названия производителя.
#например, пользователь ввел "Autel". ваша программа должна вывести вот такой результат: "Evo II Pro, Evo Nano, Evo Lite Plus". для этого вам понадобится несколько функций работы со строками. решить эту задачу можно несколькими разными способами
#производители те же: DJI, Autel, Parrot, Ryze, Eachine
"""myTODO5"""
print("""\nmyTODO5""")
ansDrone1 = input('Введите производителя(второй вариант): ')

ansList1 = list(filter(lambda x: ansDrone1.lower() in x.lower(),drone_list))
for drone in ansList1:
  print(' '.join(drone.split(sep=ansDrone1)))
print("""myTODO5END""")
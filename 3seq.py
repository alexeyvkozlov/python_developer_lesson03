#~ USAGE
# cd d:\python_developer
# .\pydev\Scripts\activate
# cd d:\python_developer\lesson_03
#~~~~~~~~~~~~~~~~~~~~~~~~
# python 3seq.py
#~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
  #~ ввод элементов первого списка
  input_list1 = input("Введите элементы 1-го списка через запятую: ")
  list1 = [int(num) for num in input_list1.split(',') if num.isdigit()]
  #~ ввод элементов второго списка
  input_list2 = input("Введите элементы 2-го списка через запятую: ")
  list2 = [int(num) for num in input_list2.split(',') if num.isdigit()]
  #~ удаляем элементы из первого списка, которые есть во втором списке
  result = [num for num in list1 if num not in list2]
  print("Результат:", ", ".join(map(str, result)))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
  main()
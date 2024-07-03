#~ USAGE
# cd d:\python_developer
# .\pydev\Scripts\activate
# cd d:\python_developer\lesson_03
#~~~~~~~~~~~~~~~~~~~~~~~~
# python 1seq.py
#~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
  num_elements = int(input("Введите количество элементов: "))
  numbers = []
  for i in range(num_elements):
    number = int(input(f"Введите {i+1} элемент: "))
    numbers.append(number)
  
  numbers.sort()
  print(f"Вывод: {numbers}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
  main()

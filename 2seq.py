#~ USAGE
# cd d:\python_developer
# .\pydev\Scripts\activate
# cd d:\python_developer\lesson_03
#~~~~~~~~~~~~~~~~~~~~~~~~
# python 2seq.py
#~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
  user_input = input("Введите элементы списка через запятую, точку с запятой или слэш: ")
  #~ заменяем разделители на запятые
  user_input = user_input.replace(';', ',').replace('/', ',')
  #~ получаем список цифр
  numbers = [int(num) for num in user_input.split(',') if num.isdigit()]
  #~ получаем только уникальные элементы
  unique_numbers = list(set(numbers))
  print("Результат:", ", ".join(map(str, unique_numbers)))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
  main()

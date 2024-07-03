#~ USAGE
# cd d:\python_developer
# .\pydev\Scripts\activate
# cd d:\python_developer\lesson_03
#~~~~~~~~~~~~~~~~~~~~~~~~
# python victory.py
#~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import random

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
famous_people = [
  ("Александр Сергеевич Пушкин", "06.06.1799"),
  ("Альберт Эйнштейн", "14.03.1879"),
  ("Махатма Ганди", "02.10.1869"),
  ("Мартин Лютер Кинг", "15.01.1929"),
  ("Стив Джобс", "24.02.1955"),
  ("Леонардо да Винчи", "15.04.1452"),
  ("Мэри Кюри", "07.11.1867"),
  ("Нельсон Мандела", "18.07.1918"),
  ("Вольфганг Амадей Моцарт", "27.01.1756"),
  ("Майя Анжелу", "04.04.1928")
]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def format_date(date):
  day, month, year = date.split('.')
  months = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
  return f"{int(day)} {months[int(month) - 1]} {year} года"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def play_quiz():
  selected_people = random.sample(famous_people, 5)
  correct_answers = 0
  incorrect_answers = 0

  for famous_person, birth_date in selected_people:
    answer = input(f"Введите дату рождения {famous_person} (в формате 'dd.mm.yyyy'): ")
    if answer == birth_date:
      correct_answers += 1
    else:
      incorrect_answers += 1
      print(f"Неверно! Правильный ответ: {format_date(birth_date)}")

  print("\nРезультаты:")
  print(f"Количество правильных ответов: {correct_answers}")
  print(f"Количество ошибок: {incorrect_answers}")

  restart = input("Хотите начать заново? (да/нет): ")
  if restart.lower() == "да":
    play_quiz()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
  play_quiz()

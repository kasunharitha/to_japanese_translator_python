#silly simple project 2 : A simple to_japanese translator

from translate import Translator

translator = Translator(to_lang="ja")


with open("test.txt", mode="r+") as my_file:
    text = my_file.read()
    print(text)

translation = translator.translate(text)


with open('translation.txt', mode='w', encoding="utf-8") as translation1:
    translation1.write(translation)
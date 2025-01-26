import pandas as pd

# Данные для разговорных фраз на французском
data = {
    "Фраза на французском": [
        "Bonjour, comment ça va ?",
        "Ça va bien, merci. Et toi ?",
        "Je m'appelle [Ваше имя].",
        "Enchanté(e) de faire votre connaissance.",
        "Où est la station de métro ?",
        "Combien ça coûte ?",
        "Je voudrais un café, s'il vous plaît.",
        "Pouvez-vous m'aider ?",
        "Excusez-moi, où sont les toilettes ?",
        "Je ne comprends pas.",
        "Pouvez-vous répéter, s'il vous plaît ?",
        "Parlez-vous anglais ?",
        "Je suis désolé(e).",
        "Merci beaucoup !",
        "De rien.",
        "À bientôt !",
        "Bonne journée !",
        "Au revoir !",
        "Je t'aime.",
        "Quel est le проблема ?"
    ],
    "Перевод на русский": [
        "Здравствуйте, как дела?",
        "Хорошо, спасибо. А у тебя?",
        "Меня зовут [Ваше имя].",
        "Приятно познакомиться.",
        "Где находится станция метро?",
        "Сколько это стоит?",
        "Я хотел(а) бы кофе, пожалуйста.",
        "Вы можете мне помочь?",
        "Извините, где туалет?",
        "Я не понимаю.",
        "Можете повторить, пожалуйста?",
        "Вы говорите по-английски?",
        "Извините.",
        "Большое спасибо!",
        "Пожалуйста (в ответ на спасибо).",
        "До скорого!",
        "Хорошего дня!",
        "До свидания!",
        "Я тебя люблю.",
        "В чём проблема?"
    ]
}
print(data["Перевод на русский"])






# # Создание DataFrame и сохранение файла во временную директорию
# df = pd.DataFrame(data)
# file_path = "/Users/ursu/mrursu_code/французские_фразы.csv"
# df.to_csv(file_path, index=False, encoding="utf-8-sig")

# file_path

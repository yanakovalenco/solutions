# "Чат-бот с искусственным интеллектом на Python" - интенсив Skillbox

import random
import nltk
import json
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# создаем библиотеку "вопрос - ответ"
BOT_CONFIG = {
    'intents': {  # перевод - намерение
        'hello': {
            'examples': ['привет!', 'хай!!', 'прив'],  # примеры
            'responses': ['здравствуйте', 'хеллоу!', 'хей!!!']  # ответы
        },
        'bye': {
            'examples': ['пока!', 'покеда!!', 'до свидания'],
            'responses': ['увидимся))', 'до связи', 'бай!']
        },
        'howdoyoudo': {
            'examples': ['как дела?', 'как ты?', 'как поживаешь?', 'как самочувствие?'],
            'responses': ['отлично!', 'норм', 'грущу', 'я всего лишь робот']
        },
        'wheather': {
            'examples': ['какая погода сейчас?', 'как на улице?', 'скажи погоду', 'прогноз погоды'],
            'responses': ['солнечный день', 'тепло', 'холодно', 'лучше не выходить на улицу']
        },
        'whoareyou': {
            'examples': ['ты робот?', 'кто ты?', 'что ты такое?'],
            'responses': ['я робот', 'я обученная машина', 'я робот, а ты?']
        },
    }
}


def clean(text):  # вводим функцию для очистки вводимого текста
    clean_text = ''  # создаем пустую переменную
    for ch in text.lower():
        # ch - последовательно значения всех символов; lower - перевод в нижний регистр вводимого текста
        if ch in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя ':
            # если символ из русского алфавита, то мы его добавляем в переменную, иначе символ пропускается
            clean_text = clean_text + ch
    return clean_text  # возвращаем конечное, обработанное значение функции


# with open('/content/BOT_CONFIG.json') as f:
#   BOT_CONFIG = json.load(f) # вызываем функцию лоад из библиотеки джейсон для файла ф


texts = []
y = []
for intent in BOT_CONFIG['intents'].keys():
    for example in BOT_CONFIG['intents'][intent]['examples']:
        texts.append(example)
        y.append(intent)

train_texts, test_texts, y_train, y_test = train_test_split(texts, y, random_state=42, test_size=0.2)

# векторное представление текста (количество слов из словаря во фразе)
vectorizer = CountVectorizer(ngram_range=(1, 3), analyzer='char_wb')
X_train = vectorizer.fit_transform(train_texts)  # изучение словаря и возврат матрицы терминов документа (векторов)
X_test = vectorizer.transform(test_texts)  # преобразование документов в матрицу терминов документов

vocab = vectorizer.get_feature_names_out()  # обучение бота (получение выходных объектов для преобразования)

clf = RandomForestClassifier(n_estimators=300).fit(X_train, y_train)
# LogisticRegression().fit(X_train, y_train)        # fit = обучить, X_train - вектора, y_train - ответы на вектора
clf.score(X_train, y_train), clf.score(X_test, y_test)  # 0.14893617021276595
# clf.predict(vectorizer.transform(['привет!']))  # проверяем, что всё получилось, что находит нужный интент


# def get_intent(text):  # создаем функцию для поиска ответов
#     for intent in BOT_CONFIG['intents']:
#         for example in BOT_CONFIG['intents'][intent]['examples']:
#             # в библиотеке полностью прописываем путь, выделяя намерения как переменную
#             s1 = clean(text)  # применяем функцию для вводимого текста
#             s2 = clean(example)  # применяем функцию для примера из библиотеки, чтобы сравнить текст
#             if nltk.edit_distance(s1, s2) / max(len(s1), len(s2)) < 0.4:
#                 # edit_distance - вычисляет расстояние Левенштейна (минимальное количество односимвольных операций,
#                 # необходимых для превращения одной последовательности символов в другую)
#                 return intent
#     return 'интент не найден'


def get_intent_by_model(text):  # создаем функцию для поиска ответов
    return clf.predict(vectorizer.transform([text]))[0]


def bot(input_text):  # функция для создания бота
    intent = get_intent_by_model(input_text)  # применяем функцию к вводимому тексту
    return random.choice(BOT_CONFIG['intents'][intent]['responses'])


print('Привет, я обученная заготовка для чат-бота, напиши что-нибудь.')
print('P.S. Для завершения работы напиши "stop"')
input_text = ''
while input_text != 'stop':
    input_text = input()
    if input_text != 'stop':
        response = bot(input_text)  # применяем функцию, при которой выбираем ответ для вводимого текста
        print(response)

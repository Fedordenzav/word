




words = {
    "лол": "что то смешное",
    "кринж": "стыд",
    "сигма": "уверенность",
    "агро" : "злой",
}


word = input("Введите слово:").lower()
if word in words:
    print(words[word])
else:
    print("Слово не найдено(")


sentence = input("Enter a sentence: ")
sentence= sentence.lower()
def count_dict(sentence):
    wo = {}
    for letter in sentence:
        wo[letter] = sentence.count(letter)
    for _ in sorted(wo):
        print(_,' ', str(wo[_]))
count_dict(sentence)

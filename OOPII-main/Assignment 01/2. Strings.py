sentence = "Learning Python is fun and rewarding."
print(sentence)
print(sentence[-28:-14])
sentence=sentence.replace('rewarding','exciting')
print(sentence)
#print(sentence.__add__(' Keep Practicing!'))
index=sentence.find('exciting')
sentence=sentence[:index+len('exciting.')]+' Keep Practicing!'
print(sentence)
#sentence=sentence.capitalize()
#print(sentence)
sentence=sentence.split()
sentence=[word.capitalize() for word in sentence]
sentence=' '.join(sentence)
print(sentence)
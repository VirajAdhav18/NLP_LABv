from gensim.utils import simple_preprocess
from gensim import corpora

#text2 = open('sample_text.txt', encoding='utf-8')

text2 = ["""Hello, how are you?", "How do you do?", 
   "Hey what are you doing? yes you What are you doing?"""]

tokens2 = []
# for line in text2.read().split('.'):
for line in text2[0].split('.'):
    tokens2.append(simple_preprocess(line, deacc=True))

g_dict2 = corpora.Dictionary(tokens2)

g_bow =[g_dict2.doc2bow(token, allow_update = True) for token in tokens2]
print("Bag of Words : ", g_bow)
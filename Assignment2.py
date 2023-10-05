import gensim
from gensim import corpora
from gensim.utils import simple_preprocess
from gensim import corpora

text1 = ["My name is Viraj Adhav.", 
   "I am from Sanjivani College of Engineering.", 
   "Viraj is from Kopargaon. "]


tokens1 = [[item for item in line.split()] for line in text1]
g_dict1 = corpora.Dictionary(tokens1)

print("The dictionary has: " +str(len(g_dict1)) + " tokens\n")
print(g_dict1.token2id)

g_bow =[g_dict1.doc2bow(token, allow_update = True) for token in tokens1]
print("Bag of Words : ", g_bow)


print("\n--------------------------------------------------------------------------------------------------------------------------")
print("-----TFIDF------------------------------------------------------------------------------------------------------------------")
text = ["My name is Viraj Adhav.", 
   "I am from Sanjivani College of Engineering.", 
   "Viraj is from Kopargaon. "]

g_dict = corpora.Dictionary([simple_preprocess(line) for line in text])
g_bow = [g_dict.doc2bow(simple_preprocess(line)) for line in text]

print("Dictionary : ")
for item in g_bow:
    print([[g_dict[id], freq] for id, freq in item])


#     OUTPUT:---------------

#     The dictionary has: 13 tokens

# {'Adhav.': 0, 'My': 1, 'Viraj': 2, 'is': 3, 'name': 4, 'College': 5, 'Engineering.': 6, 'I': 7, 'Sanjivani': 8, 'am': 9, 'from': 10, 'of': 11, 'Kopargaon.': 12}
# Bag of Words :  [[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)], [(5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1)], [(2, 1), (3, 1), (10, 1), (12, 1)]]

# --------------------------------------------------------------------------------------------------------------------------
# -----TFIDF------------------------------------------------------------------------------------------------------------------
# Dictionary : 
# [['adhav', 1], ['is', 1], ['my', 1], ['name', 1], ['viraj', 1]]
# [['am', 1], ['college', 1], ['engineering', 1], ['from', 1], ['of', 1], ['sanjivani', 1]]
# [['is', 1], ['viraj', 1], ['from', 1], ['kopargaon', 1]]





    
    

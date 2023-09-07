##Assignment No.01##
#Name:Adhav Viraj Vikram
##Roll No:01
#Batch:B1
#Title:"Text Pre-Processing using NLP operations:perform Tokenization
# Stop word removal,Lemmatization ,Part-of-Speech Tagging use any sample text"

#import Libraries
import spacy
#language model loaded
nlp = spacy.load("en_core_web_sm")
about_text = (
   "My name is viraj and I am from kopargaon and I am studying Btech in Information Technology."
    "who is your friend and where does he lives in the town."
)
##1-------Tokenization---------##

about_doc = nlp(about_text)

for token in about_doc:
    print (token, token.idx)


##2-------Stop Words-----------###

about_doc = nlp(about_text)
print([token for token in about_doc if not token.is_stop])


##3-------Lemmatization-----------##

about_doc=nlp(about_text)
for token in about_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")
        

 ##4-------Part of Speech----------##   
               
about_doc = nlp(about_text)
for token in about_doc:
    print(
        f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}"""
    )


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

#OUTPUT
#    My 0
# name 3
# is 8
# viraj 11
# and 17
# I 21
# am 23
# from 26
# kopargaon 31
# and 41
# I 45
# am 47
# studying 50
# Btech 59
# in 65
# Information 68
# Technology.who 80
# is 95
# your 98
# friend 103
# and 110
# where 114
# does 120
# he 125
# lives 128
# in 134
# the 137
# town 141
# . 145
# [viraj, kopargaon, studying, Btech, Information, Technology.who, friend, lives, town, .]
#                   My : my
#                   is : be
#                   am : be
#                   am : be
#             studying : study
#                   is : be
#                 does : do
#                lives : live

# TOKEN: My
# =====
# TAG: PRP$       POS: PRON
# EXPLANATION: pronoun, possessive

# TOKEN: name
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: is
# =====
# TAG: VBZ        POS: AUX
# EXPLANATION: verb, 3rd person singular present

# TOKEN: viraj
# =====
# TAG: JJ         POS: ADJ
# EXPLANATION: adjective (English), other noun-modifier (Chinese)

# TOKEN: and
# =====
# TAG: CC         POS: CCONJ
# EXPLANATION: conjunction, coordinating

# TOKEN: I
# =====
# TAG: PRP        POS: PRON
# EXPLANATION: pronoun, personal

# TOKEN: am
# =====
# TAG: VBP        POS: AUX
# EXPLANATION: verb, non-3rd person singular present

# TOKEN: from
# =====
# TAG: IN         POS: ADP
# EXPLANATION: conjunction, subordinating or preposition

# TOKEN: kopargaon
# =====
# TAG: NNP        POS: PROPN
# EXPLANATION: noun, proper singular

# TOKEN: and
# =====
# TAG: CC         POS: CCONJ
# EXPLANATION: conjunction, coordinating

# TOKEN: I
# =====
# TAG: PRP        POS: PRON
# EXPLANATION: pronoun, personal

# TOKEN: am
# =====
# TAG: VBP        POS: AUX
# EXPLANATION: verb, non-3rd person singular present

# TOKEN: studying
# =====
# TAG: VBG        POS: VERB
# EXPLANATION: verb, gerund or present participle

# TOKEN: Btech
# =====
# TAG: NNP        POS: PROPN
# EXPLANATION: noun, proper singular

# TOKEN: in
# =====
# TAG: IN         POS: ADP
# EXPLANATION: conjunction, subordinating or preposition

# TOKEN: Information
# =====
# TAG: NNP        POS: PROPN
# EXPLANATION: noun, proper singular

# TOKEN: Technology.who
# =====
# TAG: NNP        POS: PROPN
# EXPLANATION: noun, proper singular

# TOKEN: is
# =====
# TAG: VBZ        POS: AUX
# EXPLANATION: verb, 3rd person singular present

# TOKEN: your
# =====
# TAG: PRP$       POS: PRON
# EXPLANATION: pronoun, possessive

# TOKEN: friend
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: and
# =====
# TAG: CC         POS: CCONJ
# EXPLANATION: conjunction, coordinating

# TOKEN: where
# =====
# TAG: WRB        POS: SCONJ
# EXPLANATION: wh-adverb

# TOKEN: does
# =====
# TAG: VBZ        POS: AUX
# EXPLANATION: verb, 3rd person singular present

# TOKEN: he
# =====
# TAG: PRP        POS: PRON
# EXPLANATION: pronoun, personal

# TOKEN: lives
# =====
# TAG: VBZ        POS: VERB
# EXPLANATION: verb, 3rd person singular present

# TOKEN: in
# =====
# TAG: IN         POS: ADP
# EXPLANATION: conjunction, subordinating or preposition

# TOKEN: the
# =====
# TAG: DT         POS: DET
# EXPLANATION: determiner

# TOKEN: town
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: .
# =====
# TAG: .          POS: PUNCT
# EXPLANATION: punctuation mark, sentence closer

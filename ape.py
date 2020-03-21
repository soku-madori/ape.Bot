import csv
import os
import re
import random

from flask import request
# from janome.tokenizer import Tokenizer
from nltk.corpus import wordnet
import nagisa
# import nltk
# nltk.download("wordnet")
# nltk.download("omw")
# from nltk.corpus import wordnet
# from gensim.models import word2vec




# model = word2vec.Word2Vec.load("word2vec.gensim.model")
hangup = 'その言葉を知ってはいますが知識はないわけであります'
angry = '主語・述語が無い、これはルール違反であり、断固とした処置をとってゆく'

def ape(sentence):
    noun,post,verb = picSPV(sentence)
    if 'None' in  (noun,post,verb):
        if random.choice(range(10)) == 1: return '知らない'
        return angry
    print('ape',noun,post,verb)
    # targetli = compareWords(noun,verb)
    # print(targetli)
    words = findWords(verb)
    print(words)
    length = 0
    foundwords = [w[:w.find('+')] for w in words]
    # for word in words:
    #     w = word[:word.find('+')]
    #     # symli = compareWords(w,verb)
    #     print('w',w)
    #     print('symli',symli)
    #     simlen = simCheck(symli,targetli)
    #     if simlen > length:
    #         length = simlen
    #         foundword = w
    if not foundwords: return hangup
    foundword = random.choice(foundwords)
    print('fo',foundword)
    verb = convertWord(verb)
    if not verb: return hangup
    return f'{noun}{post}{verb}てはいますが{foundword}はしていないわけであります'
    print('found',foundverb)


# def picSV(sentence):
#     t = Tokenizer()
#     s = None
#     p = None
#     V = None
#     for token in t.tokenize(sentence):
#             print(token)
#             if '名詞' in token.part_of_speech: s = token.surface
#             if '助詞' in token.part_of_speech: p = token.surface
#             if '動詞' in token.part_of_speech: v = token.surface
#     if not s or not v: return
#     if not p: p = 'を'
#     return(s,p,v)

def picSPV(sentence):
    morp = nagisa.tagging(sentence)
    words = morp.words
    tags = morp.postags
    s = 'None'
    p = 'None'
    v = 'None'
    for w,t in zip(words,tags):
        print(w,t)
        if '名詞'==t or '代名詞'==t: s = w
        if '助詞'==t: p = w
        if '動詞'==t: v = w
        print(s,p,v)
    if not p: p = 'を'
    return(s,p,v)


def simCheck(list1,list2):
    if not list1 or not list2: return 0
    res = [i for i in list1 if i in list2]
    if not res: return 0
    return len(res)

def findWords(verb):
    words = [i for s in wordnet.synsets(verb,lang='jpn') for i in s.lemma_names('jpn')]
    return [i for i in words if re.search(r'\+',i)]

# def compareWords(word1,word2):
#     try:
#         results = model.wv.most_similar(positive=[word1,word2])
#         return [x for y in results for x in y if type(x)==str]
#     except:
#         return


"""
以下のコードはすべてこちらから転載、一部改変しています
Qiita: @omiita
https://qiita.com/omiita/items/0f811f15e569bf2539b8
"""
def convertWord(word):
    file_name = "verb_utf_8.csv"
    with open(file_name,"r",encoding='utf-8') as f:
        handler = csv.reader(f)
        for row in handler:
            if word == row[10]: #品詞発見
                if "連用タ接続" in row[9]: #活用発見
                    print(row)
                    return row[0]
    return None



if __name__ == '__main__':
    """ settings """
    root = 'C:\\Users\\user\\Dropbox\\git_hub\\Madori-APIs\\Ape-test'
    omw_reader = 'C:\\Users\\user\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\nltk\\corpus\\reader\\wordnet.py'
    filename = 'wnjpn-all.tab'

    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'plan-proxy.json'
    # jwn = JapaneseWordNetCorpusReader(root,omw_reader,filename)
    # print(jwn.synset('é¯–'))
    import os
    os.chdir('C:\\Users\\user\\Dropbox\\git_hub\\Madori-APIs\\Ape-test')
    noun = '酒'
    verb = '飲む'
    sentence = '走る'
    print(ape(sentence))

    # picSV('お酒を飲む')

    # print(findWord(verb))


















    #























#

import curses
from curses.ascii import isdigit
import nltk
from nltk.corpus import cmudict
import nltk.data

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

d = cmudict.dict()

def nsyl(word):
    try:
        out = [len(list(y 
        for y in x if isdigit(y[-1])))
            for x in d[word.lower()]]
    except:
        out = [0]
    finally:
        return out

sylls = 17

pattern = [5, 7, 5]

def findPattern(sentences, pattern):
    ns = 0
    out = []
    for i in sent:
        _pattern = pattern[:]
        maxsyl = _pattern.pop()
        tokens = nltk.word_tokenize(i)
        for j in tokens:
            ns += max(nsyl(j))
            haiku.append(j)
            if ns > maxsyl or len(_pattern) == 0:
                haiku = []
                ns = 0
                break
            elif ns == maxsyl:
                ns = 0
                maxsyl = _pattern.pop()
        ns = 0
        haiku = []
        out.append(haiku)
    return out


f = open('./conv2.txt')
text = f.read()
sent = sent_detector.tokenize(text.strip())
sent = [x.strip() for x in sent[:]]
print len(sent)
# ns = 0
# out = []
# haiku = 0
# for i in sent:
#     tokens = nltk.word_tokenize(i)
#     ns = 0
#     out = []
#     for j in tokens:
#         ns += max(nsyl(j))
#         out.append(j)
#         if ns > sylls:
#             ns = 0
#             out = []
#             break
#     if ns == sylls:
#         haiku += 1
#         print ' '.join(out)
#     ns = 0
#     out = []
# print 'total', haiku


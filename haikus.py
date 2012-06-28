# import curses
try:
    from curses.ascii import isdigit
except:
    import re
    def isdigit(c):
        return re.match(r'[0-9]', c) is not None

import nltk
from nltk.corpus import cmudict
import nltk.data
import logging
import sys

logging.basicConfig(stream=sys.stdout)
log = logging.getLogger("Syllables")
log.setLevel(logging.INFO)

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


# TODO: Make it fucking work!
def findPattern(sentences, pattern):
    ns = 0
    out = []
    haiku = []
    for i in sentences:
        _pattern = pattern[:]
        maxsyl = _pattern.pop()
        tokens = nltk.word_tokenize(i)
        for word in tokens:
            ns += max(nsyl(word))
            haiku.append(word)
            if ns > maxsyl:
                log.info('Overflow %d/%d %s\n%s\n', ns, maxsyl, word, i)
                haiku = []
                ns = 0
                # out = []
                break
            elif ns == maxsyl:
                if len(_pattern) != 0:
                    maxsyl = _pattern.pop()
                else:
                    haiku = []
                    ns = 0
                    # out = []
                ns = 0
                log.info('allmost %d %s\n%s', maxsyl, word, i)
            # elif len(_pattern) == 0:
                # log.info('pattern ends %s\n%s\n', word, i)
                # break
        if haiku != []:
            out.append(' '.join(haiku))
        ns = 0
        haiku = []
    log.info('return')
    return out


# f = open('./conv2.txt')
# text = f.read()
# sent = sent_detector.tokenize(text.strip())
# sent = [x.strip() for x in sent[:]]
# print len(sent)
# haikus = findPattern(sent, pattern)
# haikus2 = findPattern(sent, [17])
# print len(haikus)
# print haikus[0:10]
# print len(haikus2)
# print haikus2[0:10]
print 'found: ', findPattern(
    ['za cava qawa sadafa gajasa rata paca gata'], [6, 3, 9])
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

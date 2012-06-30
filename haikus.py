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
log.setLevel(logging.CRITICAL)

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

d = cmudict.dict()


def nsyl(word):
    try:
        out = [len(list(y
        for y in x if isdigit(y[-1])))
            for x in d[word.lower()]]
    except KeyError:
        out = [0]
    finally:
        return out

sylls = 17

pattern = [5, 7, 5]


# TODO: Make it fucking work!
def findPattern(sentences, pattern):
    ns = 0
    out = []
    for i in sentences:
        log.debug('Processing %s', i)
        tokens = nltk.word_tokenize(i)
        # sylls = map(lambda x: max(nsyl(x)), tokens)
        ns = 0
        maxS = 0
        for j in xrange(len(tokens)):
            word = tokens[j]
            ns += max(nsyl(word.lower()))
            log.debug('Token %s %d/%d', word, ns, pattern[maxS])
            if ns > pattern[maxS]:
                log.debug('Overflow %s %d', word, ns)
                ns = 0
                maxS = 0
                break
            elif ns == pattern[maxS]:
                log.debug('Pattern element matched %s %d', word, ns)
                ns = 0
                maxS += 1
                if maxS == len(pattern):
                    if j < len(tokens):
                        log.debug('Pattern oveflow %s %d', word, ns)
                        ns = 0
                        maxS = 0
                        break
                    else:
                        log.debug('Pattern fully matched %s %d', word, ns)
                        out.append(' '.join(tokens))
                        ns = 0
                        maxS = 0
                        break
    return out

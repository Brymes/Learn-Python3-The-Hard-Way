class Lexicon(object):

    def __init__(self, s):
        self.s = s

    def convert_number(s):
        try:
            return int(s)
        except ValueError:
            return None

    def scan(stuff):
        direction = ['north', 'south', 'east', 'west',
                     'down', 'up', 'left', 'right', 'back']
        verbs = ['go', 'stop', 'kill', 'eat', 'smack', 'open',]
        stop_words = ['the', 'in', 'of', 'from', 'at', 'it']
        nouns = ['door', 'bear', 'princess', 'cabinet', 'nose']

        words = list(stuff.split())
        words_i = ["Word %d" % x for x in range(len(words))]

        sentence = []
        start = 0
        for index in range(len(words)):
            if words[index] in direction:
                words_i[start] = ('direction', str(words[index]))
            elif words[index] in verbs:
                words_i[start] = ('verb', str(words[index]))
            elif words[index] in stop_words:
                words_i[start] = ('stop', str(words[index]))
            elif words[index] in nouns:
                words_i[start] = ('noun', str(words[index]))
            elif Lexicon.convert_number(words[index]) != None:
                words_i[start] = ('number', int(words[index]))
            else:
                words_i[start] = ('error', str(words[index]))
            sentence.append(words_i[start])
            start += 1
        return sentence

# to catch camel case use a list of letters in words in the lexicon
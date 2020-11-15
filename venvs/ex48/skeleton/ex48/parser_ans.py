class ParseError(Exception):
    pass

class Sentence(object):

    def __init__(self, subject, verb, obj):
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

    def peek(word_list):
        if word_list:
            word = word_list[0]
            return word[0]
        else:
            return None

    def match(word_list, expecting):
        if word_list:
            word = word_list.pop(0)

            if word[0] == expecting:
                return word
            else:
                return None
        else:
            return None

    def skip(word_list, word_type):
        while Sentence.peek(word_list) == word_type:
            #temp = Sentence.peek(word_list)
            Sentence.match(word_list, word_type)#temp)

    def parse_verb(word_list):
        Sentence.skip(word_list, 'stop')

        if Sentence.peek(word_list) =='verb':
            return Sentence.match(word_list, 'verb')
        else:
            raise ParseError("Expected a verb next.")

    def parse_object(word_list):
        Sentence.skip(word_list, 'stop')
        next_word = Sentence.peek(word_list)

        if next_word == 'noun':
            return Sentence.match(word_list, 'noun')
        elif next_word == 'direction':
            return Sentence.match(word_list, 'direction')
        else:
            raise ParseError("Expected a noun or direction next.")

    def parse_subject(word_list):
        Sentence.skip(word_list, 'stop')
        next_word = Sentence.peek(word_list)

        if next_word == 'noun':
            return Sentence.match(word_list, 'noun')
        elif next_word == 'verb':
            return('noun', 'player')
        else:
            raise ParseError('Expected a verb next.')

    def parse_sentence(word_list):
        subj = Sentence.parse_subject(word_list)
        verb = Sentence.parse_verb(word_list)
        obj = Sentence.parse_object(word_list)

        return Sentence(subj, verb, obj)


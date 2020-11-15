import lexicon

class Sentence(object):

    text = "open the door and smack the bear in the nose"
    word_list = lexicon.Lexicon.scan(text)
    def peek(word_list):
        Interpretation = {}

        for index in range(len(Sentence)):
            tup = Sentence[index]
            start = 1

            if 'noun' in Sentence[index]:
                Interpretation['Subject'] = str(tup[start])
            elif 'verb' in Sentence[index]:
                Interpretation['Verb'] = str(tup[start])
            elif 'direction' in Sentence[index]:
                Interpretation['Object'] = str(tup[start])
            else:
                pass
            print(Interpretation)


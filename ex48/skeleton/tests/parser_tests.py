from nose.tools import *
from ex48.parser_ans import Sentence, ParseError

def test_peek():
    assert_equal(Sentence.peek([('verb', 'eat')]), 'verb')
    assert_equal(Sentence.peek([('noun', 'bear')]), 'noun')

def test_match():
    test = Sentence.match([('verb', 'eat')], 'verb')
    assert_equal(test, ('verb', 'eat'))
    test2 = Sentence.match([('noun', 'bear')], 'verb')
    assert_equal(test2, None)

def test_skip():
    #test = Sentence.skip([('noun', 'bear'), ('stop', 'the')], 'stop')
    #assert_equal(test, ('noun', 'bear'))
    pass

def test_parse_verb():
    test = Sentence.parse_verb([('noun', 'bear'), ('stop', 'the')])
    assert_raises(ParseError, )
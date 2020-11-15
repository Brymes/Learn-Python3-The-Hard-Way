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
    test = Sentence.parse_verb([('verb', 'eat')])
    assert_equal(test, ('verb', 'eat'))
    assert_raises(ParseError, Sentence.parse_verb, [('noun', 'bear')])


def test_parse_object():
    test = Sentence.parse_object([('noun', 'bear')])
    assert_equal(test, ('noun', 'bear'))
    test2 = Sentence.parse_object([('direction', 'north')])
    assert_equal(test2, ('direction', 'north'))
    assert_raises(ParseError, Sentence.parse_object, [('verb', 'bear')])


def test_parse_subject():
    test = Sentence.parse_subject([('noun', 'bear')])
    test2 = Sentence.parse_subject([('verb', 'kill')])
    assert_equal(test, ('noun', 'bear'))
    assert_equal(test2, ('noun', 'player'))
    assert_raises(ParseError, Sentence.parse_subject, [('direction', 'bear')])


def parse_sentence():
    test = parse_sentence([('verb', 'open'), ('stop', 'the'), ('noun', 'door'), ('error', 'and'), (
        'verb', 'smack'), ('stop', 'the'), ('noun', 'bear'), ('stop', 'in'), ('stop', 'the'), ('noun', 'nose')])
    assert_equal(test.subject, 'player')
    assert_equal(test.object, 'door')
    assert_equal(test.verb, 'open')

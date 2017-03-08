#!/usr/bin/env python2
# Copyright (c) 2017 Ivan J. <parazyd@dyne.org

import nltk
import re
import twokenize
from nltk.tag.perceptron import PerceptronTagger

def tokenizelocal():
    tweets = tweetFile.read().splitlines()
    for t in tweets:
        print(t + '\n')
        print(str(twokenize.tokenize(t)) + '\n')

def format_tweet(message):
    m = str(message)
    m = m.replace('\n', ' ')
    m = m.encode('ascii', 'ignore')
    return m

def format_tagged(tagged_list):
    out = ''
    for t in tagged_list:
        token, tag = postprocess_tag(t[0], t[1])
        out = out + token + '/' + tag + '/'
    out = out + '\n'
    return out

def postprocess_tag(token, tag):
    outtag = tag
    if (is_twitter_cf_modal(token)):
        outtag = 'MD'
    elif (tag_CCJ(token)):
        outtag = 'CCJ'
    return token, outtag

def get_cf_form(tagged_message):

    # Filter out questions
    pq = re.compile('\.*/\?/.', re.IGNORECASE)
    if pq.search(tagged_message) != None:
        return 0

    # CASE 1 WISH VERB FORM
    p1 = re.compile('\.*(wish|wishing)/((VB.*/)|(JJ/))', re.IGNORECASE)
    if p1.search(tagged_message) != None:
        return 1


    # CASE 2 CONJUNTION NORMAL
    p2 = re.compile('\.*/CCJ/.*((/VBD/)|(/VBN/)).*/MD/', re.IGNORECASE)
    if p2.search(tagged_message) != None:
        return 2


    # CASE 3 CONJUNCTIVE CONVERSE
    p3 = re.compile('\.*/MD/.*/CCJ/.*((/VBN/)|(/VBD/))', re.IGNORECASE)
    if p3.search(tagged_message) != None:
        return 3


    # CASE 5 Should have
    p4 = re.compile('\.*/((should\'ve)/MD/)|(((should)|(shoulda)(shulda)|(shuda)|(shudda)|(shudve))/MD/((have)|(hve)|(ve))/)(\w)*((/VBN/)|(/VBD/))', re.IGNORECASE)
    if p4.search(tagged_message) != None:
        return 4

    # CASE 6 VERB INVERSION
    p5 = re.compile(("\.*(had/(\w)*/(\w)*((/NN/)|(/NNP/)|(/NNPS/)|(/NNS/)|(/PRP/)).*((/VBN/)|(/VBD/)).*/MD/)"
                    "|(were/(\w)*/(\w)*((/NN/)|(/NNP/)|(/NNPS/)|(/NNS/)|(/PRP/)).*/MD/)"
                    "|(/MD/.*/VB.*/had/(\w)*/(\w)*((/NN/)|(/NNP/)|(/NNPS/)|(/NNS/)|(/PRP/)).*((/VBN/)|(/VBD/)))"), re.IGNORECASE)
    if p5.search(tagged_message) != None:
        return 5


    # CASE 6 MODAL NORMAL
    p6 = re.compile('\.*/MD/.*((/VBN/)|(/VBD/)).*/MD/.*((/VBN/)|(/VBD/)|(/VB/)|(VBZ))', re.IGNORECASE)
    if p6.search(tagged_message) != None:
        return 6

    # If no matches
    return 0


def is_twitter_cf_modal(word):
    w = unicode(word, errors='ignore').encode('utf-8').lower()
    if (w == 'should' or
        w == 'should\'ve' or
        w == 'shouldve' or
        w == 'shoulda' or
        w == 'shulda' or
        w == 'shuda' or
        w == 'shudda' or
        w == 'shudve' or
        w == 'would' or
        w == 'would\'ve' or
        w == 'wouldve' or
        w == 'woulda' or
        w == 'wuda' or
        w == 'wulda' or
        w == 'wudda' or
        w == 'wudve' or
        w == 'wlda' or
        w == 'could' or
        w == 'could\'ve' or
        w == 'couldve' or
        w == 'coulda' or
        w == 'cudda' or
        w == 'culda' or
        w == 'cudve' or
        w == 'must' or
        w == 'mustve' or
        w == 'might' or
        w == 'might\'ve' or
        w == 'mightve' or
        w == 'ought' or
        w == 'may' or
        w == 'i\'d' or
        w == 'id' or
        w == 'we\'d' or
        w == 'youd' or
        w == 'you\'d' or
        w == 'he\'d' or
        w == 'she\'d'):
            return True
    return False

def tag_CCJ(word):
    w = word.lower()
    '''
    as long as, even if, if, one condition that, provided (that),
    providing (that), so long as, unless, whether... or, supposing,
    suppose, imagine, but for
    '''
    if(w == 'as' or
        w == 'if' or
        w == 'even' or
        w == 'provided' or
        w == 'providing' or
        w == 'suppose' or
        w == 'supposing' or
        w == 'unless' or
        w == 'whether' or
        w == 'envision' or
        w == 'envisioning' or
        w == 'conceptualize'or
        w == 'conceptualizing' or
        w == 'conjure' or
        w == 'conjuring' or
        w == 'visualize' or
        w == 'visualizing'):
        return True
    return False

def get_tagged_message(message, tagger):
    tagset = None
    formatted_message = format_tweet(message)
    tokens = twokenize.tokenize(formatted_message)
    tags = nltk.tag._pos_tag(tokens, tagset, tagger)
    return format_tagged(tags)

def classify(tweetfile, taggedfile):
    tweetfile  = open(tweetfile,  "r")
    taggedfile = open(taggedfile, "w")
    counterfactuals = open('counterfactuals.txt', 'w')

    tagger = PerceptronTagger()
    form_num = 8

    cf_count = [[0 for x in range(form_num)] for x in range(form_num)]

    form_vec = []

    print("Reading file...")
    tweet = tweetfile.readline()

    while tweet:
        taggedTweet = get_tagged_message(tweet, tagger)
        taggedfile.write(taggedTweet)
        form = int(get_cf_form(taggedTweet))

        if form:
            print(tweet)
            counterfactuals.write(tweet + '<hr>\n')

        form_vec.append(form)
        cf_count[form][0] += 1
        tweet = tweetfile.readline()

    count = 0
    for i in xrange(1, form_num):
        count += cf_count[i][0]

    print("Finished tagging...")
    tweetfile.close()
    taggedfile.close()

    print("counterfactuals: " + str(count) + "/100")
    counterfactuals.write("counterfactuals: " + str(count) + "/100<br>\n")
    counterfactuals.close()

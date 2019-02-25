#!/usr/bin/env python
import sys
import random
import argparse
from numpy.random import choice


#Remember to run chmod +x myscript.py in the cmd line before trying ./randsent

prob_rules = {}
LHS = {}
RHS = {}
NONTERMINAL_LIMIT = 440
nonterminal_values = 1
depth = 1
end = False

def generateTree(rules, nonterminals, symbol='ROOT', iterations='1'):
    #Generate a random sentence from the grammar, starting with the given symbol.
    sentence = ''
    depth = iterations
    global nonterminal_values
    normalize_prob = [float(i) for i in prob_rules[symbol]]
    normalize_prob = [i/float(sum(normalize_prob)) for i in normalize_prob]
    # select one production of this symbol randomly

    rhs = choice(rules[symbol], 1, p=normalize_prob)[0].split()

    for sym in rhs:
        if sym in rules:
            if sym in LHS:
                nonterminal_values += 1
            if nonterminal_values <= NONTERMINAL_LIMIT:
                sentence += '(' + sym + ' '           
                sentence += generateTree(rules, nonterminals, sym, depth)
                sentence += ')' + ' '
            else:
                sentence += '...'
        else:
            if sym in RHS:
                sentence += sym
            if sym not in RHS:
                sentence += sym + ' '
    return sentence

def generate(rules, nonterminals, symbol='ROOT'):
    #Generate a random sentence from the grammar, starting with the given symbol.
    sentence = ''
    global nonterminal_values
    global end
    normalize_prob = [float(i) for i in prob_rules[symbol]]

    normalize_prob = [i/float(sum(normalize_prob)) for i in normalize_prob]

        # select one production of this symbol randomly
    rhs = choice(rules[symbol], 1, p=normalize_prob)[0].split()

    for sym in rhs:
        if sym in LHS:
            nonterminal_values += 1
        if sym in rules:
            if nonterminal_values <= NONTERMINAL_LIMIT:
                sentence += generate(rules, nonterminals, sym)
            else:
                if end == False:
                    sentence += '...'
                    end = True
        else:
            sentence += sym + '  '
    return sentence

def main(argv):

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--tree", help="See the sentence in a syntactic tree", action="store_true")
    parser.add_argument('filename')
    parser.add_argument("sentence", type=int, help="number of sentences to print")
    args = parser.parse_args()

    numSentence = args.sentence
	
    with open(args.filename) as myfile:
        grammar = myfile.readlines()
    grams = []

    for line in grammar:
        if not line.startswith('#') and line.strip():
            line = line.split('#')[0].strip().split('\t')
            grams.append(line)

    global LHS
    global RHS
    prob = [x[0] for x in grams] 
    LHS = [x[1] for x in grams]
    RHS = [x[2] for x in grams]

    rules = {}

    for lhs in set(LHS):
    	rules[lhs] = tuple([RHS[i] for i in range(len(LHS)) if LHS[i] ==lhs])

    for lhs in set(LHS):
        prob_rules[lhs] = list([prob[i] for i in range(len(LHS)) if LHS[i] ==lhs])
    global nonterminal_values
    if args.tree:
        for x in range(numSentence):
            nonterminal_values = 1
            print("(ROOT " + generateTree(rules, nonterminal_values, 'ROOT', 1) + ")")
    else:
        for x in range(numSentence):
            nonterminal_values = 1
            print(generate(rules, nonterminal_values, 'ROOT'))


if __name__ == "__main__":
    main(sys.argv)

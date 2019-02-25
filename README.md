Example Usage:

```
./sentgen grammar.gr 1
```

where the first input is the name of the grammar file and the second input is the number of sentences to generate.

This is a sentence generator that can take in the rules of a grammar file to create "grammatical" sentences. The rules that it uses is based on whether or not a nonterminal is existent at that point and on the probability of the rule being used. Special additions to the grammar include the following:

a) relative clauses
b) "I wonder" clauses
c) adverbial clauses (ex. Sally sighed when the president ate sandwich)
d) object possession with multiple adjectives (ex. the chief of staff’s perplexed fine sandwich)
e) particular order of adjectives: when describing some- thing with more than one adjective, you arrange the adjectives in a specific order (quality, size, age, shape, color).

import spacy
nlp = spacy.load('en_core_web_md')
# nlp = spacy.load('en_core_web_sm')

# === similarity === #
print('\n-- SIMILARITY: --\n')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
word4 = nlp("chicken")

# output similarities between each word
print(f'cat and monkey: {word1.similarity(word2)}')  # compare cat and monkey
print(f'banana and monkey: {word3.similarity(word2)}')  # compare banana and monkey
print(f'chicken and monkey: {word4.similarity(word2)}\n')  # compare chicken and monkey

print(f'cat and banana: {word1.similarity(word3)}')  # compare banana and cat
print(f'chicken and banana: {word4.similarity(word3)}\n')  # compare banana and chicken

print(f'cat and chicken: {word1.similarity(word4)}')  # compare cat and chicken

print(f'cat and cat: {word1.similarity(word1)}\n')  # compare cat to itself

# NOTE 1
'''
    What is outputted, is a decimal value less than one - acting as a fraction of how similar the two
    entities/words are. When a word is matched with itself, the similarity value equals 1.0. 
    
    With sentences
'''

# NOTE 2: en_core_web_sm
'''
   This simpler language model outputs similarities however it comes with the warning that the language model
   has no word vectors loaded, so the result of the doc.similarity method is based on the tagger, parser and 
   NER. This may not give useful similarity judgements. This happens when using one of the small models such as 
   'en_core_web_sm' which doesn't ship with word vectors and only uses context-sensitive tensors. The warning also 
   states that I can add my own word vectors, or use a larger model instead.
'''


# === working with vectors === #
print('\n-- WORKING WITH VECTORS: --\n')
tokens = nlp('cat apple monkey banana ')

# output the token pairings with their similarity values
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
    print('\n')

# === working with sentences === #
print('\n-- WORKING WITH SENTENCES: --\n')

# string of model sentence - nlp still needs to be applied
sentence_to_compare = "Why is my cat on the car"

# list of sample sentences
sentences = ["where did my car go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my god Diana"]

model_sentence = nlp(sentence_to_compare)

# compare sentences to model sentence
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(f'{sentence} - {similarity}')



# NOTE 1
'''
    What is outputted, is a decimal value less than one - acting as a fraction of how similar the two
    entities/words are. When a word is matched with itself, the similarity value equals 1.0. 
    With this more complex model, a subject/entity in different parts of speech can still be identified.
    For example, I and my and me, are lemmatized to increase the similarity between the two sentences because they
    are referring to the same subject/entity. 
'''

# NOTE 2: en_core_web_sm
'''
   This simpler language model outputs similarities however it comes with the warning that the language model
   has no word vectors loaded, so the result of the doc.similarity method is based on the tagger, parser and 
   NER. This may not give useful similarity judgements. This happens when using one of the small models such as 
   'en_core_web_sm' which doesn't ship with word vectors and only uses context-sensitive tensors. The warning also 
   states that I can add my own word vectors, or use a larger model instead.
'''
# end

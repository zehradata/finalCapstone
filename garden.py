import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# List of garden path sentences
gardenpathSentences = [
    "The old man the boats.",
    "The horse raced past the barn fell."
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

# Tokenize and perform named entity recognition for each sentence
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print("Sentence:", sentence)
    for token in doc:
        print("Token:", token.text, ", POS:", token.pos_, ", Entity:", token.ent_type_)
    print("\n")

# Lookup and print explanations for entities
print("Entity explanations:")
print(spacy.explain("FAC"))  # Facility
print(spacy.explain("NORP"))  # Nationalities or religious or political groups

# Comment about the looked up entities:
# 1. Entity: FAC (Facility)
#    Explanation: Refers to buildings, airports, highways, bridges, etc.
#    Did it make sense: Yes, it is a broad category that encompasses various structures and locations.
#
# 2. Entity: NORP (Nationalities or religious or political groups)
#    Explanation: Refers to names of political, religious, or ethnic groups.
#    Did it make sense: Yes, it represents a wide range of groups related to nationality, religion, or politics.



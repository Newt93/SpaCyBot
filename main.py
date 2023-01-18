import spacy
from spacy.matcher import Matcher

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Initialize the Matcher
matcher = Matcher(nlp.vocab)

# Define the pattern to match
pattern = [{"LOWER": "hello"}, {"IS_PUNCT": True}, {"LOWER": "world"}]

# Add the pattern to the matcher
matcher.add("HELLO_WORLD", None, pattern)

# Define the function to respond to a match
def respond_to_hello_world(doc):
    print("Hello, world!")

# Register the callback to the matcher
matcher.add_entity("HELLO_WORLD", on_match=respond_to_hello_world)

# Process the text
doc = nlp("Hello, world!")
matcher(doc)

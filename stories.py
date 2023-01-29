"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, code, title, words, text):
        """Create story with words and template text."""

        self.code = code
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story("0", "Farm",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a far away {place}, there {adjective} a
       large {noun}. It loved to {verb} {plural_noun}."""
)

story1 = Story("1", "Bus",
    ["location", "noun", "verb", "adjective"], 
    """A long time ago in a galaxy far far away... \n
    There once was a {noun}, on the planet {location} \n
    it was thought to {adjective} a {verb} from time to time.
    """
)
story2 = Story("2", "Fortnite",
    ["console", "character", "verb", "weapon", "boss"], 
    """Only pros play on {console},  as {character}. There once was a {character}, but he  {verb} with his {weapon} to fight against the {boss}"""
)

story3 = Story("3", "Take a Trip", ["location", "location1", "adjective", "plural_noun", "noun", "emotion"], """
On our way to the {location} we stopped at {location1}. There we saw {adjective}{plural_noun} and a {noun}. Unfortunately they were super {emotion}, so it was an interesting experience if I do say so myself.
""")

#?dictionary = {key: expression for (key, value) in iterable}
# TODO to create and add stories to dictionary will need to adjust the below to automate adding to the dictionary when created. 
# TODO as of now creating a story will require manually typing above and then adding to the below list within the dictionary comprehension
stories = {s.code: s for s in [story, story1, story2, story3]}
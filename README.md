# AnagramPy

AnagramPy is a basic anagram game made with Python. The user's objective is to search for possible words based on the displayed letters.

The game has the following "rules":
  - You can only miss 5 times, otherwise the game will end
  - The anagram is shuffled everytime you miss or find a word
  - The word database won't consider words with special characters, so avoid using it

AnagramPy makes use of DatamuseAPI's query engine. For more information about privacy, usage limit and sources, refer to: https://www.datamuse.com/api/.

## Getting Started

### Starting the game

First you'll need to clone the repository and access the project's directory:
```bash
git clone https://github.com/0SvanZz1/AnagramPy.git
cd AnagramPy/
```

Then, to start the game, you should execute the `anagram.py` file using Python as follows:
```bash
python3 anagram.py Topic MaxNumberOfWords
```

Where `Topic` is the theme of the anagram (should be of type `String`), and `MaxNumberOfWords` is the maximum number of words for the anagram (should be of type `Int`).

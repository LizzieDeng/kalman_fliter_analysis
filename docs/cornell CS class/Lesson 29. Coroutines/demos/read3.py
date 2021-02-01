"""
A module to show off a long-running function as a coroutine.

In this module, we use a yield expression to give the
coroutine a time budget. After the time budget is up,
it has to yield to give us an update.  We will see why
this is useful later.

Author: Walker M. White
Date:   November 2, 2020
"""
import time
import random


def add_word(word,counts):
    """
    Adds a word to a word-count dictionary.

    The keys of the dictionaries are strings, and the values
    are integers. If the word is already in the dictionary,
    adding it will increase the value by 1.  Otherwise it
    will add the key and assign it a value for 1.

    Example: If count = ['a':1,'b':1}, add_word('a',count)
    alters count to be {'a':2,'b':1}

    Parameter word: The word to add
    Precondition: word is a string

    Parameter counts: The word-count dictionary
    Precondition: count is a dictionary with string keys
    and integer values
    """
    if word in counts:
        counts[word] = counts[word]+1
    else:
        counts[word] = 1


def wordcount(fname):
    """
    Returns a dictionary with the individual word count of
    fname

    The is function opens the specified text file and
    creates a dictionary from it.  The keys of the
    dictionaries are words (i.e. adjacent letters with no
    spaces or punctuation). For example, in the string
    'Who are you?', the words are 'Who', 'are', and 'you'.
    The values are the number of times that word (paying
    attention to capitalization) appears in the file.

    This function is a coroutine that is periodically
    given a "time budget".  It uses the the time module
    to count the number of seconds that have passed and
    pauses the loop (with a yield) once the time budget
    it up.

    Parameter fname: The file name
    Precondition: fname is a string and the name of a text
    file
    """
    # Load the entire file into a single string
    file = open(fname)
    text = file.read()
    file.close()

    counts = {}
    word = ''           # Accumulator to build a word

    # Get the initial budget and start the timer
    budget = (yield)
    start = time.time()

    for pos in range(len(text)):
        # See if we have taken too long
        end = time.time()
        if end-start > budget:
            progress = round(100*pos/len(text))
            budget = (yield progress)   # Notify the parent of our progress (and get new budget)
            start = time.time()         # Reset the timer for the new budget

        # Build up the word, one letter at a time
        x = text[pos]
        if x.isalpha():
            word = word+x
        else:           # Word ends
            # Add it if not empty
            if word != '':
                add_word(word,counts)
            word = ''   # Reset the accumulator

    # Add the last word
    if word != '':
        add_word(word,counts)
    return counts


def loadfile(fname):
    """
    Creates a word-count dictionary for fname and prints
    its size

    The size of the word-count dictionary is the number of
    distinct words in the file.

    This function is the parent of wordcount, pushing it
    forward with the next() function until it is done
    reading the file.

    Parameter fname: The file name
    Precondition: fname is a string and the name of a text
    file
    """
    loader = wordcount(fname)
    result = None

    # Start the loader
    next(loader)

    # We keep going as long as the loader has more for us
    while not loader is None:
        try:
            # Pick a random time in seconds
            budget = 0.5 #random.uniform(0.5,1)

            # Allow the file to load for that many seconds
            amount = loader.send(budget)
            print('Loaded '+str(amount)+'% of '+repr(fname))
        except StopIteration as e:
            result = e.args[0]      # Access the return value
            loader = None           # We are done

    print('Read a total of '+str(len(result))+' words.')


if __name__ == '__main__':
    loadfile('warpeace10.txt')

"""
A module to show off a long-running function as a coroutine.

This module shows another advantage of a coroutine. We can
interleave two functions as they load from a file. There are
reasons we might want to do this when working with large data,
but they are beyond the scope of this course.

Author: Walker M. White
Date:   November 2, 2020
"""


def merge(dict1,dict2):
    """
    Returns a new dictionary merging (joining keys) dict1
    and dict2.

    If a key appears in only one of dict1 or dict2, the
    value is the value from that dictionary. If it is in
    both, the value is the sum of values.

    Example: merge({'a':1,'b':2},{'b':3,'c':4}) returns
    {'a':1,'b':5,'c':4}

    Parameter dict1: The first dictionary to merge
    Precondition: dict1 a dictionary with int or float values

    Parameter dict2: The second dictionary to merge
    Precondition: dict2 a dictionary with int or float values
    """
    result = dict(dict1) # Makes a (shallow) copy
    for k in dict2:
        if k in dict1:
            result[k] = result[k]+1
        else:
            result[k] = 1
    return result


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

    The is function opens the specified text file and creates
    a dictionary from it.  The keys of the dictionaries are
    words (i.e. adjacent letters with no spaces or
    punctuation). For example, in the string 'Who are you?',
    the words are 'Who', 'are', and 'you'.  The values are
    the number of times that word (paying attention to
    capitalization) appears in the file.

    This function is a generator-based coroutine that stops
    at every 10% of the file to return its amount of progress
    to the original caller (the function that calls next()).

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
    for pos in range(len(text)):
        # Yield every 10%
        if pos % (len(text)//10) == 0:
            # Indicate the amount of progress we made
            yield round(100*pos/len(text))

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


def loadfiles(fname1,fname2):
    """
    Creates a word-count dictionary for fname1, fname2 and
    prints the combined size

    The size of the word-count dictionary is the number of
    distinct words in the file.

    This function is the parent of wordcount, pushing it
    forward with the next() function until it is done
    reading the file. This function creates two wordcount
    coroutines and interleaves them.

    Parameter fname1: The first file name
    Precondition: fname1 is a string and the name of a text file

    Parameter fname2: The second file name
    Precondition: fname2 is a string and the name of a text file
    """
    loader1 = wordcount(fname1)
    loader2 = wordcount(fname2)

    result = {}

    # We keep going as long as either loader is working
    while (not loader1 is None) or (not loader2 is None):

        # Load the next batch from fname1
        if not loader1 is None:
            try:
                amount = next(loader1)
                print('Loaded '+str(amount)+'% of '+repr(fname1))
            except StopIteration as e:
                result = merge(result,e.args[0])    # Access the return value
                loader1 = None                      # We are done

        # Load the next batch from fname2
        if not loader2 is None:
            try:
                amount = next(loader2)
                print('Loaded '+str(amount)+'% of '+repr(fname2))
            except StopIteration as e:
                result = merge(result,e.args[0])    # Access the return value
                loader2 = None                      # We are done

    print('Read a total of '+str(len(result))+' words.')


if __name__ == '__main__':
    loadfiles('warpeace10.txt','kingjames10.txt')

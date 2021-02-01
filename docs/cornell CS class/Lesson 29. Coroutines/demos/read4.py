"""
A module to show off a long-running function as a NATIVE coroutine.

Native Python coroutines require the asyncio module. They are
actually weaker than generator based coroutines (so we will not
use them). They do not use yield (neither the statement not the
expression) and cannot easily pass data back and forth.

Their primary advantage is that they cut down the code that you
have to write in order to use the coroutines.  You do not need
to create an explicit loops that calls next until done.  However,
these native coroutines must be procedures and cannot return a
value.

Author: Walker M. White
Date:   November 2, 2020
"""
import asyncio


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

    The keys of the dictionaries are strings, and the values are
    integers. If the word is already in the dictionary,
    adding it will increase the value by 1.  Otherwise it
    will add the key and assign it a value for 1.

    Example: If count = ['a':1,'b':1}, add_word('a',count)
    alters count to be {'a':2,'b':1}

    Parameter word: The word to add
    Precondition: word is a string

    Parameter counts: The word-count dictionary
    Precondition: count is a dictionary with string keys and integer values
    """
    if word in counts:
        counts[word] = counts[word]+1
    else:
        counts[word] = 1


# The async at the front makes this a native coroutine
async def wordcount(fname,result):
    """
    Modifies result to contain the word count of fname

    The is function opens the specified text file and stores
    is wordcount in result.  The keys of the dictionary are
    words (i.e. adjacent letters with no spaces or punctuation).
    For example, in the string 'Who are you?', the words
    are 'Who', 'are', and 'you'.  The values are the number
    of times that word (paying attention to capitalization)
    appears in the file.

    This function is a native coroutine.  It periodically
    calls await to release control and allow another
    coroutine a chance.

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
        if pos % (len(text)//10) == 0:
            progress = round(100*pos/len(text))

            # We cannot pass this back, so we just print it out
            print('Loaded '+str(progress)+'% of '+repr(fname))

             # This acts partly like a yield, giving up time
            await asyncio.sleep(1)


        # Build up the word, one letter at a time
        x = text[pos]
        if x.isalpha():
            word = word+x
        else:           # Word ends
            # Add it if not empty
            if word != '':
                add_word(word,result)
            word = ''   # Reset the accumulator

    # Add the last word
    if word != '':
        add_word(word,result)

    # Native coroutines converted to tasks MUST be procedures


async def loadfiles(fname1,fname2):
    """
    Creates a word-count dictionary for fname1, fname2 and prints
    the combined size

    The size of the word-count dictionary is the number of distinct
    words in the file.

    This function is the parent of wordcount, launching it as a task
    and awaiting its result.

    Parameter fname1: The first file name
    Precondition: fname1 is a string and the name of a text file

    Parameter fname2: The second file name
    Precondition: fname2 is a string and the name of a text file
    """
    # Create the tasks for the coroutines
    result1 = {}
    loader1 = asyncio.create_task(wordcount(fname1,result1))
    result2 = {}
    loader2 = asyncio.create_task(wordcount(fname2,result2))

    # Let them take over
    await loader1
    await loader2

    result = merge(result1,result2)
    print('Read a total of '+str(len(result))+' words.')


if __name__ == '__main__':
    asyncio.run(loadfiles('warpeace10.txt','kingjames10.txt'))

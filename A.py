import doctest

def concat(*words, sep=" "):
    """Return a sentence from input words
    separated by a separator(default being space)
    
    >>> concat('a','b','c', 'd')
    'a b c d'
    >>> concat('a','1')
    'b 1'
    
    """
    return sep.join(words)

doctest.testmod()

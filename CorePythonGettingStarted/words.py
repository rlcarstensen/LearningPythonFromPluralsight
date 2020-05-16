""" [summary]

Returns:
    [type]: [description]
"""

import sys
from urllib.request import urlopen
# url is 'http://sixty-north.com/c/t.txt'

def fetch_words(url):
    """Fetch a list of words from a URL.

    Args:
      url: The URL of a UTF-8 text document.

    Returns:
      A list or strings containing the words from the document.
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

def print_items(items):
    """print_items prints items in collection
    
    Args:
        items (collection): collection of items.
    """
    for word in items:
        print(word)

def main(url): 
    words = fetch_words(url)
    print_items(words)

if __name__ == '__main__':
    main(sys.argv[1])
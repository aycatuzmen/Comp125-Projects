
PUNCTUATION = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
def delete_punctuation(s):
    """
    Removes given characters from a string and returns the string.
    Function should work for words containing both upper and
    lowercase letters. The character string will always be lowercase.
    Input:
        s (string): string from which to remove characters

    Returns:
        removed_string (string): string with characters removed

    >>> delete_punctuation('I **hate** punctuation!!!!')
    'I hate punctuation'
    """
    result = ''
    for char in s:
        if char.lower() not in PUNCTUATION:
            result += char
    return result

def word_count_using_list():
    """
    This function uses lists to count words
    """
    word_list = []
    count_list = []

    # Write your code below
    pass


def word_count_using_dict():
    """
    This function uses dictionary to count words
    """
    # Write your code below
    pass


def main():
    #word_count_using_list()
    word_count_using_dict()

if __name__ == '__main__':
    main()
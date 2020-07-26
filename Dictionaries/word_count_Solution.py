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
    with open("tongue_twister.txt", 'r') as f:
        line = f.readline()
        while line:
            line = line.strip()
            words = delete_punctuation(line).split()
            for w in words:
                w = w.lower()
                if not w.isalpha():
                    w = w[:-1]
                if w not in word_list:
                    word_list.append(w)
                    count_list.append(1)
                else:
                    idx = word_list.index(w)
                    count_list[idx] += 1
            line = f.readline()
    print(word_list)
    print(count_list)

def word_count_using_dict():
    """
    This function uses dictionary to count words
    """
    counts = {}
    with open('tongue_twister.txt', 'r') as f:
        for line in f:
            words = delete_punctuation(line).split()
            for word in words:
                if word not in counts:
                    counts[word] = 0
                counts[word] += 1

        return counts

def main():
    word_count_using_list()
    #print(word_count_using_dict())

if __name__ == '__main__':
    main()
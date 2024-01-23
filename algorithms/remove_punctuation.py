import re

def remove_punctuation(text: str) -> str:
    """
    Remove punctuation from text
    :param text: text to remove punctuation from
    :return: text without punctuation
    """
    return re.sub(r'[^\w\s]', '', text)

def main():
    text = "`H.e,l'lo;, w:o^rld!"
    print(remove_punctuation(text))

if __name__ == "__main__":
    main()
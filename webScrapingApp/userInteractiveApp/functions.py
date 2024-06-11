import re


def extract_number(text):
    match = re.search(r'\d+', text)
    if match:
        return int(match.group())
    else:
        return None


def shorten_title(original_title):

    words = original_title.split()

    shortened_title = ' '.join(words[:4])

    return shortened_title

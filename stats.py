def count_words(text):
    word_list= text.split()
    word_count =len(word_list)
    return word_count
# Function that counts words -----------------------------------


def get_characters(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] =1
    return chars
# Function that counts lower case get_characters----------------


def char_dict(char_counts):
    chars = []
    for key, value in char_counts.items():
        items={"char":key, "num":value }
        chars.append(items)

    chars.sort(key=lambda item: item["num"], reverse=True)
    return chars

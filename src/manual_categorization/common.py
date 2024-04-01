import re


def determine_category(description, category_words):
    if not isinstance(description, str): 
        return ""

    lower_description = description.lower()

    for cat in category_words: 
        filters = cat.filters

        if bool(filters):
            filter_match = any(re.search(rf'{re.escape(word)}', lower_description) for word in filters)
        else:
            filter_match = False

        if filter_match:
            continue

        words_and = cat.words_and
        like_and = cat.like_and

        if bool(words_and):
            words_and_match = all(
                re.search(rf'\b{re.escape(word)}\b', lower_description)
                for word in words_and)
        else:
            words_and_match = True

        if not words_and_match:
            continue

        if bool(like_and):
            like_and_match = all(
                re.search(rf'{re.escape(word)}', lower_description) for word in like_and
            )
        else:
            like_and_match = True

        if not like_and_match:
            continue

        words_or = cat.words_or
        like_or = cat.like_or

        has_words_or = bool(words_or)
        has_like_or = bool(like_or)

        name = cat.name
        if not has_words_or and not has_like_or:
            return name

        if has_words_or:
            words_or_match = any(
                re.search(rf'\b{re.escape(word)}\b', lower_description)
                for word in words_or
            )

        if has_like_or:
            like_or_match = any(
                re.search(rf'{re.escape(word)}', lower_description) for word in like_or
            )

        if has_words_or and has_like_or and like_or_match and words_or_match:
            return name
        elif has_words_or and words_or_match and not has_like_or: 
            return name
        elif has_like_or and like_or_match and not has_words_or:
            return name
        
    return  ""


def determine_scope(part_number, in_scope):
    if not isinstance(part_number, str): 
        return "Out of Scope"
    
    part_number_text = str(part_number)
    
    if any(value.lstrip('0') == part_number_text.lstrip('0') for value in in_scope):
        return "In Scope"
    else:
        return  "Out of Scope"
    

def find_scope_match(in_scope, description, words):
    if in_scope == "Out of Scope":
        return determine_category(description, words)
    
    return ""

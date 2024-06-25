def word_search(query, seq):
    found_strings = [s for s in seq if query.lower() in s.lower()]

    if found_strings:
        return found_strings
    else:
        return ["None"]


query_str = "me"
strings = ["home", "milk", "Mercury", "fish"]
result = word_search(query_str, strings)
print(result)
def sort_list_of_dicts_by_key(list_of_dicts, key):
    """
    Sort a list of dictionaries by a key
    """
    return sorted(list_of_dicts, key=lambda k: k[key])

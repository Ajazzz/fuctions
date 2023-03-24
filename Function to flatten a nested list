def flatten_list(nested_list):
    """
    Flatten a nested list
    """
    flat_list = []
    for i in nested_list:
        if isinstance(i, list):
            flat_list.extend(flatten_list(i))
        else:
            flat_list.append(i)
    return flat_list

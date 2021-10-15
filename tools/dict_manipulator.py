def get_dict_pos(lst, key, value):
    return next((index for (index, d) in enumerate(lst) if d[key] == value), None)


def search_engine(search_term, data_key, data):
    a = filter(lambda search_found: search_term in search_found[data_key], data)
    return list(a)

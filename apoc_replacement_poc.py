import mgp


@mgp.function
def merge(map_a: mgp.Map, map_b: mgp.Map) -> mgp.Map:
    map_a.update(map_b)
    return map_a


@mgp.function
def to_set(collection: list) -> list:
    return list(set(list(collection)))


@mgp.function
def sort(collection: list) -> list:
    sorted_list = list(collection)
    sorted_list.sort()
    return sorted_list


@mgp.function
def flatten(collection: list) -> list:
    new_list = []
    for sub_collection in collection:
        sub_collection = list(sub_collection)
        for element in sub_collection:
            new_list.append(element)
    return new_list

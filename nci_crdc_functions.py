import mgp
import json
import ast

@mgp.function
def merge(map_a: mgp.Map, map_b: mgp.Map) -> mgp.Map:
    map_a.update(map_b)
    return map_a


@mgp.function
def to_set(collection: list) -> list:
    seen = set()  
    result = []   
    
    for item in collection:

        item_frozenset = frozenset(item.items())
        

        if item_frozenset not in seen:
            seen.add(item_frozenset)
            result.append(item)
    
    return result


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
    
@mgp.function
def join_collection(collection: list, separator: str = '') -> str:
    result = ''
    for i, item in enumerate(collection):
        if i == 0:
            result += str(item)  
        else:
            result += separator + str(item)

    return result
@mgp.function
def remove_collection_braces(json_list):
    if isinstance(json_list, str):
        json_list = ast.literal_eval(json_list)
    cleaned_list = [item.strip("'\"") if isinstance(item, str) else str(item) for item in json_list]
    cypher_list = ", ".join(cleaned_list)
    return cypher_list
@mgp.function
def text_replace(string, old, new):
    return string.replace(old, new)
@mgp.function
def text_join(elements, delimiter):
    return delimiter.join(elements)
@mgp.function
def text_split(string, delimiter):
    return string.split(delimiter)

@mgp.function
def text_capitalize(string: str) -> str:
    if not string:
        return string
    return string.capitalize()

@mgp.function
def map_group_by(collection: list, key: str) -> mgp.Map:
    """
    Groups items in a collection by a specified key, similar to apoc.map.groupBy.
    
    Args:
        collection: List of dictionaries/maps to group
        key: The key to group by
        
    Returns:
        mgp.Map: A map where each key contains a list of items that share that key value
    """
    result = {}
    
    for item in collection:
        # Handle both dict-like objects and mgp.Map objects
        if hasattr(item, 'get'):
            group_key = item.get(key)
        elif isinstance(item, dict):
            group_key = item.get(key)
        else:
            continue  # Skip items that don't have the expected structure
            
        # Convert the group key to string for consistency
        group_key_str = str(group_key) if group_key is not None else "null"
        
        # Initialize the group if it doesn't exist
        if group_key_str not in result:
            result[group_key_str] = []
            
        # Add the item to the appropriate group
        result[group_key_str].append(item)
    
    return result


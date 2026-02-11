#!/usr/bin/python3
def class_to_json(obj):
    """
    Returns a dictionary of all serializable attributes
    (instance and class attributes) of obj.
    """
    result = {}
    for key in dir(obj):
        if key.startswith('__'):
            continue
        value = getattr(obj, key)
        if isinstance(value, (int, float, str, bool, list, dict)):
            result[key] = value
    return result

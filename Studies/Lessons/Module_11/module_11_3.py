def introspection_info(obj):
    result = {'type': type(obj),
              'attributes': dir(obj),
              'methods': [method for method in dir(type(obj)) if callable(getattr(obj, method))],
              'module': obj.__mod__, }
    return result


number_info = introspection_info(42)
print(number_info)

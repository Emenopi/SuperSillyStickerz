def find_dict_by_item(attrName, attrContent, dict_list, ):
        for dict in dict_list:
            if dict[attrName] == attrContent:
                return dict
        return None
    
def dict_to_obj(obj, dict):
    for key, value in dict.items():
                setattr(obj, key, value)
    return obj
def find_dict_by_item(attrName, attrContent, dict_list, ):
        for dict in dict_list:
            if dict[attrName] == attrContent:
                return dict
        return None
    
def dict_to_obj(inst, dict):
    for key, value in dict.items():
                setattr(inst, key, value)
    return inst

def create_obj_by_attr(attrName, attrContent, dict_list, inst):
    objData = find_dict_by_item(attrName,attrContent,dict_list)
    obj = dict_to_obj(inst, objData)
    return obj
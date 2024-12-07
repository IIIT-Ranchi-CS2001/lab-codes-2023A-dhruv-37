
def my_zip(name_list, id_list, points_list, strct=True):
    if strct:
        if len(name_list) == len(id_list) == len(points_list):
            return [(name_list[i], id_list[i], points_list[i]) for i in range(len(name_list))]
        else:
            return "Error: Lists are of unequal length."
    else:
        min_len = min(len(name_list), len(id_list), len(points_list))
        return [(name_list[i], id_list[i], points_list[i]) for i in range(min_len)]

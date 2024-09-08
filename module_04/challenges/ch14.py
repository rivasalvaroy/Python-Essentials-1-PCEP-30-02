def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list


foo = [1, 2, 3, 4, 5]
print(list_updater(foo))

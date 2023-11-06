#!/usr/bin/python3
def new_in_list(my_list,idx,element):
    nl =[]
    for i in range(len(my_list)):
        if i ==idx:
            nl.append(element)
        else:
            nl.append(my_list[i])
    return nl

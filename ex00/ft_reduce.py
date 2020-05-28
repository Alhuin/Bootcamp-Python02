def ft_reduce(function_to_apply, list_of_inputs):
    tmp = None
    for el in list_of_inputs:
        tmp = el if tmp is None else function_to_apply(tmp, el)
    return tmp

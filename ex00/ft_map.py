def ft_map(function_to_apply, *list_of_inputs):
    shortest_length = len(list_of_inputs[0])
    # min(strings, key=len)
    for inp in list_of_inputs[1:]:
        if len(inp) < shortest_length:
            shortest_length = len(inp)
    return [
        function_to_apply(*(elem[i] for elem in list_of_inputs))
        for i in range(shortest_length)
    ]

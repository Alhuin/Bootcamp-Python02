def ft_filter(function_to_apply, list_of_inputs):
    if function_to_apply is None:
        return (
            inp
            for inp in list_of_inputs
            if inp
        )
    return (
        inp
        for inp in list_of_inputs
        if function_to_apply(inp)
    )

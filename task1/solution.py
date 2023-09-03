def strict(func):
    type_dct = func.__annotations__
    type_list = [i[1] for i in type_dct.items()]
    def inner(*args,**kwargs):
        for indx,var in enumerate(args):
            if not type(var) == type_list[indx]:
                raise TypeError
        return func(*args,**kwargs)
    return inner

@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError
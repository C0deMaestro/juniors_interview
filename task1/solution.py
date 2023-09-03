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
@strict
def divide(a: float, b: float) -> float:
    return a / b

@strict
def concat_strings(s1: str, s2: str) -> str:
    return s1 + s2

@strict
def logical_and(x: bool, y: bool) -> bool:
    return x and y

# print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError
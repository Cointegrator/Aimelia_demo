import inspect


def log(message: str) -> None:
    stack = inspect.stack()

    the_class = stack[1][0].f_locals["self"].__class__.__name__
    the_method = stack[1][0].f_code.co_name

    print(f"[{the_class}].[{the_method}] {message}")

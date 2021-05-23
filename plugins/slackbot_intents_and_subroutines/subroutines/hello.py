def hello(sb_input):
    print(f"hello world {sb_input}")
    return f"hello world {sb_input}"


def run(sb_input):
    """
    every subroutine must have an input and the run method is named as run
    :param sb_input:
    :return:
    """
    return hello(sb_input)

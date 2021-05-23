from howdoi import howdoi

def get_howdoi(sb_input):
    print(f"> {sb_input}")
    output = howdoi.howdoi(sb_input)
    print(output)
    return f"{output}"


def run(sb_input):
    """
    every subroutine must have an input and the run method is named as run
    :param sb_input:
    :return:
    """
    return get_howdoi(sb_input)

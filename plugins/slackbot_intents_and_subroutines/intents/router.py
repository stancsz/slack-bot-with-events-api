# Route intent, run subroutine and return to caller

def router(intent, input):
    """
    dynamically match intent with subroutine
    https://stackoverflow.com/questions/15792658/call-functions-of-a-dynamically-imported-module
    :param intent:
    :param input:
    :return:
    """
    subroutine = __import__(f"subroutines.%s" % (intent),
                            locals(),
                            globals(),
                            fromlist=[f"{intent}"])
    return subroutine.run(input)

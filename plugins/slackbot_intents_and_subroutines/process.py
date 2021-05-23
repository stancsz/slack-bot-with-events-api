import sys

import intents.get_intent as gi
import intents.router as rt

def process_text(text):
    intent = gi.get_intent(text)
    if intent is not None:
        response = rt.router(intent, text)
        return response
    return


if __name__ == '__main__':
    process_text(sys.argv[1])

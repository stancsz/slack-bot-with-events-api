def get_intent(message):
    print(f"message received is: {message}")
    howdoi_list = ['howdo', 'howto', 'howcan', 'whatto', 'anyoneknow']
    staged_message = message.replace(" ", "").lower()
    for i in howdoi_list:
        if i in staged_message:
            return "howdoido"
    return

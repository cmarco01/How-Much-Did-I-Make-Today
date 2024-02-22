from datetime import date


def init():
    today = date.today()
    getDate = today.strftime("%B %d, %Y")
    # print(getDate)


init()
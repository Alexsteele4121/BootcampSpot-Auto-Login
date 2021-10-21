class Colors:
    # Clears all colors and affects
    clear = '\033[0m'

    # Effects
    bold = '\033[1m'
    italic = '\33[3m'
    underline = '\033[4m'
    blink = '\33[5m'
    selected = '\33[7m'

    # Colors
    gray = '\33[90m'
    red = '\33[91m'
    green = '\33[92m'
    yellow = '\33[93m'
    blue = '\33[94m'
    violet = '\33[95m'
    cyan = '\33[96m'
    white = '\33[97m'

    # Background Colors
    black_bg = '\33[100m'
    red_bg = '\33[101m'
    green_bg = '\33[102m'
    yellow_bg = '\33[103m'
    blue_bg = '\33[104m'
    violet_bg = '\33[105m'
    cyan_bg = '\33[106m'
    white_bg = '\33[107m'


def inform(text: str, end: str = '\n'):
    print(Colors.cyan + '[-]', text + Colors.clear, end=end)


def successful(text: str, end: str = '\n'):
    print(Colors.green + '[*]', text + Colors.clear, end=end)


def warning(text: str, end: str = '\n'):
    print(Colors.yellow + '[*]', text + Colors.clear, end=end)


def error(text: str, end: str = '\n'):
    print(Colors.red + '[!]', text + Colors.clear, end=end)

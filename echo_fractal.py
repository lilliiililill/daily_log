# 2026.08.22
# echo_fractal.py

def echo(text):

    if len(text) <= 1:

        return text

    return f"{text} -> {echo(text[1: -1])} <- {text}"

print(echo("PYTHON"))

import pipes


def make_upper(text: str) -> str:
    """
    3.13で削除されるpipesモジュールを使用する関数
    https://docs.python.org/3.12/library/pipes.html#module-pipes
    """
    t = pipes.Template()
    t.append("tr a-z A-Z", "--")

    with t.open("pipefile", "w") as f:
        f.write(text)

    with open("pipefile", "r") as f:
        output = f.read()

    return output

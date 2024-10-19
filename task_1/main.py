def list_of_numbers(n: int) -> list:
    arr = []
    for i in range(1, n + 1):
        arr.append(i)
    return arr


def reverse(string: str) -> str:
    try:
        return string[::-1].lower()
    except TypeError:
        return f'{string} не является строкой'


def check_email(email: str) -> bool:
    if email.count('@') == 1 and ' ' not in email and '.' in email:
        return True
    else:
        return False

# 2026.10.27
# days_until_date.py

from datetime import datetime, date

def days_until(target_str):

    try:

        target = datetime.strptime(target_str, "%Y-%M-%d").date()

    except ValueError:

        return "날짜 형식 잘못됨 (YYYY-MM-DD)"

    today = date.today()
    delta = (target - today).days

    if delta > 0:

        return f"{delta}일 남음"

    elif delta == 0:

        return "오늘이야!"

    else:

        return f"{abs(delta)}일 지남"


if __name__ == "__main__":

    user_input = input("목표 날짜 입력 (YYYY-MM-DD):")
    print(days_until(user_input))

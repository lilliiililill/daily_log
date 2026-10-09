# 2026.10.10
# weekday_orbit.py

from datetime import date

labels = "월화수목금토일"
today = date.today().weekday()

for step in range(7):

    idx = (today + step) % 7
    mark = "●" if step == 0 else "○"
    print(f"{step}일 후: {labels[idx]} {mark}")

# 2026.10.08
# mask_email.py

def mask_email(email):

    name, domain = email.split("@")
    return name[:2] + "*"  * (len(name) - 2) + "@" + domain


print(mask_email("python123@gmail.com"))

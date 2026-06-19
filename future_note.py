# 2026.06.20
# future_note.py

msg = input("미래의 나에게 한마디: ")

capsule = sum(ord(c) for c in msg) % 100

print("\n[10년 후 개봉]")
print(f"보관 번호: {capsule:02d}")
print(f"내용: {msg}")

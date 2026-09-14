log = "2026-09-14|ERROR|user_id=4471|message=Payment failed due to timeout"

infos= log.split("|")

print(f"Date: {infos[0]}")
print(f"Level: {infos[1]}")
print(f"User ID: {infos[2][infos[2].find("=")+1:]}")
print(f"Message: {infos[3][infos[3].find("=")+1:]}")
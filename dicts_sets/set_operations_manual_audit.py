premium_users = {"u1", "u3", "u5", "u7", "u9"}
active_users = {"u2", "u3", "u4", "u5", "u8"}
flagged_users = {"u5", "u9"}

premium_and_active= premium_users.intersection(active_users)

active_not_premium= active_users-premium_users

exclusive_users= premium_users.symmetric_difference(active_users)

escalated_users= premium_users and flagged_users

invalid_flagged= flagged_users.intersection(active_not_premium)

print(f"Users who are premium and active: {premium_and_active}")
print(f"Users who are active but not premium: {active_not_premium}")
print(f"Users who are either premium or active: {exclusive_users}")
print(f"Premium users who are flagged (escalated): {escalated_users}")
print(f"Check flagged users wrongly in active-only group: {invalid_flagged}")
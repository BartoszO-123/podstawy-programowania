facebook = True
twitter = False
instagram = True
# instagram = False


print(f"facebook = {facebook}")
print(f"twitter = {twitter}")
print(f"instagram = {instagram}")


active_accounts_count = facebook + twitter + instagram


print("--- Assessment ---")

if active_accounts_count >= 2:
    print("You are a good influencer!")
else:
    print(
        "You do not meet the minimum requirement (at least two accounts) to be considered a good influencer."
    )

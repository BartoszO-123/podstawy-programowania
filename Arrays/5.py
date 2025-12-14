computer_games = [
    "Minecraft",
    "Fortnite",
    "Cyberpunk 2077",
    "The Witcher 3",
    "League of Legends",
    "Valorant",
    "Grand Theft Auto V",
    "Elden Ring",
    "Apex Legends",
    "Call of Duty: Warzone",
]

computer_games.sort()

print("\nPopular Computer Games (sorted):")
index = 1
for game in computer_games:
    print(f"{index}. {game}")
    index += 1

# A dictionary to store a player's profile

player = {
    "username": "Adventurer_1",
    "level": 5,
    "gold": 100
}

print(f"Original player profile: {player}")

# Access a value using it's key

current_gold = player["gold"]
print(f"The player has {current_gold} gold. ")

# Add a new key-value pair

print("Player found a key!")
player["has_key"] = True

# Modify an existing value

print("Player spent 20 gold...")
player["gold"] = player["gold"] - 20

# Remove a key-value pair using 'del'
print("Removing the level key...")

del player["level"]
print(f"Final player profile: {player}")
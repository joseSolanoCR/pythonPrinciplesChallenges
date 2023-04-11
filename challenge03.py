statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def online_count(statuses):
    count = 0
    for value in statuses.values():
        if value == 'online':
            count = count +1
    return count
print(online_count(statuses))
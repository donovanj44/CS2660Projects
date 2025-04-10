import hashlib
import csv


with open("common_words.txt", "r") as f:
    wordlist = [line.strip() for line in f]

users = []
with open("testusers.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if len(row) == 3:
            username, user_id, hash_value = row
            users.append((username, hash_value))

cracked_passwords = {}

for word in wordlist:
    hashed_word = hashlib.sha1(word.encode()).hexdigest()
    for username, stored_hash in users:
        if hashed_word == stored_hash:
            cracked_passwords[username] = word
            print(f"[+] Found password for {username}: {word}")

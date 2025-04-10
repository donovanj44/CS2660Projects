import requests

with open("words_to_test.txt", "r") as file:
    words = [line.strip() for line in file]

found_files = []

for word in words:
    url = f"http://jreddy1.w3.uvm.edu/cs2660/accounts/{word}.csv"
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Found: {url}")
        found_files.append(url)
        with open(f"retrieved_{word}.csv", "wb") as f:
            f.write(response.content)
        break

if not found_files:
    print("No valid files found.")

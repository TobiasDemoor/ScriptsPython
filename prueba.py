import requests
r = requests.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vRI2OKrUzJc30kIvIZP9xc4lKAGnN3h9p-cq-yhxkYrEV83bYrzwChpqW0yLQa0cpNQxDAIa56iXb7p/pub?output=csv")
print(r.text)
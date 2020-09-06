deposit = int(input().strip())
rate = 1.071
years = 0

while deposit < 700000:
    years += 1
    deposit *= rate
print(years)

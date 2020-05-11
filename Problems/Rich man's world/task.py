years = 0
deposit = int(input())
while deposit <= 700000:
    deposit = deposit * 1.071
    years = years + 1
print(years)
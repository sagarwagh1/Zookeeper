number = int(input())
word = input()

# write a condition for plurals
if number == 1 and word[-1] != 's':
    print(number, word)
if number != 1 and word[-1] != 's':
    word = word + 's'
    print(number, word)

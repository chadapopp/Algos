# Write a program that takes in a dictionary of stock prices and returns the name of the stock with the highest price.

stocks = {
    "Microsoft": 120,
    "Amazon": 140,
    "Netflix": 130,
    "Tesla": 160,
    "Google": 150,
}


max_key = next(iter(stocks))

for key in stocks:
    if stocks[key] > stocks[max_key]:
#         max_key = key
        print(max_key)

def highest_stock(stocks):
    highest = 0
    for key, val in stocks.items():
        if val > highest:
            highest_com = key
            highest = val
    return [highest_com, highest] 

best_com = highest_stock(stocks)
stocks.pop(best_com[0])
second_highest = highest_stock(stocks)

print(best_com)
print(second_highest)

# Expected output: Tesla

#  most repeated letter: write a function that accepts an array of letters and returns the most repeated letter


def repeated_letter(letters):
    letter_count = {}
    
    for letter in letters:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    
    max_count = 0
    most_repeated_letter = None
    
    for letter, count in letter_count.items():
        if count > max_count:
            max_count = count
            most_repeated_letter = letter
    
    return most_repeated_letter

letters = ['a', 'a', 'b', 'b', 'b', 'c', 'a', 'c', 'a']
print(repeated_letter(letters))

dic = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '0': 'zero'
}

phone_number = input('phone: ')
numbers = phone_number.split()
print(len(numbers))
for ch in phone_number:
    str = dic[ch]
    if str != None:
        print(str)
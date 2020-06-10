string = input('enter string');
result = ''
for i in string:
        if i == 'n':
                i = 'ns'
        result += i
print(result)
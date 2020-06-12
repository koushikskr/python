def string_alternative(value):
    list_input=list(value)
    list_output=[]
    for i in range(len(list_input)):
        if(i%2==0):
             list_output.append(list_input[i])
    string=''.join(list_output)
    return string
def __main():
    Str = input(("Enter Input String:"))
    print("Input:", Str)
    return string_alternative(Str)

print("Output:",__main())
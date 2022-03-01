def print_formatted(number):
    space = len('{0:b}'.format(n))
    for num in range(1,number+1):
        Hexadecimal = (hex(int(num)).replace('0x','')).upper().rjust(space,' ')
        Octal = oct(int(num)).replace('0o','').rjust(space,' ')
        Binary = ('{0:b}'.format(num)).rjust(space, ' ')
        Decimal = str(num).rjust(space, ' ')
        print(Decimal, Octal, Hexadecimal, Binary)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

ss0 = '98uiabch\tsi\nabc05-ui7/a\nd-propabc-0328'
ss1 = ('today', 'is', '2023', '4', '1')
ss2 = '今天is0328'


print('aBcDeFg'.capitalize())
print('aBcDeFg'.lower())
print('aBcDeFg'.upper())
print('aBcDeFg'.swapcase())
print('aBcD eFg'.title())


print(ss0.endswith('28', 0, len(ss0)))
print(ss0.startswith('98', 0, len(ss0)))

print("isalnum?", 'aBc123'.isalnum())
print("isalpha?", 'ni好'.isalpha())
print("isdigit?", '65536'.isdigit())
print("islower?", 'is123'.islower())
print("isnumeric?", '16384½'.isnumeric())
print("isspace?", '\t\n'.isspace())
print("istitle?", 'Abcd Efg'.istitle())
print("isupper?", '123UPP'.isupper())
print("isdeciaml?", '86808'.isdecimal())


print(ss0.count('abc', 0, len(ss0)))
print(ss0.find('ui', 0, len(ss0)))
print(ss0.rfind('ui', 0, len(ss0)))
print(ss0.index('ui', 0, len(ss0)))
print(ss0.rindex('ui', 0, len(ss0)))

print('hello'.ljust(10, '-'))
print('hello'.rjust(10, '-'))
print('hello'.center(10, '-'))
print('--strip-'.lstrip('-'))
print('--strip-'.rstrip('-'))
print('--strip-'.strip('-'))
print('6a8'.zfill(8))
print('8x2x5=80=0x50'.replace('x', '*', 2))
print('[\t]'.expandtabs(4))


print(max('ifaux'))
print(min('ifaux'))

ss2_utf8 = ss2.encode(encoding='gbk')
print(type(ss2_utf8), ss2_utf8)
print(ss2_utf8.decode(encoding='gbk'))

print('-'.join(ss1))
print(ss0.split('-', 2))
print(ss0.splitlines(True))


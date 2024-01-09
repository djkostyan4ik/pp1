import re
def f(vname):
    regex = '[a-zA-Z_]'
    if len(vname) not in range(1,6):
        return False
    first_character = re.search(regex,vname[0])
    if first_character:
        return True
    else:
        return False

def main():
    print(f('abc'))
    print(f('Abc'))
    print(f('aBC'))
    print(f('_ab_c'))
    print(f('abcdef'))
    print(f('8abc'))
    print(f('_aB8_'))
    print(f('_4x'))

if __name__ == '__main__':
    main()
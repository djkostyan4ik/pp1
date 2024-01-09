def f(uid):
    result = []
    for id in uid:
        if id not in result:
            result.append(id)
        else:
            return False
    return True

def main():
    print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]))
    print(f(["abc123","ann","abc123","a10"]))
    print(f(["bob2","bob2"]))
    print(f(["bob2","BOB2"]))
    print(f(["BOB2"]))

if __name__ == '__main__':
    main()
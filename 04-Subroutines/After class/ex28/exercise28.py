def f(binary_number):
    istrue = True
    for i in binary_number:
        if i != '0' and i != '1':
            istrue = False
    return istrue

if __name__ == '__main__':
    print(f"f('101101') returns {f('101101')}")
    print(f"f('1311a10100') returns {f('1311a10100')}")
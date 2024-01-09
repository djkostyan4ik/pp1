def f(fnc,prods):
    result = list(map(fnc,prods))
    return ','.join(result)
def main():
    print(f(lambda x: "id:"+x[:2],["water","cheese","tomato"]))
    print(f(lambda x: (x[0]+x[-1]).upper(),["water","cheese","tomato"]))


if __name__ == '__main__':
    main()
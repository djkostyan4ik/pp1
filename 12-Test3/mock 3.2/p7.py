def f(d):
    arr = []
    for row in d:
        if row[1] == 'in':
            arr.append(row[0])
        if row[1] == 'out' and row[0] in arr:
            arr.remove(row[0])
    arr.sort()
    return arr
def main():
    print(f([["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"], ["BA111","in"],["BA123","out"],["KR234","in"]]))
    print(f([["KR234","in"],["KR234","out"]]))

if __name__ =='__main__':
    main()
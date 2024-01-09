def f(fnc,res):
    filtered = list(filter(fnc,res))
    result = max(filtered) - min(filtered)
    return result

def main():
    print(f(lambda x: x > 50,[95,90,20,50,70]))
    print(f(lambda x: x > 30 and x < 90,[95,90,20,50,70]))

if __name__ == '__main__':
    main()
def f(fnc,res):
    filtered_result = list(filter(fnc,res))
    maximum = max(filtered_result)
    minimum = min(filtered_result)
    result = maximum - minimum
    return result
def main():
    print(f(lambda x: x>50,[95,90,20,50,70]))
    print(f(lambda x: x>30 and x<90,[95,90,20,50,70]))
    print(f(lambda x: x>30 and x<90,[-9,-89,-78,-34]))

if __name__ == '__main__':
    main()
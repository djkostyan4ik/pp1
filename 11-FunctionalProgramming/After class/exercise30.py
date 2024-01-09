def main() -> None:
    filled_bottles = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509]
    bottle_capasity = 500
    tolerance = 500 * 0.02


    def is_filled_correctly(fill: int) -> bool:
        return fill > (bottle_capasity + tolerance) or fill < (bottle_capasity - tolerance)
    
    filtered_bottles = list(filter(is_filled_correctly,filled_bottles))

    print(len(filtered_bottles) * 100 / len(filled_bottles))

if __name__ == '__main__':
    main()
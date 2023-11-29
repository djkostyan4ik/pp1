countries = [
    {'name': 'Poland', 'population': 38000000},
    {'name': 'Belarus', 'population': 9340000},
    {'name': 'Ukraine', 'population': 43790000},
    {'name': 'Czech', 'population': 10510000},
    {'name': 'UK', 'population': 67330000},
    {'name': 'France', 'population': 67750000}
    ]

print(f'{"Country":10}{"Population":10}')
i = 0
while i != len(countries):
    print(f'{countries[i]['name']:10}{countries[i]['population']:<10}')
    i += 1

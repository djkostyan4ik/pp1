def hotel_list(hotels):
    result=[]
    for i in range(len(hotels)):
        result += {hotels[i]['name']}
    return (', '.join(map(str,result)))

def avg_price(hotels):
    prices = []
    for i in range(len(hotels)):
        prices += {hotels[i]['price']}
    lenght = len(prices)
    my_sum = 0
    for j in prices:
        my_sum += int(j)
    av_price = my_sum/lenght
    return round(av_price)


hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]



if __name__ == '__main__':
    print('Hotels in Krakow:',hotel_list(hotels_in_Krakow))
    print('Average hotel price in Krakow:',avg_price(hotels_in_Krakow))
    print('Hotels in Sopot:',hotel_list(hotels_in_Sopot))
    print('Average hotel price in Sopot:',avg_price(hotels_in_Sopot))

if avg_price(hotels_in_Krakow) > avg_price(hotels_in_Sopot):
    print('Cheaper hotels in: Sopot')
else:
    print('Cheaper hotels in: Krakow')
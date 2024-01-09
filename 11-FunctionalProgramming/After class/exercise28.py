classification = [{"country":"Denmark","gold":2,"silver":4,"bronze":6},
{"country":"Finland","gold":5,"silver":0,"bronze":4},
{"country":"USA","gold":12,"silver":5,"bronze":11},
{"country":"Peru","gold":0,"silver":1,"bronze":7}]
medals = list(filter(lambda x: x['gold'] + x['silver'] + x['bronze']>=10, classification))
print('COUNTRIES WITH AT LEAST 10 MEDALS')
print(f"{medals[0]["country"]}: {medals[0]["gold"]}, {medals[0]["silver"]}, {medals[0]["bronze"]}")
print(f"{medals[1]["country"]}: {medals[1]["gold"]}, {medals[1]["silver"]}, {medals[1]["bronze"]}")
speed = [48,47,54,50,42,68,39,46]
view1 = ','.join(map(str,speed))
result = list(filter(lambda n: n > 50,speed))
view2 = ','.join(map(str, result))
print(f'Recorded speed: {view1}')
print(f'Speed too high: {view2}')
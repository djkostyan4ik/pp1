test_results = [
    {"name":"Peter","result":27},
    {"name":"Anna","result":63},
    {"name":"Robert","result":92},
    {"name":"Paul","result":46},
    {"name":"Barbara","result":52}]
students = list(filter(lambda x: x['result'] < 70 and x['result'] > 50, test_results))
print([x['name'] for x in students])
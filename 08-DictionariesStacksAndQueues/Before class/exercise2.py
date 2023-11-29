post = {'user_id':209, 'message': 'D5 E5 C5 C4 G4', 'language':  'English', 'datetime': '20230215T124231Z', 'location':(44.590533,-104.715556)}
print(type(post))

post2 = {'message':'SS Cotopaxi', 'language': 'English'}

post2['user_id'] = 209
post2['datetime'] = '19771116T093001Z'

print(post2)
print(post['message'])




try:
    print(post2['location'])
except KeyError:
    print('The post does not have a location.')



loc = post2.get('location',None)
print(loc)



for key in post.keys():
    value = post[key]
    print(key, '=', value)



for key, value in post.items():
    print(key, '=', value)
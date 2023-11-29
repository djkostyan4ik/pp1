import re

names = ['Finn Bindeballe',
         'Geir Anders Berge',
         'HappyCodingRobot',
         'Ron Cromberge',
         'Sohil']

# Find people with first and last name only
regex = '^\\w+\\s+\\w+$'
for name in names:
    result = re.search(regex, name)
    if result:
        print(name)


# # Find people with first and last name only
# regex = '^\\w+\\s+\\w+$'
# for name in names:
#     result = re.search(regex, name)
#     if result:
#         print(result)


# # Search for word char sequence starting with C
# regex = 'C\\w*'
# for name in names:
#     match = re.search(regex,name)
#     if match:
#         print(name)
#         # print(match.start())
#         # print(match.end())
#         print(match.span())
#         print(match.group())

names1 = ['Brian Daugette',
          'Veronica Supersonica',
          'Tony Gasparovic',
          'Patrick Germann',
          'm!sha']

# regex = '^(?P<fn>\\w+)\\s+(?P<ln>\\w+)$'
# for name in names1:
#     match = re.search(regex,name)
#     if match:
#         print(name)
#         print(match.group('fn'))
#         print(match.group('ln'))



# # Detect lat name
# regex = '^[a-zA-Z!]+$'
# for name in names1:
#     if re.search(regex,name):
#         print(name)



# #  Scan for blocks of lower case.letters
# regex = '[a-z]+'
# for name in names1:
#     matches = re.findall(regex,name)
#     if matches:
#         print(matches)





# #  Scan for blocks of lower case.letters
# regex = '[a-z]+'
# for name in names1:
#     matches = re.finditer(regex,name)
#     for match in matches:
#         print(match)


values = ['https://www.socratica.com',
          'http://www.socratica.org',
          'file://test.this.path',
          'com.socratica.www_https://']

# # Test if string starts with http or https
# regex = 'https?'
# for value in values:
#     if re.match(regex,value):
#         print(value)

regex = 'https?://w{3}.\\w+.(org|com)'
for value in values:
    if re.fullmatch(regex,value):
        print(value)
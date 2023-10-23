question1 = input ('Do you have an account in Facebook?\n (1 for Yes/2 for No)\n\n')
answer1 = int(question1)

question2 = input ('Do you have an account in Twitter?\n (1 for Yes/2 for No)\n\n')
answer2 = int(question2)

question3 = input ('Do you have an account in Instagram?\n (1 for Yes/2 for No)\n\n')
answer3 = int(question3)

if answer1 == 1:
    answer1 = True
    print('Facebook =',True)
else:
    answer1 = False
    print('Facebook =',False)
if answer2 == 1:
    answer2 = True
    print('Twitter =',True)
else:
    answer2 = False
    print('Twitter =',False)
if answer3 == 1:
    answer3 = True
    print('Instagram =',True)
else:
    answer3 = False
    print('Instagram =',False) 

if answer1 == True and answer2 == True:
    print('A person can be a good influencer!')
elif answer1 == True and answer3 == True:
    print('A person can be a good influencer!')
elif answer2 == True and answer3 == True:
    print('A person can be a good influencer!')
else:
    print("A person can't be a good influencer!")
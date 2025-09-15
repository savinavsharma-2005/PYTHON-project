import random
dic={
    'snake':1,
    'water':0,
    'gun':-1
}
reverseDic={
    1:'snake',
    0:'water',
    -1:'gun'
}

machine=random.choice([1,0,-1])

user=input("enter your choice : ")
user_num=dic.get(user)

print(f"You:{reverseDic.get(user_num)}  ;  Computer:{reverseDic.get(machine)}")

if machine-user_num==-1 or machine-user_num==2:
    print("YOU WIN !")
elif machine-user_num==-2 or machine-user_num==1:
    print("YOU LOSE !")
else:
    print("Some error occured !")
    

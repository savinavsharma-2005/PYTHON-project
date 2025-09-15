import random
dic={
    'rock':1,
    'paper':0,
    'scissors':-1
}
reverseDic={
    1:'rock',
    0:'paper',
    -1:'scissors'
}

machine=random.choice([1,0,-1])

user=input("enter your choice : ")
user_num=dic.get(user)

print(f"You:{reverseDic.get(user_num)}  ;  Computer:{reverseDic.get(machine)}")
if user_num == machine:
    print("Draw !")

elif machine-user_num==1 or machine-user_num==-2:
    print("YOU WIN !")
elif machine-user_num==2 or machine-user_num==-1:
    print("YOU LOSE !")
else:
    print("Some error occured !")
    

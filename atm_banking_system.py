import mysql.connector
import random

db=mysql.connector.connect(host='localhost',username='root',password='S@nthosh712')
cursr=db.cursor()
cursr.execute('create database IF NOT EXISTS bankingdetails')
db.commit()

db1=mysql.connector.connect(host='localhost',username='root',password='S@nthosh712',database='bankingdetails')
s=db1.cursor()

s.execute('create table if not exists banking1(name varchar(200) not null,accnum int not null primary key,dob varchar(10) not null,balance int not null)')
q="insert into banking1(name,accnum,dob,balance) values(%s,%s,%s,%s)"
while True:
    ch=input("1.CREATE ACCOUNT\n2.ADD MONEY\n3.WITHDRAW MONEY\n4.CHECK BALANCE\n5.SHOW ACCOUNT DETAILS\n6.EXIT:-")
    if ch=='1':
        try:
            name=input('enter your good name:-')
            if len(name)==0:
                print('\ninvalid name\n')
                continue
            elif name==' ' or name=='  ' or name=='   ' or name=='    ' or name=='     ':
                print('\ninvalid name\n')
                continue
            d=input('enter DOB in mm-dd-yyyy:-')
            x,y,z=d.split('-')
            if int(x)>=1 and int(x)<=12 and int(y)>=1 and int(y)<=31 and len(z)==4:
                date=d
                print(date)
            else:
                print('invalid')
                d=input('enter DOB in mm-dd-yyyy format again:-')
                x,y,z=d.split('-')
                if int(x)>=1 and int(x)<=12 and int(y)>=1 and int(y)<=31:
                    date=d
                    print(date,'considered')
                else:
                    print('invalid date retry again from begining')
                    continue

            amount=int(input("entrer amt to add please add more than 500:-"))
            if amount>=500:
                amt=amount
            else:
                print('\ninvalid retry entering amt greater than 500')
                continue

            num=random.randint(100000,1000000)
            amt=str(amt)
            num=str(num)
            tup=(name,num,date,amt)
            s.execute(q,tup)
            db1.commit()
            print('accnt created succesfully and your acc num is',num)
        except:
            print('\nerror in creating accunt,retry\n')
    elif ch=='2':
        accnum=int(input('enter yout acc num:-'))
        v1=(accnum,)
        try:
            s.execute('select balance from banking1 where accnum=%s',v1)
            srch=s.fetchone()
            for i in srch:
                balance1=i
            print('acc balnce is',balance1)
            amt1=int(input('enter the amount to add'))
            amt1+=balance1
            v=(amt1,accnum)
            s.execute('update banking1 set balance=%s where accnum=%s',v)
            db1.commit()
            print('\nbalance updated new balance is',amt1)
        except:
            print('\ninvalid details\n')

    elif ch=='3':
         try:
             accnum=int(input('enter yout acc num:-'))
             v1=(accnum,)
             s.execute('select balance from banking1 where accnum=%s',v1)
             srch=s.fetchone()
             for i in srch:
                 balance2=i
             print('acc balnce is',balance2)
             withdraw=int(input('enter any amout less than your acc balance'))
             if withdraw<=balance2:
                amt2=balance2-withdraw
                v2=(amt2,accnum)
                s.execute('update banking1 set balance=%s where accnum=%s',v2)
                db1.commit()
                print('\n',withdraw,'rs withdrawed')
                print('\nbalance left:rs',amt2)
             else:
                 print('\ninsufficient funds')
         except:
            print('\ninvalid details\n')
            
    elif ch=='4':
        try:
            accnum=int(input('enter yout acc num:-'))
            v1=(accnum,)
            s.execute('select balance from banking1 where accnum=%s',v1)
            srch=s.fetchone()
            for i in srch:
                balance1=i
            print('\nacc balnce is',balance1)
        except:
            print('\ninvalid details\n')
 

    elif ch=='5':
        try:
            accnum=int(input('enter your accnum:-'))
            v3=(accnum,)
            s.execute('select name from banking1 where accnum=%s',v3)
            s1=s.fetchone()
            for i in s1:
                name=i
            s.execute('select dob from banking1 where accnum=%s',v3)
            s2=s.fetchone()
            for i in s2:
                dob=i
            s.execute('select balance from banking1 where accnum=%s',v3)
            s3=s.fetchone()
            for i in s3:
                bal=i
            print('\n\n')
            print('hello',name)
            print('accnum is:-',accnum)
            print("DOB is",dob)
            print('acc balance',bal)
            print('\n\n')
        except:
            print('\ninvalid details\n')
    else:
        break
        
    




            
            
            
        
        
    


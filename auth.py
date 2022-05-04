import mysql.connector
db=mysql.connector.connect(host='localhost',username='root',password='S@nthosh712')
myd=db.cursor()
myd.execute("CREATE DATABASE IF NOT EXISTS logindetails")

s=mysql.connector.connect(host='localhost',username='root',password='S@nthosh712',database='logindetails')
x=s.cursor()

x.execute('show tables')

for i in x:
    if i==('logincredentials',):
        #print('table exists')
        break
    else:
        x.execute("create table logincredentials(usernamees varchar(250) not null primary key,passwords varchar(250) not null)")
        
q="insert into logincredentials(usernamees,passwords) values(%s,%s)"

while True:
    y=input("1 to sign up 2 to login 3 to delete and 4 to exit:")
    
    if y=='1':
        usrnm=input("enter ur username:")
        pswrd=input("enter your password:")
        try:
            if len(pswrd)>=6:
                v=(usrnm,pswrd)
                x.execute(q,v)
                s.commit()
            else:
                print("enter password with more 6 characterd")
                pswrd=input("enter your password:")
                if len(pswrd)>=6:
                    v=(usrnm,pswrd)
                    x.execute(q,v)
                    s.commit()
                else:
                    print("invalid,account not created,try again choosing password")
                    continue
            print("account created successfully")      
        except:
            print('account not created,same username already exists ')
     
    elif y=='2':
        try:
            usrnm=input("enter ur username:")       
            pswrd=input("enter your password:")
            tuple1=(usrnm,pswrd)
            x.execute("select * from logincredentials where usernamees='%s' and passwords='%s';",tuple1)
            s.commit()
            srch=x.fetchall()
            for x in srch:
                print('\nhello',usrnm)

        except:
            print('invalid details')
    elif y=='3':
        usrnm=input("enter ur username:")       
        pswrd=input("enter your password:")
        tuple1=(usrnm,)
        x.execute("delete from logincredentials where usernamees=%s",tuple1)
        print("succesfully deleted")

    else:
        print('thank you byee')
        break
    



import sqlite3
DB_NAME="users.db"
def create_database():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    cursor.execute(""" 
                        CREATE TABLE IF NOT EXISTS role (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        role_fk INTEGER
                        );
                       """)
    cursor.execute("""
                       CREATE TABLE IF NOT EXISTS users (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       login VARCHAR(25),
                       password VARCHAR(32),
                       role_fk INTEGER,
                       FOREIGN KEY (role_fk) REFERENCES role(id) ON DELETE CASCADE
                       );
    
                 """)
    
    connect.commit
    cursor.close()
create_database()
def insert_into():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    roles=[("Администратор",),
         ("Модератор",),
         ("Гость",),
         ("Пользователь",)]

   #INSERT INTO role (role) VALUES("Admin");/
    for role in roles:
        cursor.execute("""
                 INSERT INTO role (role_fk)
                 VALUES (?)
                 """,role)
    

    users=[("user1","Pass1",1),
           ("user2","Pass2",2),
           ("user3","Pass3",3),
           ("user4","Pass4",1),
           ("user5","Pass5",2),
           ("user6","Pass6",3),
           ("user7","Pass7",1)
           ]
    for user in users:
            cursor.execute("""
                     INSERT INTO users (login,password,role_fk)
                     VALUES (?,?,?)
                     """,user)
            
    connect.commit()
    cursor.close()
insert_into()
#insert_into()
def select():
     connect = sqlite3.connect(DB_NAME)
     cursor = connect.cursor()
     cursor.execute(
                """
               SELECT * FROM users WHERE id<4
                """
                   )
     rows = cursor.fetchall()
     for row in rows:
          print(row)
          connect.commit()
          cursor.close

def updete():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    cursor.execute(
                """
                UPDATE users SET password="P@ssword" WHERE 1
                """
                    )
    connect.commit()
    cursor.close
def delete():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    cursor.execute(
                    """
                DELETE FROM users WHERE id<4
                    """
        )
    connect.commit()
    cursor.close
#create_database()
#insert_into()
delete()
updete()
select()

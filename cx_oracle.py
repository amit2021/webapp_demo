# todos=open('todos.txt','a')
# print(todos)
# print('put out the trash ',file=todos)
# print('feed the cat ',file=todos)
# print('prepare the tax return',file=todos)
# print('hi')
# # tasks=open('todos.txt')
# todos.close()
# # print(tasks)
# # for i in tasks:
# #     print(i)
# with open('todos.txt') as chor:
#     for i in chor:
#         print(i)
# # #todos.close()
#
#
# with open('todos.txt','w') as chor:
#     chor.write('hi')
#     chor.write("\n")
#     chor.write('hello')
#     chor.write("\n")
#     chor.write('how r u')
#     chor.write("\n")
#     chor.writelines(['how r u','i am good ','what about u'])
#
# with open('todos.txt', 'r') as chor:
#     for i in chor:
#         print(i)



import cx_Oracle

# dbconfig = {'host': 'localhost',
#             'user': 'scott',
#             'password': 'tiger',
#             'database': 'ORCLPDB'
#             }

dbconfig={'user':'scott',
          'password':'tiger',
          'dsn':'localhost:1521/orclpdb',
          'encoding':"UTF-8"}

# conn = cx_Oracle.connect('scott/tiger@localhost:1521/orclpdb')

conn = cx_Oracle.connect(**dbconfig)



# conn =cx_Oracle.connect(**dbconfig)

print(conn)

cursor= conn.cursor()
print(cursor)

print('create table script')

try:
    cursor.execute('create table pt_test(ename varchar2(20))')
    print('table created')
except Exception as e:
    print(e)

print('inserting data in table')

try:
    cursor.execute('insert into pt_test values(\'Amit\')')
    conn.commit()
except Exception as e:
    print(e)

print('inserting multiple data in oracle')
try:
    data= [['shweta'],['shweta1'],['shweta2'],['shweta3'],['shweta4']]
    cursor.executemany('insert into pt_test values(:1)', data)
    conn.commit()
except Exception as e:
    print(e)

print('fetching multiple data from db')
cursor.execute('select * from pt_test')
row=cursor.fetchmany(3)
print(row)


print('fetching one data from db')
cursor.execute('select * from pt_test')
row=cursor.fetchone()
print(row)


print('fetching  data from db using bindvariable')
cursor.execute('select * from pt_test where ename = :name',{'name':'shweta1'})
row=cursor.fetchall()
print(row)


conn.close()

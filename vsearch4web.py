# from flask import Flask, render_template ,request,redirect
import cx_Oracle
from flask import Flask, render_template ,request,escape
from search4letters import search4letters
# import cx_Oracle.connect
from DBcm import UseDatabase


app=Flask(__name__)
print(__name__)
print(app)

app.config['dbconfig'] =  { 'user': 'scott',
                            'password': 'tiger',
                            'dsn': 'localhost:1521/orclpdb',
                            'encoding': "UTF-8"}




# def log_request(req:'flask_request',res:str)->None:
    #with open('vsearch4letter.txt','a') as data:
        # print(str(dir(req)),res,file=data)
     #  print(req.form,req.remote_addr,req.user_agent,res,file=data,end=' | ')
        # print(req.remote_addr,file=data,end=' | ')
        # print(req.user_agent,file=data,end=' | ')
        # print(res,file=data,end=' | ')

# ##new version using module and context manager
# def log_request(req:'flask_request',res:str)->None:
#     dbconfig = {'user': 'scott',
#                 'password': 'tiger',
#                 'dsn': 'localhost:1521/orclpdb',
#                 'encoding': "UTF-8"}
#
#     conn = cx_Oracle.connect(**dbconfig)
#     cursor = conn.cursor()
#
#     _sql = """insert into log(phrase,letter,ip,browser_setting,result)
#              values(:1,:2,:3,:4,:5)"""
#     print('inserting data   ',_sql)
#     cursor.execute(_sql,[req.form['phrase'],req.form['letters'],req.remote_addr,req.user_agent.browser,res])
# #    print('done')
#     conn.commit()
#     #cursor.close()
#     conn.close()




def log_request(req:'flask_request',res:str)->None:
    with UseDatabase(app.config['dbconfig']) as cursor:
        _sql = """insert into log(phrase,letter,ip,browser_setting,result)
                 values(:1,:2,:3,:4,:5)"""
        print('inserting data   ',_sql)
        cursor.execute(_sql,[req.form['phrase'],req.form['letters'],req.remote_addr,req.user_agent.browser,res])



# @app.route('/')
# def hello() ->302:
#     return redirect('/entry')

@app.route('/search4',methods=['POST'])
def do_search()->'html':
    phrase=request.form['phrase']
    letter=request.form['letters']
    title='here is your results'
    results=str(search4letters(phrase,letter))
    log_request(request,results)
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letter=letter,
                           the_title=title,
                           the_results=results,)


@app.route('/')
@app.route('/entry')
def entry_page() ->'html':
    # return render_template('entry.html',the_title='welcome to searchpage')
      return render_template('entry.html',the_title='Wlecome to search4letter on thw web for u')


#
# @app.route('/viewlog')
# def view_the_log()->str:
#     with open('vsearch4letter.txt') as data:
#         content=data.read()
#     return content



# @app.route('/viewlog')
# def view_the_log()->'html':
#     contents=[]
#     with open('vsearch4letter.txt') as data:
#         for line in data:
#              contents.append([])
#              for item in line.split('|'):
#                  contents[-1].append(escape(item))
#     titles=('Form Data','Remote_addr','user_agent','Results')
#     return render_template('viewlog.html',
#                            the_title='view Log',
#                            the_row_title=titles,
#                            the_data=contents,)



@app.route('/viewlog')
def view_the_log()->'html':
    with UseDatabase(app.config['dbconfig']) as cursor:
        _sql="""select phrase,letter,ip,browser_setting,result from log"""
        cursor.execute(_sql)
        contents=cursor.fetchall()
    titles=('phrase','letters','Remote_addr','user_agent','Results')
    return render_template('viewlog.html',
                           the_title='view Log',
                           the_row_title=titles,
                           the_data=contents,)



if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)


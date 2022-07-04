

from flask import Flask,redirect, request,url_for,render_template,flash
import json
import os
from os.path import join, dirname
from flask import jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'data'
 
mysql = MySQL(app)
# cursor = mysql.connection.cursor()

@app.route("/login", methods=['GET'])
def login():
    return render_template('login.html')

@app.route("/register.html", methods=['GET'])
def register():
    return render_template('register.html')

@app.route("/",methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/event',methods=['GET'])
def event():
    return render_template('events.html')

@app.route('/courselisting',methods=['GET'])
def courselisting():
    return render_template('course-listing.html')

@app.route('/contact',methods=['GET'])
def contact():
    return render_template('contact.html') 

@app.route('/coursesingle',methods=['GET'])
def coursesingle():
    return render_template('course-single.html') 

@app.route("/gallery2", methods=['GET'])
def gallery2():
    return render_template('gallery2.html') 

@app.route("/course-single", methods=['GET'])
def course_single():
    return render_template('course-single.html') 



@app.route("/detail_gallery", methods=['GET'])
def detail_gallery():
    return render_template('detail_gallery.html') 


@app.route('/getCourse',methods=['POST'])
def getCource():
    sql_select_Query = "select * from hsu_course ORDER BY priority DESC "
    cursor = mysql.connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    cursor.close()
    return jsonify(list(records))

@app.route('/getCourse_crm',methods=['POST'])
def getCource_crm():
    sql_select_Query = "select * from crm_course "
    cursor = mysql.connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    cursor.close()
    return jsonify(list(records)[0:60])
    

@app.route('/login_form', methods=['POST'])
def loginPOST():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username)
    sql = "SELECT * FROM hsu_users WHERE username = '{}' AND password = '{}'  ".format(username,password)
    cursor = mysql.connection.cursor()
    cursor.execute(sql)
    records = cursor.fetchall()
    return jsonify(list(records))


@app.route('/ROLE_ADMIN', methods =['GET'] )
def admin():
    return render_template('indexAdmin.html') 


@app.route('/ROLE_ADMIN/Account',methods =['GET'])
def account_admin():
    return render_template('account.html')

@app.route('/getUser',methods=['POST'])
def getUser():
    sql_select_Query = "select * from hsu_users WHERE Authority = 'ROLE_COUNSELLOR'"
    cursor = mysql.connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    cursor.close()
    return jsonify(list(records))

@app.route('/delete',methods=['GET'])
def deleteAccount():
    id = request.args.get("id")
    sql_select_Query = "DELETE FROM hsu_users WHERE ID = '{}'".format(id)
    cursor = mysql.connection.cursor()
    cursor.execute(sql_select_Query)
    mysql.connection.commit()
    cursor.close()
    return render_template('delete.html')

@app.route('/edit',methods=['GET'])
def editAccount():
    return render_template('edit.html')


@app.route('/getInforAccount',methods=['GET'])
def InforAccount():
    id = request.args.get("id")
    sql_select_Query = "SELECT * FROM hsu_users WHERE ID = '{}'".format(id)
    cursor = mysql.connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    cursor.close()
    return jsonify(list(records))

# /update

@app.route('/update',methods=['GET'])
def update():
    id = request.args.get("id")
    email = request.args.get("email")
    phone = request.args.get('phone')
    sql_select_Query = "UPDATE hsu_users SET Phone = '{}' , email = '{}' WHERE id = '{}'".format(phone,email,id)
    cursor = mysql.connection.cursor()
    cursor.execute(sql_select_Query)
    mysql.connection.commit()
    cursor.close()
    return jsonify({'mess':'Thành công'})



@app.route('/ROLE_COUNSELLOR', methods =['GET'] )
def ROLE_COUNSELLOR():
    return render_template('ROLE_COUNSELLOR.html') 

#/ROLE_COUNSELLOR/enquiry
@app.route('/ROLE_COUNSELLOR/enquiry', methods =['GET'] )
def ROLE_COUNSELLOR_enquiry():
    return render_template('enquiry.html') 

#/ROLE_COUNSELLOR/enquirynote
@app.route('/ROLE_COUNSELLOR/enquirynote', methods =['GET'] )
def ROLE_COUNSELLOR_enquirynote():
    return render_template('enquirynote.html') 

@app.route('/getenquiry',methods=['POST'])
def getenquiry():
    sql_select_Query = "select * from hsu_enquiry ORDER BY id DESC "
    cursor = mysql.connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    cursor.close()
    return jsonify(list(records)[0:200])


@app.route('/getDetailCourse',methods=['GET'])
def getDetailCourse():
    id = request.args.get('id')
    sql_select_Query = "select * from hsu_course WHERE id = '{}'".format(id)
    cursor = mysql.connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    cursor.close()
    return jsonify(list(records))

@app.route('/getDetailCourse2',methods=['GET'])
def getDetailCourse2():
    id = request.args.get('id')
    sql_select_Query = "select * from crm_course WHERE id = '{}'".format(id)
    cursor = mysql.connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    cursor.close()
    return jsonify(list(records))

#edit_course
@app.route('/ROLE_ADMIN/edit_course',methods=['GET'])
def edit_course():
   return render_template('edit_course.html')


#/ROLE_COUNSELLOR/course

@app.route('/ROLE_ADMIN/course', methods =['GET'] )
def ROLE_COUNSELLOR_course():
    return render_template('course.html') 

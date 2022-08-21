'''1 . Write a program to insert a record in sql table via api database
2.  Write a program to update a record via api
3 . Write a program to delete a record via api
4 . Write a program to fetch a record via api
5 . All the above questions you have to answer for mongo db as well .'''

from flask import Flask, request, jsonify
import mysql.connector as conn

app = Flask(__name__)

mydb = conn.connect(host="localhost", user='root', passwd="")
cursor = mydb.cursor()
cursor.execute("create database if not exists taskdb")
cursor.execute("create table if not exists taskdb.tasktable (name varchar(30) , number int)")


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into taskdb.tasktable  values(%s , %s)", (name, number))
        mydb.commit()
        return jsonify(str('succesfully inserted'))


@app.route("/update", methods=['POST'])
def update():
    if request.method == 'POST':
        get_name = request.json['get_name']
        cursor.execute("update taskdb.tasktable set number = number + 500 where name = %s ", (get_name,))
        mydb.commit()
        return jsonify(str("updated successfully"))


if __name__ == '__main__':
    app.run()

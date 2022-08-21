from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("")
database = client['taskdb']
collection = database['taskcollection']


@app.route("/insert/mongo", methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name: number})
        return jsonify(str("succefully inserted "))


if __name__ == '__main__':
    app.run()



'''To directly fetch data to web via sql '''


@app.route('/get_data')
def get_data_from():
    db = request.args.get('db')
    tn = request.args.get('tn')
    try:
        con = conn.connect(host="localhost", user="root", password="", database=db)
        cur = con.cursor(dictionary=True)
        cur.execute(f'select * from {tn}')
        data = cur.fetchall()
        con.commit()
        con.close()
    except Exception as e:
        return jsonify(str(e))
    return jsonify(data)


if __name__ == "__main__":
    app.run(port=5002)

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('homework4.html')

## API 역할을 하는 부분
@app.route('/templates', methods=['POST'])
def write_review():
   # 1. 클라이언트가 준 title, author, review 가져오기.
   # 2. DB에 정보 삽입하기
   # 3. 성공 여부 & 성공 메시지 반환하기

   inputGroupSelect01 = request.form['inputGroupSelect01_give']
   name = request.form['name_give']
   address = request.form['address_give']
   tel = request.form['tel_give']

   print(inputGroupSelect01)
   
   print(name)
   print(address)
   print(tel)


   db.reviewCollection.insert_one({
      'inputGroupSelect01': inputGroupSelect01,      
      'name': name,
      'address': address,
      'tel': tel
       })

   return jsonify({'result':'success', 'msg': '주문완료'})



@app.route('/templates', methods=['GET'])
def read_orders():
   orders = list(db.orderCollection.find({}, {'_id': False}))
   # print(orders)
   return jsonify({
      'result':'success',
      'msg': '잘 받아왔습니다.',
      'data' : orders
   })


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
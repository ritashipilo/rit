from flask import Flask, render_template, request ,url_for,redirect,jsonify
app = Flask(__name__)
app.json.ensure_ascii=False
product= [{"id":1,'name':'Видеокарты'},
              {"id":2,'name':'Мат. платы'}]
users={
        "login":'admin',
        "pass":'12345'
      }
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/catalog')
def catalog():
    return render_template('catalog.html',product=product) 
@app.route('/add')
def add():
    goods = [[1,'card'],[2,'mouse']]
    return render_template('add.html',goods=goods)
@app.route('/api/product' , methods=['GET'])
def api_product():
    return jsonify (product)
@app.route('/api/product/<int:id>',methods=['GET'])
def api_products(id):
   for products in product:
       if products['id']==id:
           return jsonify(products)
       return jsonify({'error1':f"Товар {id} не найден"})
   
@app.route('/login')
def login():
   return render_template('login.html')
@app.route('/api/login',methods=["POST"])
def api_login():
    data = request.get_json()
    login = data.get("login")
    password = data.get("password")
    if not isinstance(login,str) or not isinstance(password,str):
        return jsonify({
            "success":False, 
            "message":"Введите логин или пароль"
        }),400
    if login==users['login'] and password== users['pass']:
        return jsonify({
            "success":True,
            "message":"Авторизация успешна",
            "redirect":url_for('catalog')
        })
    return None
if __name__=='__main__':
    app.run()
    
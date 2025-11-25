from flask import Flask,render_template,request
import joblib

app = Flask(__name__)  
# 固定写法，初始化你的 Flask App
# 创建整个 Web 应用，所有 route 都会登记在这个 app 上。
# Flask = 一个 Python 写网页（后端）的工具包，里面包含一堆处理 URL、请求、返回 HTML 和 JSON 的函数。

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    q = request.form.get("q")
    print(q)
    return(render_template("main.html"))

@app.route("/dbs",methods=["GET","POST"])
def dbs():
    return(render_template("dbs.html"))

@app.route("/dbs_prediction",methods=["GET","POST"])
def dbs_prediction():
    q=float(request.form.get("q"))
    model = joblib.load("dbs.pkl")
    r=model.predict([[q]])
    return(render_template("dbs_prediction.html",r=r[0][0]))

if __name__ == "__main__":
    app.run()
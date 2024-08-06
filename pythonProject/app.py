from flask import Flask, request, render_template, url_for, redirect, make_response, json, jsonify, abort

# 用当前脚本名称实例化Flask对象，方便flask从该脚本文件中获取需要的内容
app = Flask(__name__)


#程序实例需要知道每个url请求所对应的运行代码是谁。
#所以程序中必须要创建一个url请求地址到python运行函数的一个映射。
#处理url和视图函数之间的关系的程序就是"路由"，在Flask中，路由是通过@app.route装饰器(以@开头)来表示的
@app.route("/")
#url映射的函数，要传参则在上述route（路由）中添加参数申明
def index():
    return "Hello index World!"


# 直属的第一个作为视图函数被绑定，第二个就是普通函数
# 路由与视图函数需要一一对应

# methods参数用于指定允许的请求格式
# 常规输入url的访问就是get方法
@app.route("/hello", methods=['GET', 'POST'])
def hello():
    return "Hello World!"


def hello2():
    return "Hello2 World!"


app.add_url_rule("/hello2", 'hello2', hello2)


# 注意路由路径不要重名，映射的视图函数也不要重名
@app.route("/hi", methods=['POST'])
def hi():
    return "Hi World!"


# 可以在路径内以/<参数名>的形式指定参数，默认接收到的参数类型是string

'''#######################
以下为框架自带的转换器，可以置于参数前将接收的参数转化为对应类型
string 接受任何不包含斜杠的文本
int 接受正整数
float 接受正浮点数
path 接受包含斜杠的文本
########################'''


@app.route("/func1/<int:id>", )
def func1(id):
    if id == 1:
        return 'first'
    elif id == 2:
        return 'second'
    elif id == 3:
        return 'thrid'
    else:
        return 'hello world!'


# 我们也可以在路由中修改endpoint（当视图函数名称很长时适用）
# 相当于为视图函数起别名，简而言之，endpoint是url的名字
@app.route('/func2', endpoint='our_set')
def func2():
    return 'Hello func2!'


#即使修改endpoint为其他视图函数名，依然是绑定其正下方的视图函数，说明endpoint作用于url：
@app.route('/func3', endpoint='Test')
def test():
    return 'None'


def Test():
    return 'World!'


@app.route("/funcRequest", methods=['GET', 'POST'])
# url映射的函数，要传参则在上述route（路由）中添加参数申明
def funcRequest():
    if request.method == 'GET':
        # 想要html文件被该函数访问到，首先要创建一个templates文件，将html文件放入其中
        # 该文件夹需要被标记为模板文件夹，且模板语言设置为jinja2
        return render_template('index.html')
    # 此处欲发送post请求，需要在对应html文件的form表单中设置method为post
    elif request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        return name + " " + password


'''
想要在正常执行的代码的前、中、后时期，强行执行一段我们想要执行的功能代码，便要用到钩子函数——用特定装饰器装饰的函数。
before_request：在每一次请求之前调用；
该钩子函数表示每一次请求之前，可以执行某个特定功能的函数；执行顺序是先绑定的先执行；
并且先执行 flask app 的 before_request, 再执行 blueprint 的 before_request；
一般用于检验用户权限、请求是否合法等场景；
'''

'''
@app.before_request
def before_request_a():

    print('I am in before_request_a')
    return 'I am in before_request_a'


@app.before_request
def before_request_b():
    print('I am in before_request_b')
    return 'I am in before_request_b'

# @app._got_first_request
# def before_first_request_func():
#     return 'I am in before_first_request_func'
#
# @app._got_first_request
# def before_first_request_func2():
#     return 'I am in before_first_request_func2'

'''


@app.after_request
def after_request_a(response):
    print('I am in after_request_a')
    # 该装饰器接收response参数，运行完必须归还response，不然程序报错
    return response


# @app.after_request
# def after_request_b(response):
#     print('I am in after_request_b')
#     return response

@app.teardown_request
def teardown_request_a(exc):
    print('I am in teardown_request_a')


# @app.teardown_request
# def teardown_request_b(exc):
#     print('I am in teardown_request_b')

#重定向
@app.route('/redirectfunc')
def redirectfunc():
    return redirect(url_for('beiRedirect'))


@app.route('/beiRedirect')
def beiRedirect():
    print('beiRedirect-----------ing-----------')
    return 'beiRedirect'


@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('beiRedirect2'))
    else:
        return redirect(url_for('hello_guest', guest=name))


@app.route('/beiRedirect2')
def beiRedirect2():
    print('beiRedirect2-----------ing-----------')
    return 'beiRedirect2'


@app.route('/guest/<guest>')
def hello_guest(guest):
    print('hello_guest-----------ing-----------')
    return 'Hello %s as Guest' % guest


@app.route("/jsonFunc")
def jsonFunc():
    data = {
        'name': '张三'
    }
    # json.dumps 将一个python数据结构转化为json
    # json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False
    # 生成一个response响应对象，而不是直接return来返回响应对象，便于执行更多的后续操作
    response = make_response(json.dumps(data, ensure_ascii=False))
    # 修改数据的MIME标准类型为json（在发送数据前会先发送该类型）
    response.mimetype = 'application/json'
    return response


# 在Flask的config是一个存储了各项配置的字典
# 该操作是进行等效于ensure_ascii=False的配置
app.config['JSON_AS_ASCII'] = False


@app.route("/jsonifyFunc")
def jsonifyFunc():
    data = {
        'name': '张三'
    }
    return jsonify(data)


@app.route("/bortFunc", methods=['GET', 'POST', 'PUT', 'DELETE'])
def bortFunc():
    if request.method == "PUT":
        return "bortfunc get"
    elif request.method == "POST":
        name = request.form.get('name')
        pwd = request.form.get('password')
        return name + "--------- " + pwd
    else:
        print('not get not post')
        abort(404)


# 自定义错误处理方法,将404这个error与Python函数绑定
# 当需要抛出404error时，将会访问下面的代码
@app.errorhandler(404)
def handle_404_error(err):
    # return "发生了错误，错误情况是：%s"%err
    # 自定义一个界面
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # request.args.get('name')
        return render_template('login.html')
    else:
        name = request.form.get('name')
        pwd = request.form['password']
        if name == 'admin':
            return redirect(url_for('success', name=name))
        else:
            return 'hello' + name + '你的密码是：' + pwd


@app.route('/success/<name>')
def success(name):
    return 'hello' + name + '-----------------'

@app.route('/initialtemplate')
def initialtemplate():
    return '<html><body><h1>"Hello initial template"</h1></body></html>'

@app.route('/initialtemplate2')
def initialtemplate2():
    return render_template('initialtemplate2.html')


@app.route('/Jinja2Func/<user>')
def Jinja2Func(user):
    dict = {'phy': 59, 'che': 60, 'maths': 90}
    return render_template('Jinja2Func.html', name=user,result = dict)

@app.route('/staticFunc')
def staticFunc():
    return render_template('staticFile.html')

@app.route('/formOperationFunc', methods=['GET', 'POST'])
def formOperationFunc():
    if request.method == 'GET':
        return render_template('formOperationFunc.html')
    else:
        dict = {'name': request.form.get('name'),'password': request.form.get('password')}
        return render_template('formOperationListFunc.html',list=dict)


if __name__ == '__main__':
    #view_functions------endpoint与view_functions视图函数的对应情况；
    #url_map-------------当前url与endpoint的绑定情况；
    print(app.view_functions)
    # 启动一个本地开发服务器，激活该网页
    app.run()

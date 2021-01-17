from flask import Flask

def create_app():
    app = Flask(__name__)
    return app


app = create_app()


@app.route('/')
def hello():
    # testing how paths work
    with open('dir1/dir2/random.txt') as f:
        txt = f.read()
        print(txt)
        return txt
    # return "welcome to iljas flask server!"


if __name__ == "__main__":
    print('main')
    # we could specify a port below with port="123"
    app.run(debug=True, host='0.0.0.0')

# routes.py
from flask import render_template
from flask import Blueprint
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM employees")  # 적절한 쿼리를 실행하여 데이터 가져오기
    data = cur.fetchall()
    cur.close()

    # 가져온 데이터를 HTML 템플릿에 전달
    return render_template('test.html', data=data)

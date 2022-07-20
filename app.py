from flask import Flask, request
from konlpy.tag import Mecab
from g2pk import G2p

app = Flask(__name__)


mecab = Mecab()
g2p = G2p()


@app.route('/')
def hello_world():
    return {'result': 'hello world!'}


@app.route('/mecab')
def get_mecab():
    k_str = request.args.get('q', u'영등포구청역에 있는 맛집 좀 알려주세요.')
    morphs = mecab.morphs(k_str)
    nouns = mecab.nouns(k_str)
    pos = mecab.pos(k_str)
    return {'morphs': morphs, 'nouns': nouns, 'pos': pos}


@app.route('/g2pk')
def run_g2pk():
    k_str = request.args.get('q', u'신을 신고 얼른 동사무소에 가서 혼인 신고 해라')
    print(k_str)
    res = g2p(k_str)
    return {'result': res}

import os

import time
from flask import Flask, request, render_template
from konlpy.tag import Kkma, Komoran, Hannanum, Mecab, Okt

'''
   2020. 05. 26. ZS
   * CentOS 8 + gunicorn + Flask + Nginx *
   기존 Template만 가지고 내부모델 konlpy로 교체하여
   Web Application으로 변형 작업
   
   ★ 별도의 라디오버튼이나 select button을 활용하여
   형태소분석기를 고를 수 있도록 구현하기
'''

# 형태소 분석기 라이브러리 호출
# 로딩 속도를 고려해 미리 띄워두기
kkma = Kkma()
komoran = Komoran()
hannanum = Hannanum()
mecab = Mecab()
okt = Okt()

selectdic = {"Kkma": kkma, "Komoran": komoran, "Hannanum": hannanum, "Mecab": mecab, "Okt": okt}

# WEB APP
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('intro.html')


# Konlpy 형태소 분석 호출부
def pos(tagger, text):
    result = tagger.pos(text)
    return result


@app.route('/tagging', methods=['GET', 'POST'])
def input_text():
    if request.method == 'POST':
        start_time = time.time()
        print(start_time)
        select_tagger = request.form['select_btn']
        print(select_tagger)
        input_text = request.form['text']
        print(input_text)
        # 선택한 형태소 분석기 형태와 입력 텍스트를 같이 넘김
        output_text = pos(selectdic[select_tagger], input_text)
        end_time = time.time()
        print(output_text)
        print('소요 시간 :' + str(end_time - start_time))
        return render_template('tagging.html', output=output_text)
    return render_template('tagging.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')


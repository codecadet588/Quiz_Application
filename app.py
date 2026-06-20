from flask import Flask, render_template, request, session
import requests
import html
import random
import os
import sqlite3

app=Flask(__name__)
app.secret_key=os.urandom(24)

def fetch_api(amount, category, difficulty):
    url=(f"https://opentdb.com/api.php?amount={amount}&category={category}&difficulty={difficulty}&type=multiple")
    response=requests.get(url)
    return response.json()['results']

# Creating Database
def create_db():
    conn=sqlite3.connect('Records.db')
    c=conn.cursor() 
    # cretaing a table if does not exist already
    c.execute('''
              CREATE TABLE IF NOT EXISTS Records(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  percentage INTEGER
              )
              ''')
    conn.commit()
    conn.close()
      
create_db()
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/startquiz', methods=["POST"])
def startquiz():
    name=request.form.get('name', 'Anoynomous')
    amount=int(request.form.get('amount', 3))
    category=int(request.form.get('category',18))
    difficulty=request.form.get('difficulty','easy')
        
    questions_list=[]
    questions=fetch_api(amount, category, difficulty)
    for q in questions:
        question=html.unescape(q['question'])
        correct_answer=html.unescape(q['correct_answer'])
        incorrect_answer=[html.unescape(ans) for ans in q['incorrect_answers']] 
        choices=[correct_answer]+incorrect_answer
        random.shuffle(choices)
        
        questions_list.append({
            'question':question,
            'choices':choices,
            'correct':correct_answer                 
        })
    session['name']=name
    session['questions_list']=questions_list
          
    return render_template('quizstart.html', name=name, questions_list=questions_list)

@app.route('/submitquiz', methods=["POST"])
def submitquiz():
    
    score=0
    questions_list=session.get('questions_list', [])
    name=session.get('name', 'Anoynomous')
    
    for index,question in enumerate(questions_list):
        question_num = index + 1
        user_answer = request.form.get(f'q{question_num}')
        
        if user_answer==question['correct']:
            score+=1
    total_questions = len(questions_list)
    percentage = (score * 100) // total_questions

    conn=sqlite3.connect('Records.db')
    c=conn.cursor()
    c.execute('INSERT INTO Records (name, percentage) VALUES (?, ?) ', (name, percentage))
    conn.commit()
    conn.close()
    return render_template('result.html',score=score,percentage=percentage, name=name,questions_list=questions_list )


@app.route('/Previous_records')
def previous_records():

    conn=sqlite3.connect('Records.db')
    c=conn.cursor()
    c.execute('SELECT name, percentage FROM Records ORDER BY id DESC')
    records=c.fetchall()
    conn.close()
    return render_template('previous_records.html', records=records)
    
    
    

if __name__=="__main__":
    app.run(debug=True)






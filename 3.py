import csv
import json

QUESTIONS_FILE = 'file.json'
RESULTS_FILE = 'results.csv'

# قراءة الأسئلة والأجوبة من ملف JSON
file= open(QUESTIONS_FILE, 'r')
data = json.load(file)
questions = [(q['q'], q['a']) for q in data]
file.close()
# طرح الأسئلة على المستخدم وجمع الإجابات
username = input("enter your name ")
c = 0
for q, a in questions:
    user_answer = input(q)
    if user_answer == a:
        c += 1
score = f"{c}/{20}"
print(f"{username}::: {score}")

# حفظ اسم المستخدم والنتيجة في ملف CSV
result = [username, str(c), "20"]

file=open(RESULTS_FILE, 'w')
writer = csv.writer(file)
writer.writerow(result)
file.close()

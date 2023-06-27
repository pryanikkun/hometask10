from flask import Flask
import json

app = Flask(__name__)


@app.route('/')
def page_main():
    string = f"<pre>\n"
    for candidate in data:
        string += f'Имя кандидата - {candidate["name"]}\n' \
                  + f'Позиция кандидата - {candidate["position"]}\n' \
                  + f'Навыки - {candidate["skills"]}\n'+ '\n'
    string += f"</pre>\n"
    return string


@app.route("/candidate/<int:cid>")
def page_candidate(cid):
    candidate = data[cid-1]
    string = f"<img src={candidate['picture']}>\n" + '\n<pre>\n'\
             + f'Имя кандидата - {candidate["name"]}\n' \
             + f'Позиция кандидата - {candidate["position"]}\n' \
             + f'Навыки - {candidate["skills"]}\n'\
             + f"</pre>\n"
    return string


@app.route("/skill/<skill>")
def page_skills(skill):
    string = f"<pre>\n"
    for candidate in data:
        if skill.lower() in candidate['skills'].lower():
            string += f'Имя кандидата - {candidate["name"]}\n' \
                    + f'Позиция кандидата - {candidate["position"]}\n' \
                    + f'Навыки - {candidate["skills"]}\n' + '\n'
    string += f"</pre>\n"
    return string


file = open('candidates.json', encoding='utf-8')
data = json.load(file)
file.close()

app.run()

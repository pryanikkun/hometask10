from flask import Flask
import utils

app = Flask(__name__)


@app.route('/')
def page_main():
    string = f"<pre>\n"
    for candidate in list_candidates:
        string += candidate.get_name_pos_skills()
    string += f"\n</pre>\n"
    return string


@app.route("/candidate/<int:cid>")
def page_candidate(cid):
    candidate = list_candidates[cid-1]
    string = candidate.get_img_nps()
    return string


@app.route("/skill/<skill>")
def page_skills(skill):
    string = f"<pre>\n"

    for candidate in list_candidates:
        if skill.lower() in candidate.skills.lower().split(', '):
            string += candidate.get_name_pos_skills()
    string += f"</pre>\n"
    return string


list_candidates = utils.make_objects()

app.run()

from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    candidates = utils.load_candidates_from_json('candidates.json')
    return render_template('list.html', items=candidates)

@app.route("/candidate/<candidat_id>")
def page_profile(candidat_id):
    candidat = utils.get_candidate(candidat_id)
    return render_template('single.html', item=candidat)

@app.route("/search/<candidate_name>")
def page_search(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', items=candidates, len_item=len(candidates))

@app.route("/skill/<skill_name>")
def page_skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template('skill.html', items=candidates, len_item=len(candidates))

if __name__ == '__main__':
    app.run()

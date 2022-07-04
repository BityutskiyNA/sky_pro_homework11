import json


def load_candidates_from_json(path):
    """
     – возвращает список всех кандидатов
    """
    file = open(path, encoding="utf-8")
    candidates = json.load(file)
    return candidates


def get_candidate(candidate_id):
    """
    – возвращает одного кандидата по его id
    """
    candidates = load_candidates_from_json("candidates.json")
    for candidat in candidates:
        if str(candidat['id']) == candidate_id:
            return candidat

    return None


def get_candidates_by_name(candidate_name):
    """
    ` – возвращает кандидатов по имени
    """
    found_candidates = []
    candidates = load_candidates_from_json("candidates.json")
    for candidat in candidates:
        if candidate_name in candidat['name']:
            found_candidates.append(candidat)
    return found_candidates


def get_candidates_by_skill(skill_name):
    """
    – возвращает кандидатов по навыку
    """
    found_candidates = []
    candidates = load_candidates_from_json("candidates.json")
    for candidat in candidates:
        candidat_skill = candidat['skills'].upper()
        candidat_skill = candidat_skill.split(', ')
        if candidat_skill.count(skill_name.upper()) > 0:
            found_candidates.append(candidat)
    return found_candidates

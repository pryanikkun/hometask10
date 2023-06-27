class CandidatesGetter:

    def __init__(self, dict_candidate):
        self.id = dict_candidate['id']
        self.name = dict_candidate['name']
        self.picture = dict_candidate['picture']
        self.position = dict_candidate['position']
        self.skills = dict_candidate['skills']

    def get_name_pos_skills(self):
        string = f'Имя кандидата - {self.name}\n' \
             + f'Позиция кандидата - {self.position}\n' \
             + f'Навыки - {self.skills}\n'
        return string

    def get_img_nps(self):
        string = f"<img src={self.picture}>\n" + '\n<pre>\n'\
             + f'Имя кандидата - {self.name}\n' \
             + f'Позиция кандидата - {self.position}\n' \
             + f'Навыки - {self.skills}\n' + '\n</pre>\n'
        return string

    def __repr__(self):
        return f'Я кандидат {self.name}'

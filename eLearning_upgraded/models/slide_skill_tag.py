from odoo import models, fields
from random import randint
import csv, os
#from google.cloud import bigquery


class SlideChannelTag(models.Model):
    _name = 'slide.skill.tag'
    _description = 'Channel/Course Skill'
    _order = 'sequence asc'

    name = fields.Char('Name', required=True, translate=True, readonly=True)
    external_id = fields.Char('External ID', required=True, translate=True, readonly=True)
    sequence = fields.Integer('Sequence', default=10, index=True, required=True)

    _sql_constraints = [
        ('slide_skill_unique', 'UNIQUE(external_id)', 'A skill must be unique!'),
    ]

    # Update the skills, this function is called automatically every week 
    def update_skills(self):

        # POSSIBLE CODE FOR BIGQUERY CONNECTION
        #client = bigquery.Client()

        #query = """
        #    SELECT name, id
        #    FROM `wizelake-non-prod.wizeline_os.skills`
        #   """
        #query_job = client.query(query)  # Make an API request.

        #for row in query_job:
            # Row values can be accessed by field name or index.
        #    skill_list.append({'name' : row[0], 'external_id': row[1]})

        skills_list = []
        try:
            with open('src/user/imports/skills.csv', mode='r') as f:
                csv_reader = csv.reader(f, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if not line_count: 
                        line_count += 1
                        continue
                    skills_list.append({'name': row[0], 'external_id': row[1]})
        except FileNotFoundError:
            skills_list = [{'name': 'Sequelize', 'external_id': 'a_1'}, {'name': 'Haskell', 'external_id': 'a_2'},
                {'name': 'Jest', 'external_id': 'a_3'}, {'name': 'Rust', 'external_id': 'a_4'}, {'name': 'Grunt', 'external_id': 'a_5'},
                {'name': 'Gulp', 'external_id': 'a_6'}, {'name': 'Python', 'external_id': 'a_7'}, {'name': 'C++', 'external_id': 'a_8'}]
        for skill in skills_list:
            skill_vals = {
                'name': skill['name'],
                'external_id': skill['external_id']
            }
            course_skill_id = self.env['slide.skill.tag'].search([('external_id', '=', skill['external_id'])])
            if not len(course_skill_id):
                self.env['slide.skill.tag'].create(skill_vals)

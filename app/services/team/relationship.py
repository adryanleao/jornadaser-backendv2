from app import models


def clear_team_students(item_id):
    models.User.query.filter(
        models.User.team_id == item_id
    ).delete()

def create_team_students(item, dict_body):
    if 'students' in dict_body:
        clear_team_students(item.id)
        for student in dict_body["students"]:
            user = models.User.get_by_id(student['id'])
            if user:
                user.team_id = item.id
                user.update()
                item.students.append(
                    user
                )
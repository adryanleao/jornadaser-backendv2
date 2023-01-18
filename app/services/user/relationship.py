from app import models


def clear_user_institutions(item_id):
    models.UserInstitution.query.filter(
        models.UserInstitution.user_id == item_id
    ).delete()


def clear_user_secretaries(item_id):
    models.UserSecretary.query.filter(
        models.UserSecretary.user_id == item_id
    ).delete()

def create_user_institutions(item, dict_body):
    if 'institutions' in dict_body:
        clear_user_institutions(item.id)
        for institution in dict_body["institutions"]:
            if models.Institution.get_by_id(institution['id']):
                dict_relationship = {
                    "user_id": item.id,
                    "institution_id": institution["id"]
                }
                item.institutions.append(
                    models.UserInstitution().create_item(dict_relationship).save()
                )


def create_user_secretaries(item, dict_body):
    if 'secretaries' in dict_body:
        clear_user_secretaries(item.id)
        for secretary in dict_body["secretaries"]:
            if models.Secretary.get_by_id(secretary['id']):
                dict_relationship = {
                    "user_id": item.id,
                    "secretary_id": secretary["id"]
                }
                item.institutions.append(
                    models.UserSecretary().create_item(dict_relationship).save()
                )

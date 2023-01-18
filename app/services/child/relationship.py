from app import models


def clear_child_parents(item_id):
    models.ChildKinship.query.filter(
        models.ChildKinship.child_id == item_id
    ).delete()

def create_child_parents(item, dict_body):
    if 'parents' in dict_body:
        clear_child_parents(item.id)
        for parent in dict_body["parents"]:
            if models.User.get_by_id(parent['id']):
                dict_relationship = {
                    "child_id": item.id,
                    "parent_id": parent["id"],
                    "kinship": parent["kinship"]
                }
                item.parents.append(
                    models.ChildKinship().create_item(dict_relationship).save()
                )
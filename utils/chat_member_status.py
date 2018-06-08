def can_delete(chat, user_id):
    return chat.get_member(user_id).can_delete_messages


def can_restrict_members(chat, user_id):
    return chat.get_member(user_id).can_restrict_members

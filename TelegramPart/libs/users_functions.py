def find_by_id(users, id):
    for x in users:
        if x.id == id:
            return x
    return None


def find_index_by_id(users, id):
    for i in range(len(users)):
        if users[i].id == id:
            return i
    return -1






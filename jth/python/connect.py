from crud_module import *
from select_all import select
import requests

url = "https://jsonplaceholder.typicode.com/posts"
datas = requests.get(url).json()

if __name__ == '__main__':
    save_query = "insert into post(userId, title, body) values(%s, %s, %s)"
    for number in range(len(datas)):
        save_params = (datas[number]['userId'], datas[number]['title'], datas[number]['body'])
        # save(save_query, save_params)

    find_by_id_query = "select userId, title, body from post where userId = %s"
    find_by_id_params = 1,
    search = find_by_id(find_by_id_query, find_by_id_params)
    print(search)

    delete_query = "delete from post where userId = %s"
    delete_params = 1,
    # delete = delete(delete_query, delete_params)

    find_all_query = "select userId, title, body, id from post"
    members = find_all(find_all_query)

    select_list = []
    for member in members:
        select_list.append(select(member.get('userId'), member.get('title'), member.get('body'), member.get('id')))

    [print(select.__dict__) for select in select_list]
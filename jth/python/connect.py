from crud_module import *
from select_all import select
import requests

url = "https://jsonplaceholder.typicode.com/posts"
datas = requests.get(url).json()

def check_user_id(user_id):
    find_by_id_query = "select userId, title, body from post where userId = %s"
    find_by_id_params = user_id,
    search = find_by_id(find_by_id_query, find_by_id_params)
    if search is None:
        return None
    else:
        return f'{search.get("userId")}: {search.get("title")}, {search.get("body")}'

def check_id(check):
    find_by_id_query = "select userId, title, body, id from post where id = %s"
    find_by_id_params = check,
    search = find_by_id(find_by_id_query, find_by_id_params)
    if search is None:
        return None
    else:
        return f'userId: {search.get("userId")}/ id: {search.get("id")} = {search.get("title")}, {search.get("body")} 삭제'

class Db:
    def __init__(self, userId, title, body):
        self.userId = userId
        self.title = title
        self.body = body

    @classmethod
    def save_info(cls, **kwargs):
        member = Member(**kwargs).__dict__
        print(member.get("userId"))
        save_query = "insert into post(userId, title, body) values(%s, %s, %s)"
        save_params = member.get('userId'), member.get('title'), member.get('body')
        save(save_query, save_params)
        '''
        # 처음 테이블에 입력할 때 사용
        for number in range(len(datas)):
            save_query = "insert into post(userId, title, body) values(%s, %s, %s)"
            save_params = (datas[number]['userId'], datas[number]['title'], datas[number]['body'])
            save(save_query, save_params)
        '''

    @staticmethod
    def show_info(user_id):
        find_all_by_query = "select userId, title, body, id from post where userId = %s"
        find_all_by_params = user_id,
        members = find_all_by(find_all_by_query, find_all_by_params)
        select_list = []
        for member in members:
            select_list.append(select(member.get('userId'), member.get('title'), member.get('body'), member.get('id')))
        [print(select.__dict__) for select in select_list]

    @staticmethod
    def show_all():
        find_all_query = "select userId, title, body, id from post"
        members = find_all(find_all_query)
        select_list = []
        for member in members:
            select_list.append(select(member.get('userId'), member.get('title'), member.get('body'), member.get('id')))
        [print(select.__dict__) for select in select_list]

    @staticmethod
    def delete_info(check):
        delete_query = "delete from post where Id = %s"
        delete_params = check,
        delete(delete_query, delete_params)

    @staticmethod
    def check_userId(userId: str):
        return check_user_id(userId)

    @staticmethod
    def check_delete(check: int):
        return check_id(check)

class Member(Db):
    pass

# Db.save_info(userId=1000, title="test", body="test")

choose_message = '번호 입력: '
user_message = "userId: "
input_message = "title과 body를 입력하세요: "
delete_message = "id: "
# '''
if __name__ == '__main__':
    # save_query = "insert into post(userId, title, body) values(%s, %s, %s)"
    # for number in range(len(datas)):
    #     save_params = (datas[number]['userId'], datas[number]['title'], datas[number]['body'])
    #     # save(save_query, save_params)
    while True:
        choose = int(input(choose_message))
        if choose == 1:
            user_id = input(user_message)
            title, body = input(f'{input_message} ex)title, body\n'). split(',')
            Db.save_info(userId="1000", title="test", body="test")

        if choose == 2:
            user_id = input(user_message)
            if Db.check_userId(user_id) is None:
                print("일치하는 정보가 없습니다.")
            else:
                Db.show_info(user_id)

        if choose == 3:
            print("전체 목록 보기")
            Db.show_all()

        if choose == 4:
            print("id로 삭제하기")
            check = int(input(delete_message))
            if Db.check_delete(check) is None:
                print("일치하는 정보가 없습니다.")
            else:
                print(Db.check_delete(check))
                Db.delete_info(check)
        if choose == 5:
            break
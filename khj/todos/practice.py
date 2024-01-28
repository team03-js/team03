from crud_module import *
import requests

url = "https://jsonplaceholder.typicode.com/todos"
datas = requests.get(url).json()

# 생성
def create_todos():
    for number in range(len(datas)):
        save_query = "insert into tbl_todos(userId, title, completed) values (%s, %s, %s)"
        save_params = (datas[number]['userId'], datas[number]['title'], datas[number]['completed'])
        save(save_query, save_params)

# 전체 목록
def read_todos():
    read_query = "select * from tbl_todos"
    result = find_all(read_query)
    for row in result:
        print(row)

# 조회
def read_select_todo(todo_id):
    find_id_query = "select * from tbl_todos where id = %s"
    result = find_by_id(find_id_query, todo_id)
    print(result)
    return result


# 수정
def update_todo(todo_id, new_title):
    update_query = "update tbl_todos set title = %s where id = %s"
    # todo_id에 해당하는 id 값을 찾아서 사용하도록 수정
    find_id_query = "select id from tbl_todos where id = %s"
    id_params = (todo_id,)
    id_result = find_by_id(find_id_query, id_params)

    if id_result:
        # id_result가 None이 아닐 때에만 업데이트 수행
        update_params = (new_title, id_result['id'])
        update(update_query, update_params)
    else:
        print(f"{todo_id}가 존재하지 않음")

# 삭제
def delete_todo(todo_id):
    delete_query = "delete from tbl_todos where id = %s"
    delete_params = (todo_id,)
    delete(delete_query, delete_params)


if __name__ == '__main__':
            # # Create
            # create_todos()

            # # Read
            read_todos()
            # read_select_todo(1)


            # # Update
            # update_todo(todo_id=1, new_title="수정된 제목")

            # # Delete
            # delete_todo(todo_id=200)

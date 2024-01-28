from crud_module import *

# posts 내용 추가
# save_many_query = "insert into tbl_posts(userId, title, body) \
#                    values(%s, %s, %s)"
# save_many_params = (
#     (1, 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
#      'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'),
#     (1, 'qui est esse',
#      'est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla'),
#     (1, 'ea molestias quasi exercitationem repellat qui ipsa sit aut',
#      'et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut')
# )
# save_many(save_many_query, save_many_params)

# find_all_query = "select userId, id, title, body from tbl_posts"
# post = find_all(find_all_query)
# print(post)
class Post:
    def __init__(self,userId,id,title,body):
        self.userId = userId
        self.id = id
        self.title = title
        self.body = body

    def list_view():
        find_all_query = "select userId, id, title, body from tbl_posts "
        views = find_all(find_all_query)
        for view in views:
            # print(view)
            view_list = view.get('userId'), view.get('title'), view.get('body')
            print(view_list)
    # Post.list_view()

    def title_view(title_id):
        find_all_by_query = "select userId, title, body, id from tbl_posts where userId = %s"
        find_all_by_params = title_id
        members = find_all_by(find_all_by_query, find_all_by_params)
        for member in members:
            select_list = member.get('userId'), member.get('title')
            print(select_list)

    def delete_view(user_id):
        delete_query = "delete from tbl_posts where id = %s"
        delete_params = user_id
        delete(delete_query, delete_params)


menu_message = '원하는 번호를 입력하세요. \n 1. 전체 조회하기 \n 2. title 목록 조회하기 \n 3. 삭제하기 \n'
title_message = '조회하실 userId를 입력하세요: '
del_message = '삭제하실 글 번호를 입력하세요: '

if __name__ == '__main__':
    while True:
        menu = int(input(menu_message))
        # 전체 목록 조회
        if menu == 1:
            Post.list_view()
            continue

        # userId로 title 조회
        elif menu == 2:
            title_id = int(input(title_message))
            Post.title_view(title_id)
            continue

        # # id로 정보 삭제하기
        elif menu == 3:
            user_id = int(input(del_message))
            Post.delete_view(user_id)
            continue
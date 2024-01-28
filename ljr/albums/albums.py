from crud_module import *
import requests

url = "https://jsonplaceholder.typicode.com/albums"
datas = requests.get(url).json()

        # for number in range(len(datas)):
        #         save_query = "insert into tbl_albums(userId, title) values(%s, %s)"
        #         save_params = (datas[number]['userId'], datas[number]['title'])
        #         save(save_query, save_params)


class Albums:
        def __init__(self, userId, title):
                self.userId = userId
                self.title = title

        @staticmethod
        def insert_albums(userId, title):
                save_query = "insert into tbl_albums(userId, title) values (%s, %s)"
                save_params = (userId, title)
                save(save_query, save_params)

        @staticmethod
        def create_albums():
                for number in range(len(datas)):
                        save_query = "insert into tbl_albums(userId, title) values(%s, %s)"
                        save_params = (datas[number]['userId'], datas[number]['title'])
                        save(save_query, save_params)

        @staticmethod
        def read_albums():
                find_all_query = "select * from tbl_albums"
                albums_all = find_all(find_all_query)
                for albums in albums_all:
                 print(albums)

        @staticmethod
        def read_choice_album(album_id):
                select_by_id_query = "select * from tbl_albums where id = %s"
                result = find_by_id(select_by_id_query, (album_id,))
                print(f"Result: {result}")
                return result
        @staticmethod
        def update_album_title(album_id, new_title):
                update_query = "update tbl_albums set title = %s where id = %s"
                update_params = (new_title, album_id)
                update(update_query, update_params)

        @staticmethod
        def delete_album(album_id):
                delete_query = "delete from tbl_albums where id = %s"
                delete_params = (album_id,)
                delete(delete_query, delete_params)


if __name__ == '__main__':

        # 데이터 하나 추가하기
        Albums.insert_albums(333, "1234")

        # 전체 데이터 추가
        # Albums.create_albums()

        # 전체 데이터 불러오기
        # Albums.read_albums()

        # 조회하기
        # Albums.read_choice_album(22)

        # 수정하기
        # Albums.update_album_title("2","1111" )

        # 삭제하기
        # Albums.delete_album(1)



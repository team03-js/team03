from crud_module import *

class Photo :
    def __init__(self, newUpdate, albumId, title, url, thumbnailUrl):
        self.newUpdate = newUpdate
        self.albumId = albumId
        self.title = title
        self.url = url
        self.thumbnailUrl = thumbnailUrl

    # 추가
    @classmethod
    def insertPhotos(cls, albumId, title, url, thumbnailUrl):
        save_query = "insert into tbl_photos(albumId, title, url, thumbnailUrl) \
                      values (%s, %s, %s, %s)"
        save_params = (albumId, title, url, thumbnailUrl)
        save(save_query, save_params)

    @staticmethod
    # 아이디로 하나만 조회
    def getPhoto(albumId):
        find_by_id_query = "select id, albumId, url, thumbnailUrl from tbl_photos where id = %s"
        find_by_id_params = albumId,
        photo = find_by_id(find_by_id_query, find_by_id_params)
        photo_all = photo.get("id"), photo.get("albumId"), photo.get("url"), photo.get("thumbnailUrl")
        print(photo_all)

    # 전체조회
    @staticmethod
    def getAllPhotos():
        find_all_query = "select id, albumId, url, thumbnailUrl from tbl_photos"
        photos = find_all(find_all_query)
        for photo in photos:
            print(photo)

    # 수정
    @staticmethod
    def updatePhoto(newUpdate, albumId):
        update_query = "update tbl_photos set url = %s where id like %s"
        update_params = [newUpdate, albumId]
        update(update_query, update_params)

    # 삭제
    @staticmethod
    def deletePhoto(albumId):
        delete_query = "delete from tbl_photos where id like %s"
        delete_params = [albumId]
        delete(delete_query, delete_params)

# Photo.insertPhotos(2, "testTitle1", "testUrl1", "testThumbnailUrl1")
# Photo.getPhoto(3)
# Photo.getAllPhotos()
# Photo.updatePhoto("google.com", 6)
# Photo.deletePhoto(4)
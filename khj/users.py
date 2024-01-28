from crud_module import *
from class_users import Users
from class_address import Address
from class_geo import Geo
from class_company import Company


if __name__ == '__main__':
    save_many_query = "insert into tbl_users(name, username, email, phone, website)\
                        values(%s, %s, %s, %s, %s)"
    save_many_params = (
        # ("Leanne Graham","Bret","Sincere@april.biz","1-770-736-8031 x56442","hildegard.org"),
        # ("Ervin Howell", "Antonette","Shanna@melissa.tv", "010-692-6593 x09125","anastasia.net"),
        # ("Clementine Bauch", "Samantha", "Nathan@yesenia.net","1-463-123-4447", "ramiro.info"),
        # ("Patricia Lebsack","Karianne","Julianne.OConner@kory.org", "493-170-9623 x156", "kale.biz"),
        ("Chelsey Dietrich", "Kamren", "Lucio_Hettinger@annie.ca", "(254)954-1289",  "demarco.info"),
    )

    save_many(save_many_query, save_many_params)

    find_by_id_query = "select id from tbl_users where id = %s"
    find_by_id_params = 5,
    users = find_by_id(find_by_id_query, find_by_id_params)
    users_id = users.get("id")


    save_many_query = "insert into tbl_address(street, suite, city, zipcode, users_id) \
                       value(%s, %s, %s, %s, %s)"
    save_many_params = (
        # ("Kulas Light", "Apt. 556", "Gwenborough", "92998-3874", users_id),
        # ("Victor Plains", "Suite 879", "Wisokyburgh", "90566-7771", users_id),
        # ("Douglas Extension", "Suite 847", "McKenziehaven", "59590-4157", users_id),
        # ("Hoeger Mall", "Apt. 692", "South Elvis", "53919-4257", users_id),
        ("Skiles Walks", "Suite 351", "Roscoeview", "33263", users_id),
    )

    save_many(save_many_query, save_many_params)


    find_by_id_query = "select id from tbl_address where id = %s"
    find_by_id_params = 5,
    address = find_by_id(find_by_id_query, find_by_id_params)
    address_id = address.get("id")

    save_many_query = "insert into tbl_geo(lat, lng, address_id)\
                        value(%s, %s, %s)"
    save_many_params =(
        # (-37.3159, 81.1496, address_id ),
        # (-68.6102, -47.0653, address_id ),
        # (-68.6102, -47.0653, address_id ),
        # (29.4572, -164.2990, address_id ),
        (-31.8129, 62.5342, address_id ),
    )
    save_many(save_many_query, save_many_params)

    find_by_id_query = "select id from tbl_users where id = %s"
    find_by_id_params = 5,
    users = find_by_id(find_by_id_query, find_by_id_params)
    users_id = users.get("id")

    save_many_query = "insert into tbl_company(name, catchPhrase, bs, users_id)\
                        value(%s, %s, %s, %s)"
    save_many_params =(
        # ("Leanne Graham", "Multi-layered client-server neural-net", "harness real-time e-markets", users_id),
        # ("Ervin Howell", "Proactive didactic contingency", "synergize scalable supply-chains", users_id),
        # ("Clementine Bauch", "Face to face bifurcated interface", "e-enable strategic applications", users_id),
        # ("Patricia Lebsack", "Multi-tiered zero tolerance productivity","transition cutting-edge web services", users_id),
        ("Chelsey Dietrich", "User-centric fault-tolerant solution","revolutionize end-to-end systems", users_id),
    )
    save_many(save_many_query, save_many_params)
from crud_module import *
from class_todos import Todos

if __name__ == '__main__':
    save_many_query = "insert into tbl_todos(userId, title, completed)\
                       values(%s, %s, %s)"
    save_many_params = (
        (1, "delectus aut autem", False),
        (1, "quis ut nam facilis et officia qui", False),
        (1, "fugiat veniam minus", False),
        (1, "et porro tempora", True),
        (1, "laboriosam mollitia et enim quasi adipisci quia provident illum", False),
        (1, "qui ullam ratione quibusdam voluptatem quia omnis", False),
        (1, "illo expedita consequatur quia in", False),
        (1, "quo adipisci enim quam ut ab", True),
        (1, "molestiae perspiciatis ipsa", False),
        (1, "illo est ratione doloremque quia maiores aut", True),
        (1, "vero rerum temporibus dolor", True),
        (1, "ipsa repellendus fugit nisi", True),
        (1, "et doloremque nulla", False),
        (1, "repellendus sunt dolores architecto voluptatum", True),
        (1, "ab voluptatum amet voluptas", True),
        (1, "accusamus eos facilis sint et aut voluptatem", True),
        (1, "quo laboriosam deleniti aut qui", True),
        (1, "dolorum est consequatur ea mollitia in culpa", False),
        (1, "molestiae ipsa aut voluptatibus pariatur dolor nihil", True),
        (1,"ullam nobis libero sapiente ad optio sint", True),
    )
    save_many(save_many_query, save_many_params)

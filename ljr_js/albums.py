from crud_module import *
from class_albums import Albums



save_many_query = "insert into tbl_albums(userId, title)\
                    values(%s, %s)"
save_many_params = (
        (1, "quidem molestiae enim"),
        (1, "sunt qui excepturi placeat culpa"),
        (1, "omnis laborum odio"),
        (1, "non esse culpa molestiae omnis sed optio"),
        (1, "eaque aut omnis a"),
        (1, "natus impedit quibusdam illo est"),
        (1, "quibusdam autem aliquid et et quia"),
        (1, "qui fuga est a eum"),
        (1, "saepe unde necessitatibus rem"),
        (1, "distinctio laborum qui"),
        (2, "quam nostrum impedit mollitia quod et dolor"),
        (2, "consequatur autem doloribus natus consectetur"),
        (2, "ab rerum non rerum consequatur ut ea unde"),
        (2, "ducimus molestias eos animi atque nihil"),
        (2, "ut pariatur rerum ipsum natus repellendus praesentium"),
        (2, "voluptatem aut maxime inventore autem magnam atque repellat"),
        (2, "aut minima voluptatem ut velit"),
        (2, "nesciunt quia et doloremque"),
        (2, "velit pariatur quaerat similique libero omnis quia"),
        (2, "voluptas rerum iure ut enim"),
)

save_many(save_many_query, save_many_params)


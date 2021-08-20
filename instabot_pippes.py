from instapy import InstaPy

session = InstaPy(username= "pippes.pizza", password= "R3boll3d")
session.login()

session.set_relationship_bounds(enabled = True, max_followers= 1000)
session.set_do_follow(True, percentage= 100)
session.like_by_tags(["pizza","pizzavacio","delivery","foodporn" , "quintaregion" , " Viña" , "Valpo" , "pizzacasera", "pizzatime"], amount= 3)

session.end


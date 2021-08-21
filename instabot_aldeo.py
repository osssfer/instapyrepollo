from instapy import InstaPy

my_username = "aldeocl"
my_password ="ventus123"


session = InstaPy(username= my_username, password=my_password )
session.login()

session.set_relationship_bounds(enabled = True, max_followers= 1000)
session.set_do_follow(True, percentage= 100)
session.like_by_tags(["pizza","pizzavacio","delivery","foodporn" , "quintaregion" , " Viña" , "Valpo" , "pizzacasera", "pizzatime"], amount= 3)

session.end


from instagrapi import Client

cl = Client()
cl.login('nadezhda_timofeeva2474', "Ytp1ID6iOc")

user_id = cl.user_id_from_username("figurina_nao_lladro")
medias = cl.user_medias(user_id, 200)
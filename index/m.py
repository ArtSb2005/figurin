from instagrapi import Client

cl = Client()
cl.login('valerija_nazarova5669', "Hjd8EN4aUy")

user_id = cl.user_id_from_username("figurina_nao_lladro")
medias = cl.user_medias(user_id, 200)
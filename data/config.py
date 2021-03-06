from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста
channel_name = env.str("channel_name")  # Название для основного канала
donatlink = env.str("donatlink")  # Линк для доната

banned_users = env.list("BLOCKLIST")  # Тест для блоклиста
import discord
from config.token import TOKEN
from config.config import ROLES


class Testbot(discord.Client):
    async def on_ready(self):
        print(f'Bot {self.user} ready')

    async def on_message(self, message):
        chanel = None
        print(f'Message from {message.author}: {message.content}')
        roles = message.author.roles
        role_list = [i.id for i in roles]
        if ROLES['Holder'] in role_list and ROLES['Member'] in role_list:
            print(f'У пользователя роли Holder и Member')  # Заглушка полная авторизация
        elif ROLES['Team'] in role_list or ROLES['Founder'] in role_list:
            print(f'У пользователя роль Team или Founder')  # Заглушка полная авторизация
        else:
            print('Отказ в авторизации')  # Заглушка для отказа


intents = discord.Intents.default()
intents.message_content = True

client = Testbot(intents=intents)
client.run(TOKEN)

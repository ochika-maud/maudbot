import discord
import os
#import ffmpeg
import aiohttp
from discord import app_commands

# インテントの生成
intents = discord.Intents.default()
intents.message_content = True

# クライアントの生成
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# discordと接続した時に呼ばれる
@client.event
async def on_ready():
  print("起動した…")
  await client.change_presence(activity=discord.Game(name="jubeat Ave."))
  await tree.sync()


# メッセージを受信した時に呼ばれる
@client.event
async def on_message(message):
  # 自分のメッセージを無効
  if message.author == client.user:
    return

  # メッセージが"$hello"で始まっていたら"Hello!"と応答
  if message.content.startswith('$テスト'):
    await message.channel.send('Hello!')


@tree.command(name="test", description="テストコマンドです。")
async def test_command(interaction: discord.Interaction, テキスト: str):
  if テキスト == "モード":
    await interaction.response.send_message("どうしたの？", ephemeral=True)
  else:
    await interaction.response.send_message(テキスト, ephemeral=True)


  

# クライアントの実行
my_secret = os.environ['token']
client.run(my_secret)


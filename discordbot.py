# インストールした discord.py を読み込む
import discord
import random

# 自分のBotのアクセストークンに置き換えてください
TOKEN = ''

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました\n')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 部屋名がbotの部屋で/shuffleコマンドで実行
    if message.content.startswith('/shuffle') and message.channel.name == 'bot':
        commands = message.content.split()
        mylist = []
        print(message.guild.voice_channels)

        # 部屋にいる人数を数える
        for voice_channels in message.guild.voice_channels:
            # General部屋のみメンバーを数える場合は次を追加
            # if voice_channels.name == 'General':
            for member in voice_channels.members:
                print(member.name)
                mylist.append(member.name)
        print("count" + str(len(commands)) )
        # コマンドで人数を増やしたり部屋したり
        mode = '-null'
        for c in commands :
            if c == '-add':
                mode = '-add'
                continue
            if c == '-remove':
                mode = '-remove'
                continue
            if mode == '-add':
                mylist.append(c)
            if mode == '-remove':
                mylist.remove(c)

        print("count" + str(len(mylist)) )
        count = len(mylist)
        if count != 4 and (count < 6 or count > 8) :
            await message.channel.send('人数が4,6,7,8のときじゃないと部屋分けが難しいッピ /shuffle -add <なまえ> や /shuffle -remove <なまえ>で人数を調整できるッピ')
            return

        # 文章生成と送信
        random.shuffle(mylist)
        firstRoomCount = 2 if count == 4 else 4
        text = 'No.1 Court\n'
        for i in range(0,firstRoomCount):
            text += mylist[i] + "\n"
        text += '\nNo.2 Court\n'
        for i in range(firstRoomCount,len(mylist)):
            text += mylist[i] + "\n"
        print(text)
        await message.channel.send(text)
        return
            

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
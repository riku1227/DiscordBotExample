import discord

#注意 私(riku1227)はPython + Discord.py 初心者なので説明が間違えている可能性があります
#あとは私は文字列に""を使用する派です

client = discord.Client()

@client.event
async def on_ready():
#botの準備ができたとき(?)ログインできたとき(?)
    print("Logged in as")
    #Logged in asという文字を出力
    print(client.user.name)
    #Client(bot)のユーザー名を出力
    print(client.user.id)
    #Client(bot)のユーザーIDを出力
    print("------")
    #------という文字を出力

@client.event
async def on_message(message):
#メッセージが追加(?)送信(?)投稿(?)されたとき
    if message.author == client.user:
        #メッセージ送信主が自分(bot)だったら
        return
        #何もせずに終了する
    if message.content.startswith("!test"):
        #メッセージのスタート(最初)が!testだったら
        #message.contentでメッセージ内容を取得

        await client.send_message(message.channel, "Hello World")
        #Hello Worldというメッセージを投稿
        #send_message(messageを投稿するチャンネル,メッセージ内容)
        #message.channelでそのメッセージが送られたチャンネルを取得(?)

    elif message.content.startswith("!hello"):
        #メッセージのスタートが!helloだったら
        msg = "{0.author.mention} Hello".format(message)
        await client.send_message(message.channel, msg)
        #これと

        author_mention = message.author.mention
        msg2 = author_mention+" Hello"
        await client.send_message(message.channel, msg2)
        #これは同じ動きをする
        #投稿主に@を付けて @投稿主 Hello と投稿
        #message.author.mentionで投稿主のmention情報取得(?)
        #あとはmsg(2)にそれとHelloをくっつける

client.run("アプリ(bot)のtoken")
#おまじない()
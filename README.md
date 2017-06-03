# DiscordBotExample  
## これなに  
Discord用botのサンプルソースです。  
Pythonで書いています。  
実行にはDiscordライブラリが必要です。  
## Androidでの導入,実行方法  
### 1.環境構築  
Termuxというアプリをインストールしてください。  
[Termux](https://play.google.com/store/apps/details?id=com.termux)  
インストールしたらアプリを開き  
**`packages install python`**  
と入力してください  
*Do you want to continue? [Y/n]*  
と聞いてくるので **Y** と入力してください。  
これでPythonのインストールができました。  
次は  
**`python -m pip install -U https://github.com/Rapptz/discord.py/archive/master.zip`**  
と入力してください  
これでDiscordライブラリのインストールができました  
次は**curl**というのを入れます。  
これ自体はPythonに関係ないのですが、これを入れておくとAndroidのテキストエディタでbotを作りTermuxでそれを実行するということが非rootで簡単にできるようになります。 ~~めんどくさくないとは言ってない~~  
**`packages install curl`**  
と入力してください  
これも  
*Do you want to continue? [Y/n]*  
と聞いてくるので **Y** と入力してください。  
これでcurlのインストールができました  
### 2.botの登録  
[discordapp.com/developers/applications/me](https://discordapp.com/developers/applications/me)  
まずこちらのサイトにアクセスしてください(PC表示推奨)  
MyaAppsというところに **New App** と言うものがあるのでそれを押してください
すると  
![discord_dev_new_app](https://github.com/riku1227/DiscordBotExample/raw/images/discord_dev_new_app.png)  
このような画面が表示されます。  
`App Name にアプリ(bot)の名前`  
`App Descriptionにアプリ(bot)の説明`
`App Iconにアプリ(bot)のアイコン`  
を入れ  **Waiting for form completion** を押してください。すると
![descord_dev_app_setting](https://github.com/riku1227/DiscordBotExample/raw/images/descord_dev_app_setting.png)  
このような画面になります。  
そしたら **Create a Bot User** を押してください
***この時App Nameに設定されてりいる名前がbotの名前になります***  
***一度Bot Userを作ってしまうと名前の変更ができません。~~多分~~***  
***エラーが出る場合は名前を変更してやってみてください。***  
Bot Userの作成が成功すると  
![discord_dev_create_bot_user](https://github.com/riku1227/DiscordBotExample/raw/images/discord_dev_create_bot_user.png)  
このような画面になります。  
とりあえず **Public Bot**にチェック付けておいてください。  
**この画像では、別のところにチェックをつけていますが `Public Bot` にチェックを付けてください**
そしたら、  
`https://discordapp.com/oauth2/authorize?&client_id=CLIENT ID&scope=bot&permissions=0`  
*CLIENT ID* は *APP DETAILS* にある *Client ID* に変えてください。  
にアクセスしてください。  
そして、適当なサーバーにbotを追加してください。  
最後に *App Bot User* のところにあるTokenの右にあるやつを押してください。  
何か出るので、それをコピーして何処かにメモっておいてください。  

### 3.botの作成  
まずサンプルソースをダウンロードしましょう。  
[DiscordBotExample.zip](https://github.com/riku1227/DiscordBotExample/archive/master.zip)
それを解凍し、中には行っている *`command_reply.py`* というファイルをテキストエディタなどで開いてください。  
開いたら  
`client.run("アプリ(bot)のtoken")`  
のアプリ(bot)のtokenをさっきコピーした自分のbotのtokenを貼り付けてください。  
`client.run("123456789abcdefg")`  
こんな感じ(桁数はもっとあります)になればOkです。  
できたらそれを保存し、適当なクラウドストレージなどにuploadしてください。  
**誰にも見られないやつにアップロードしてください。**  
### 4.botの実行  
まずはTermuxでBot用のフォルダを作ります  
**`mkdir discord_bot`**  
フォルダの名前はなんでもOkです。  
そしたら  
**`cd discord_bot`**  
でdiscord_botの中に移動します。  
そしたらクラウドストレージに上げたbotのソースをダウンロードします。  
**`curl -O DLURL`**  
DLURLはアクセスしたらダウンロードが始まるURLにしてください。  
Mediafireの場合は  
`http://download698.mediafire.com/`  
このようなURLです。 
終わったら  
**`ls`**  
と打ってみましょう。  
先程DLしたファイル名が表示されます。  
そしたら  
**`python ./FILENAME`**  
FILENAMEは先程DLしたファイル名を入力してください。  
**`例 : python ./command_reply.py`**  
そうすると、botの名前 botのIDが出てきます。  
これでbotが実行できました。  
あとはDiscordでbotを追加したサーバーで  
**`!test`**  
と打ってください。 
すると **Hello World** というメッセージがbotから投稿されるはずです。  
他にも  
**`!hello`**
と打つと、botから ***二回*** @付きでHelloと投稿されます。  
これでbotを **作成 実行** ができました。  
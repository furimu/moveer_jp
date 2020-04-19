from discord import Embed
def send_normal_help():
    e = Embed(
        title = 'BOTを招待するリンク',
        url = 'https://discordapp.com/api/oauth2/authorize?client_id=694884958723899453&permissions=871456210&scope=bot'
    )

    e.add_field(
        name = 'help',
        value = 'これ',
        inline= False
    )

    e.add_field(
        name = 'move',
        value = '@mentionでメンバーを指定し移動させます',
        inline= False
    )

    e.add_field(
        name = 'cmove',
        value = '@mentionでメンバーを指定し特定のチャンネルに移動させます',
        inline= False
    )

    e.add_field(
        name = 'fmove',
        value = '指定されたボイスチャンネルにいるユーザーを別のチャンネルへ移動させます',
        inline= False
    )

    e.add_field(
        name = 'rmove',
        value = '指定された役職がついてるメンバーをコマンド送信者が居るボイスチャンネルへ移動させます',
        inline= False
    )

    e.add_field(
        name = 'tmove',
        value = '指定された役職がついてるメンバーを指定されたボイスチャンネルへ移動させます',
        inline= False
    )

    e.add_field(
        name = 'changema',
        value = '指定されたチャンネルでmoveeradminコマンドを使用できる様にします',
        inline= False
    )

    e.add_field(
        name = 'faq',
        value = 'よくある質問一覧です',
        inline= False
    )

    e.add_field(
        name = 'join',
        value = 'BOTを招待するリンクを発行します',
        inline= False
    )

    e.set_footer(
        text = '!help <command>でコマンドの詳細を確認してください。'
    )

    return e


def move_help():
    e = Embed(
        title = '!move users',
        description = '''
        1.「Moveer」という名前の音声チャネルを作成します
        2.音声チャネルに参加する（「Moveer」ではない）
        3.移動することをユーザーに伝え、チャンネル「Moveer」に参加する
        4 !move @user1 @user2...とコマンドを送信します
        '''
    )
    return e

def cmove_help():
    e = Embed(
        title = '!cmove voicechannel users',
        description = '''
        1. 'moveeradmin'という名前のテキストチャネルを作成します。
        2.友達に音声チャネルに参加するように伝えます。
        3.!cmove <voicechannel name or id> @ user1 @ user2とコマンドを送信します

        このコマンドでは、作成者が音声チャネル内にいる必要はありません。 これは管理者専用のコマンドなので、すべての！cmoveコマンドは「moveeradmin」「changema」で設定したチャンネルチャンネルで送信する必要があります。
        使用例：
        !cmove Channel1 @ Fragstealern＃2543
        !cmove 569909202437406750 @ Fragstealern＃2543
        （音声チャネルにスペースが含まれている場合は、
        !cmove "チャネル2" @ Fragstealern＃2543）
        '''
    )
    return e

def fmove_help():
    e = Embed(
        title = '!fmove before_channel after_channel',
        description = '''
        1.音声チャネルAに参加するために移動することをユーザーに通知
        2.!fmove before_channel after_channelとコマンドを送信します。after_channelは移動する音声チャネルです。

        このコマンドは、テキストチャネル「moveeradmin」「changema」で設定したチャンネルから送信する必要があります。
        （音声チャネルにスペースが含まれている場合は、
        !fmove "チャネル1" "チャネル2"）
        '''
    )
    return e

def rmove_help():
    e = Embed(
        title = '!rmove role<name or id or mention>',
        description = '''
        1.移動することをユーザーに伝え、音声チャネルに参加する
        2.他の音声チャネルに参加して、!rmove roleを書き込みます。ここで、roleは移動する役職の名前です

        このコマンドは、テキストチャネル「moveeradmin」「changema」で設定したチャンネルから送信する必要があります。
        役職にスペースが含まれている場合
        !rmove "super admins"
        '''
    )
    return e

def tmove_help():
    e = Embed(
        title = '!tmove channel role<name or id or mention>',
        description = '''
        1.音声チャネルに参加するために移動することをユーザーに伝えます
        2.!tmove channel roleとコマンドを送信します。roleは移動する役職の名前、channelは音声チャネル

        このコマンドは、テキストチャネル「moveeradmin」「changema」から送信する必要があります。
        役職にスペースが含まれている場合
        !tmove channel "super admins"
        '''
    )
    return e

def changema_help():
    e = Embed(
        title = '!changema Textchannel<name or id or mention>',
        description = '''
        1.!changema＃<channelName>とコマンドを送信します
        2. Moveerは、管理コマンドが＃<channelName>内で許可されていることを返信します
        '''
    )
    return e
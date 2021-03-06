from discord.ext import commands
from discord import Embed, Game, Activity, ActivityType, utils, TextChannel, VoiceChannel, CategoryChannel, Member, Role, Permissions 
import json
import send_help
import config
import asyncio

DEFAULT_MESSAGE = {}

def save(value, module):
    with open(f'config/jsons/{module}.json', 'w', encoding= 'utf-8') as f:
        return json.dump(value, f, ensure_ascii=False, indent=4)


def load(module):
    try:
        with open(f'config/jsons/{module}.json', encoding='utf-8') as f:
            return json.load(f)

    except OSError:
        
        save(DEFAULT_MESSAGE, module)

admin_channel = load('admin_channel')

bot = commands.Bot(command_prefix = '!', description = 'これはMoveerの日本語版です', help_command = None)


@bot.event
async def on_ready():
    print('起動完了')
    
    while True:
        await bot.change_presence(
            activity=Game(
                name='使い方は!help'
            )
        )
        await asyncio.sleep(10)
        guildcount = len(bot.guilds)
        membercount = 0
        for g in bot.guilds:
            membercount += len(g.members)
            await bot.change_presence(
                activity=Activity(
                    name= f'{guildcount}サーバー | {membercount}　ユーザー',
                    type=ActivityType.watching
                )
            )
        await asyncio.sleep(10)
        
    

@bot.event
async def on_guild_join(guild):
    mes = await guild.owner.send('このBOTは「本家」Moveerと使い方は同じです。しかし、コマンドを送信したら本家とこのBOTが反応してしまうため、本家様の方を手動で退出させてください。自動で本家様を退出させるのは権限の仕様上不可能となっています。')

@bot.command()
async def changema(ctx, channel: TextChannel = None):
    if channel is None:
        return await ctx.send('チャンネルが指定されていません')
    if ctx.channel.name != 'moveeradmin':
        return await ctx.send(f'これは管理コマンドです。"moveeradmin"というテキストチャンネルで最初に実行してください。{ctx.author.mention}')

    if not admin_channel.get(str(ctx.guild.id)):
        admin_channel[str(ctx.guild.id)] = {}
    
    admin_channel[str(ctx.guild.id)]['サーバーの名前'] = ctx.guild.name
    admin_channel[str(ctx.guild.id)]['テキストチャンネルの名前'] = channel.name
    admin_channel[str(ctx.guild.id)]['テキストチャンネルのID'] = str(channel.id)

    save(admin_channel, 'admin_channel')
    await ctx.send(f'{channel.mention}で管理コマンドを送信できるようにしました')


@bot.command()
async def move(ctx, users: commands.Greedy[Member] = None):
    if users is None:
        return await ctx.send('メンバーが指定されていません')

    vc = utils.get(ctx.guild.voice_channels, name='Moveer') 
    if vc is None:
        return await ctx.send('**Moveer**というボイスチャンネルが見つかりませんでした')

    elif ctx.channel.name != 'moveeradmin' and str(ctx.channel.id) != admin_channel[str(ctx.guild.id)]['テキストチャンネルのID']:
        return await ctx.send(f'これは管理コマンドです。"moveeradmin"というテキストチャンネルで最初に実行するか、！changema＃<変更先のチャンネル名> で設定してください。(最初はmoveeradminチャンネルで実行する必要があります){ctx.author.mention}')
   
    for member in users:
        if member.voice.channel is None:
            return await ctx.send(f'{member.name}はVCにいない為処理が停止しました')

        await member.move_to(vc)

    await ctx.send(f'{ctx.author.name}のリクエストにより{len(users)}人のユーザーを移動させました')
    


@bot.command()
async def cmove(ctx, channel: VoiceChannel, users: commands.Greedy[Member] = None):
    if users is None:
        return await ctx.send('メンバーが指定されていません')

    elif ctx.channel.name != 'moveeradmin' and str(ctx.channel.id) != admin_channel[str(ctx.guild.id)]['テキストチャンネルのID']:
        return await ctx.send(f'これは管理コマンドです。"moveeradmin"というテキストチャンネルで最初に実行するか、！changema＃<変更先のチャンネル名> で設定してください。(最初はmoveeradminチャンネルで実行する必要があります){ctx.author.mention}')

    for user in users:
        await user.move_to(channel)
    
    await ctx.send(f'{ctx.author.name}のリクエストにより{len(users)}人のユーザーを移動させました')


@bot.command()
async def fmove(ctx, channel: VoiceChannel, after_channel: VoiceChannel = None):
    if after_channel is None:
        return await ctx.send('チャンネルが指定されていません')

    elif ctx.channel.name != 'moveeradmin' and str(ctx.channel.id) != admin_channel[str(ctx.guild.id)]['テキストチャンネルのID']:
        return await ctx.send(f'これは管理コマンドです。"moveeradmin"というテキストチャンネルで最初に実行するか、！changema＃<変更先のチャンネル名> で設定してください。(最初はmoveeradminチャンネルで実行する必要があります){ctx.author.mention}')

    counter = 0
    for member in channel.members:
        
        counter = counter +1
        await member.move_to(after_channel)

    await ctx.send(f'{ctx.author.name}のリクエストにより{counter}人のユーザーを移動させました')


@bot.command()
async def rmove(ctx, role: Role):
    if ctx.author.voice.channel is None:
        return await ctx.send('貴方がボイスチャンネルに接続していない為このコマンドを実行できません')

    elif ctx.channel.name != 'moveeradmin' and str(ctx.channel.id) != admin_channel[str(ctx.guild.id)]['テキストチャンネルのID']:
        return await ctx.send(f'これは管理コマンドです。"moveeradmin"というテキストチャンネルで最初に実行するか、！changema＃<変更先のチャンネル名> で設定してください。(最初はmoveeradminチャンネルで実行する必要があります){ctx.author.mention}')
    counter = 0
    for member in ctx.guild.members:
        if role in member.roles:
            
            if member.voice is None:
                continue
            counter= counter + 1
            await member.move_to(ctx.author.voice.channel)
    await ctx.send(f'{ctx.author.name}のリクエストにより{counter}人のユーザーを移動させました') 

@bot.command()
async def tmove(ctx, channel: VoiceChannel, role: Role):
    if ctx.channel.name != 'moveeradmin' and str(ctx.channel.id) != admin_channel[str(ctx.guild.id)]['テキストチャンネルのID']:
        return await ctx.send(f'これは管理コマンドです。"moveeradmin"というテキストチャンネルで最初に実行するか、！changema＃<変更先のチャンネル名> で設定してください。(最初はmoveeradminチャンネルで実行する必要があります){ctx.author.mention}')


    counter = 0
    for member in ctx.guild.members:
        if role in member.roles:
            if member.voice is None:
                continue
            counter = counter + 1
            await member.move_to(channel)

    await ctx.send(f'{ctx.author.name}のリクエストにより{counter}人のユーザーを移動させました')

@bot.command()
async def help(ctx, option: str = None):
    if option is None:
        e = send_help.send_normal_help()

    elif option == 'move':
        e = send_help.move_help()

    elif option == 'cmove':
        e = send_help.cmove_help()

    elif option == 'fmove':
        e = send_help.fmove_help()

    elif option == 'rmove':
        e = send_help.rmove_help()

    elif option == 'tmove':
        e = send_help.tmove_help()

    elif option == 'changema':
        e = send_help.changema_help()

    await ctx.send(embed = e)


@bot.command()
async def faq(ctx):
    e = Embed(
        title = 'FAQ'
    )

    e.add_field(
        name = 'どうして実装されてないコマンドがあるのか。',
        value = 'helpを翻訳したところゲーム関係の機能だったので不要だと判断し、除去しました',
        inline= False
    )

    await ctx.send(embed = e)


@bot.command(aliases=['invite'])
async def join(ctx):
    """Joins a server."""
    perms = Permissions.none()
    
    perms.connect = True
    perms.move_members = True
    
    await ctx.send(f'<{utils.oauth_url(config.client_id, perms)}>')


bot.run(config.token)
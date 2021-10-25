import datetime
from discord import utils
from random import randint
import wikipediaapi as wpaapi
from discord.utils import get
import os
from translate import Translator

PREFIX = '.'
bad_words = ['фильтр','плохие слова']


client = commands.Bot( command_prefix = PREFIX )
client.remove_command( 'help' )

@client.event

async def on_ready():
	print('ля какой')
	await client.change_presence( status = discord.Status.online, activity = discord.Game( '.help' ) )
	

	my_channel = client.get_channel(774073933107429389)
	await my_channel.send('Бот WOW запущен')




#help
@client.event
async def on_command_error( member ):
	pass


@client.command()
async def help( ctx ):
	b=ctx.message.author
	emb = discord.Embed( title = 'Навигация по командам для пользователей', colour = discord.Color.teal() )
	emb.add_field( name = 'Информация', value = '\n.время\n.погода\n.wiki\n.text\n.join(.leave)\n.send_a\n.rand a b' )
	emb.add_field( name = 'Fun', value = '.think\n.Мото\n.cats' )
	emb.set_image( url = 'https://media.discordapp.net/attachments/775235971306094602/821591097222496256/ch_150146_s1AZ.png' )
	await ctx.send( embed = emb )
	print(b,'>help<')


@client.command()
async def text( ctx, *, args ):
	a=args
#	a1,a2=map(str,input().split())
	a1='rus'
	a2='eng'

	if a1 == 'eng':
		a1 ='English'
	if a2 == 'rus':
		a2 ='Russian'
	if a2 == 'eng':
		a2 ='English'
	if a1 == 'rus':
		a1 ='Russian'

	translator = Translator(from_lang=a1, to_lang=a2)
	result = translator.translate(a)
	await ctx.send( result )
	print(result)


@client.command()
async def wiki(ctx,message):
	emb = discord.Embed( title = message, colour = discord.Color.gold() )
	wiki=wpaapi.Wikipedia('ru')
	search=message
	x=wiki.page(search)
	a=x.summary[:]
	a = list(a) 
	del a[1999:]
	a=''.join(a) 
	c = a.rfind('.')
	a = list(a)
	del a[c:2000]
	a=''.join(a)
	emb.add_field( name = 'Информация из Википедии', value = a )
	if x.exists():

		try:
			await ctx.send( embed = emb )
			await ctx.send('Подробнее: : %s' % x.fullurl)
		except:
			await ctx.send( a )
			await ctx.send('Подробнее: : %s' % x.fullurl)
	else:
		await ctx.send('Страница не найдена')
	print('>wiki<')

#фан

@client.command()
async def think( ctx ):
	emb = discord.Embed( title = 'Думающий', colour = discord.Color.teal() )
	emb.set_image( url = 'https://media.discordapp.net/attachments/774073933107429389/815405106652381224/72gi.gif' )
	await ctx.send( embed = emb )
#	await ctx.send('https://media.discordapp.net/attachments/774073933107429389/815405106652381224/72gi.gif')

@client.command()
async def amogus( ctx ):
	emb = discord.Embed( title = 'Amogus', colour = discord.Color.light_gray() )
	emb.set_image( url = 'https://images-ext-1.discordapp.net/external/OjeM2EHeRz2gP96r3YntgHwggfm3h9rQmVFaHcuq00k/https/media.discordapp.net/attachments/464626846160650262/858807440756834314/image0.gif' )
	await ctx.send( embed = emb )

@client.command()
async def cats(ctx):
	emb = discord.Embed( title = 'Коты', colour = discord.Color.teal() )
	emb.set_image( url = 'https://media.discordapp.net/attachments/774073933107429389/813029224306442290/cat.jpg?width=1191&height=670' )
	await ctx.send( embed = emb )
#	await ctx.send("https://media.discordapp.net/attachments/774073933107429389/813029224306442290/cat.jpg?width=1191&height=670")

@client.command()
async def Мото(ctx):
	emb = discord.Embed( title = 'Мото-Мото', colour = discord.Color.teal() )
	emb.set_image( url = 'https://images-ext-2.discordapp.net/external/weZsQvMu6Rj87Nxln7AS1ZlUwCHlSW_gEqFkA7tVgTk/%3Fwidth%3D1191%26height%3D670/https/media.discordapp.net/attachments/774157603202662442/820672426962321428/image0.jpg' )
	await ctx.send( embed = emb )
#	await ctx.send("https://media.discordapp.net/attachments/774157603202662442/820672426962321428/image0.jpg?width=1191&height=670")	


#люди

@client.command()
async def Жора(ctx):
	emb = discord.Embed( title = 'Жра Осипов', colour = discord.Color.teal() )
	emb.set_image( url = 'https://media.discordapp.net/attachments/792709187640754177/820655892881473536/image0.jpg?width=375&height=669' )
	await ctx.send( embed = emb )
#	await ctx.send("https://media.discordapp.net/attachments/792709187640754177/820655892881473536/image0.jpg?width=375&height=669")

@client.command()
async def Лёха(ctx):
	emb = discord.Embed( title = 'Лёха', colour = discord.Color.teal() )
	emb.set_image( url = 'https://media.discordapp.net/attachments/775235971306094602/820666744074534952/2d5e3c8e5df5a46e.png' )
	await ctx.send( embed = emb )
#	await ctx.send("https://media.discordapp.net/attachments/775235971306094602/820666744074534952/2d5e3c8e5df5a46e.png")

@client.command()
async def Миша(ctx):
	emb = discord.Embed( title = 'Миша', colour = discord.Color.teal() )
	emb.set_image( url = 'https://media.discordapp.net/attachments/775235971306094602/820667257318539314/29f04ed6-9404-4840-bb50-bb344ab63561.png?width=852&height=671' )
	await ctx.send( embed = emb )
#	await ctx.send("https://media.discordapp.net/attachments/775235971306094602/820667257318539314/29f04ed6-9404-4840-bb50-bb344ab63561.png?width=852&height=671")

@client.command()
async def Макс(ctx):
	emb = discord.Embed( title = 'Макс', colour = discord.Color.teal() )
	emb.set_image( url = 'https://media.discordapp.net/attachments/775235971306094602/820666938183122984/pp_1.jpg' )
	await ctx.send( embed = emb )
#	await ctx.send("https://media.discordapp.net/attachments/775235971306094602/820666938183122984/pp_1.jpg")	

@client.command()
async def Женя(ctx):
	emb = discord.Embed( title = 'Женя', colour = discord.Color.teal() )
	emb.set_image( url = 'https://media.discordapp.net/attachments/775235971306094602/820672120827936778/e7a8bda86a385cd0.png?width=450&height=670' )
	await ctx.send( embed = emb )
#	await ctx.send("https://media.discordapp.net/attachments/775235971306094602/820672120827936778/e7a8bda86a385cd0.png?width=450&height=670")	

@client.command()
async def Егор(ctx):
	emb = discord.Embed( title = 'Егор', colour = discord.Color.teal() )
	emb.set_image( url = 'https://media.discordapp.net/attachments/774157603202662442/820673253206130688/-1.png?width=670&height=670' )
	await ctx.send( embed = emb )
#	await ctx.send("https://media.discordapp.net/attachments/774157603202662442/820673253206130688/-1.png?width=670&height=670")	

@client.command()
async def Альберь(ctx):
	emb = discord.Embed( title = 'Альберь', colour = discord.Color.teal() )
	emb.set_image( url = 'https://media.discordapp.net/attachments/775235971306094602/820671962127794186/b202eedc-d52b-44b7-bae8-8a25de6efa28.jpg?width=495&height=670' )
	await ctx.send( embed = emb )
#	await ctx.send("https://media.discordapp.net/attachments/775235971306094602/820671962127794186/b202eedc-d52b-44b7-bae8-8a25de6efa28.jpg?width=495&height=670")

@client.command()
async def Айтал( ctx ):
	emb = discord.Embed( title = 'Айтал', colour = discord.Color.teal() )
	emb.set_image( url = 'https://media.discordapp.net/attachments/792709187640754177/814126317510721596/1231321.png' )
	await ctx.send( embed = emb )
#	await ctx.send('https://media.discordapp.net/attachments/792709187640754177/814126317510721596/1231321.png')

@client.command()
async def Андрей( ctx ):
	emb = discord.Embed( title = 'Андрей', colour = discord.Color.teal() )
	emb.set_image( url = 'https://media.discordapp.net/attachments/792709187640754177/818659284522106920/unknown.png' )
	await ctx.send( embed = emb )
#	await ctx.send('https://media.discordapp.net/attachments/792709187640754177/818659284522106920/unknown.png')

@client.command()
async def Ваня( ctx ):
	emb = discord.Embed( title = 'Ваня', colour = discord.Color.teal() )
	emb.set_image( url = 'https://media.discordapp.net/attachments/774073933107429389/818659963337310268/cringe1.jpg' )
	await ctx.send( embed = emb )
#	await ctx.send('https://media.discordapp.net/attachments/774073933107429389/818659963337310268/cringe1.jpg')

@client.command()
async def Ваня2( ctx ):
	emb = discord.Embed( title = 'Ваня', colour = discord.Color.teal() )
	emb.set_image( url = 'https://media.discordapp.net/attachments/774073933107429389/818659957322285076/7f272cd038a3e9bb.png?width=824&height=670' )
	await ctx.send( embed = emb )
#	await ctx.send('https://media.discordapp.net/attachments/774073933107429389/818659957322285076/7f272cd038a3e9bb.png?width=824&height=670')

@client.command()
async def Эркин( ctx ):
	emb = discord.Embed( title = 'Эркин', colour = discord.Color.teal() )
	emb.set_image( url = 'https://media.discordapp.net/attachments/780709173632696350/789895163773452338/image2.png?width=376&height=669' )
	await ctx.send( embed = emb )
#	await ctx.send('https://media.discordapp.net/attachments/780709173632696350/789895163773452338/image2.png?width=376&height=669')

@client.command()
async def Лёня( ctx ):
	emb = discord.Embed( title = 'Саркома Картошка', colour = discord.Color.teal() )
	emb.set_image( url = 'https://scontent-arn2-1.cdninstagram.com/v/t51.2885-19/s320x320/243182338_240500674682141_3159728161771067275_n.jpg?_nc_ht=scontent-arn2-1.cdninstagram.com&_nc_ohc=KkKZszIABokAX-_CIUW&edm=ABfd0MgBAAAA&ccb=7-4&oh=9f2ebc7592cf56cbf68f9f87a1d77e52&oe=6161E134&_nc_sid=7bff83' )
	await ctx.send( embed = emb )




@client.command()
async def время( ctx ):
	rasp = discord.Embed( title = 'Расписание уроков', colour = discord.Color.magenta() )
	rasp.add_field( name = 'Расписание Звонков', value = '1.  8:15 - 9:00\n2.  9:05 - 9:50\n\n3.  10:00 - 10:45\n4.  10:55 - 11:40\n\n5.  11:50 - 12:35\n6.  12:45 - 13:30\n\n\n7.  14:35 - 15:15\n8.  15:20 - 16:15' )
	rasp.set_image( url = 'https://images-ext-1.discordapp.net/external/Gkn2ts3XGwcztdhCAMwwvclNdbuzGMy8yaGoksYcQ-4/https/img3.goodfon.ru/original/3872x2592/a/60/chasy-vremya-time-sirenevyy.jpg?width=1001&height=670')
	await ctx.send( embed = rasp )
	print('>время<')

@client.command()

async def time( ctx ):
	emb = discord.Embed( title = 'Время в Якутии', description = 'Вы сможете узнать текущее время', colour = discord.Color.purple(), url = 'https://time100.ru/Yakutsk')

	emb.set_author( name = client.user.name, icon_url = client.user.avatar_url )
	emb.set_footer( text = ctx.author.name, icon_url = ctx.author.avatar_url )
	emb.set_thumbnail( url = 'http://getdrawings.com/images/clock-line-drawing-9.gif' )

	now_date = datetime.datetime.now()

	emb.add_field( name = 'Time', value = format( now_date ))

	await ctx.send( embed = emb )
	print('>time<')

@client.command()
async def rand( ctx, arg1, arg2 ):
	arg1=int(arg1)
	arg2=int(arg2)
	await ctx.send(randint(arg1,arg2))

@client.command()
async def хотой( ctx ):
    author=ctx.message.author
    c=randint(0,10000)
    if c==10000:
        b=await ctx.send( 'https://images-ext-2.discordapp.net/external/kjFjltfKFxmdV3pXeK5SaAEVbWiQxHjn5eawwO0rojc/https/media.discordapp.net/attachments/894918922808229928/899996478913773608/coin-flip-18.gif' )
        await asyncio.sleep(6)
        rasp = discord.Embed( title = 'ВЫПАЛО РЕБРО', colour = discord.Color.gold() )
        rasp.add_field(name=':exclamation: :exclamation: ВНИМАНИЕ:exclamation: :exclamation: ',value ='Сообщение будет удалено через 5 минут')
        rasp.set_image( url = 'http://99-kopeek.ru/assets/images/nikolay_2/5r_1904_gu.jpg' )        
        await b.edit(embed=rasp,content='')
        await asyncio.sleep(300)        
        await b.delete()
        print(author,'>>Ребро<<')

    elif 0<=c<=4999:
        b=await ctx.send( 'https://images-ext-2.discordapp.net/external/kjFjltfKFxmdV3pXeK5SaAEVbWiQxHjn5eawwO0rojc/https/media.discordapp.net/attachments/894918922808229928/899996478913773608/coin-flip-18.gif' )
        await asyncio.sleep(3)
        rasp = discord.Embed( title = 'ВЫПАЛ ОРЁЛ', colour = discord.Color.gold() )
        rasp.set_image( url = 'https://media.discordapp.net/attachments/774157603202662442/894823886858911764/2.png?width=670&height=670' )
        await b.edit(embed=rasp,content='')
        print(author,'>>Орёл<<')

    else:
        b=await ctx.send( 'https://images-ext-2.discordapp.net/external/kjFjltfKFxmdV3pXeK5SaAEVbWiQxHjn5eawwO0rojc/https/media.discordapp.net/attachments/894918922808229928/899996478913773608/coin-flip-18.gif' )
        await asyncio.sleep(3)
        rasp = discord.Embed( title = 'ВЫПАЛА РЕШКА', colour = discord.Color.gold() )
        rasp.set_image( url = 'https://images-ext-2.discordapp.net/external/exNBf95t64_ifIm9-m2c6Fy5dPOvmzJOgKxGK0u-HLM/%3Fwidth%3D670%26height%3D670/https/media.discordapp.net/attachments/774157603202662442/894822924484231198/1.png' )
        await b.edit(embed=rasp,content='')
        print(author,'>>Решка<<')


		
#Расписание

@client.command()
async def пн( ctx ):
	rasp = discord.Embed( title = 'Расписание уроков', colour = discord.Color.green() )
	rasp.add_field( name = 'Понедельник', value = '1. История\n2. История\n\n3. Як. лит\n4. Як. лит\n\n5. Алгебра\n6. Алгебра\n\n\n7. Литература\n8. -' )
	rasp.set_thumbnail( url = 'https://media.discordapp.net/attachments/775235971306094602/820988578879504384/1024px-Weekday_heptagram.png?width=670&height=670' )
	rasp.set_image( url = 'https://media.discordapp.net/attachments/774073933107429389/819927692958892052/cartoon-vector-illustration-christmas-candy-cane-hand-drawn-font-actual-creative-holidays-sweet-alph.png?width=1280&height=670' )
	await ctx.send( embed = rasp )
	print('>расписание уроков пн<')

@client.command()
async def вт( ctx ):
	rasp = discord.Embed( title = 'Расписание уроков', colour = discord.Color.green() )
	rasp.add_field( name = 'Вторник', value = '1. -\n2. -\n\n3. Физика\n4. Физика\n\n5. Геометрия\n6. Геометрия\n\n\n7. Русский язык\n8. Русский язык \n 9.Программирование' )
	rasp.set_image( url = 'https://media.discordapp.net/attachments/774073933107429389/819928363200151572/tuesday-concept-retro-colorful-word-art-illustration-written-shapes-colors-203217108.png?width=1206&height=670' )
	rasp.set_thumbnail( url = 'https://media.discordapp.net/attachments/775235971306094602/820988578879504384/1024px-Weekday_heptagram.png?width=670&height=670' )
	await ctx.send( embed = rasp )
	print('>расписание уроков вт<')

@client.command()
async def ср( ctx ):
	rasp = discord.Embed( title = 'Расписание уроков', colour = discord.Color.green() )
	rasp.add_field( name = 'Среда', value = '1. Биология\n2. -\n\n3. Английский язык\n4. Английский язык\n\n5. Начертательная Геометрия\n6. -\n\n\n7. Физика\n8. Физика' )
	rasp.set_image( url = 'https://fontsme.com/wp-data/w/593/3593/slide/swednesday-0.png')
	rasp.set_thumbnail( url = 'https://media.discordapp.net/attachments/775235971306094602/820988578879504384/1024px-Weekday_heptagram.png?width=670&height=670' )
	await ctx.send( embed = rasp )
	print('>расписание уроков ср<')

@client.command()
async def чт( ctx ):
	rasp = discord.Embed( title = 'Расписание уроков', colour = discord.Color.green() )
	rasp.add_field( name = 'Четверг', value = '1. Английский язык\n2. Физкультура\n\n3. Информатика\n4. Информатика\n\n5. Физика\n6. Информатика\n\n\n7. История Якутии\n8. -' )
	rasp.set_image( url = 'https://st2.depositphotos.com/3523009/6509/i/950/depositphotos_65096635-stock-photo-thursday-word-calendar-translation-text.jpg' )
	rasp.set_thumbnail( url = 'https://media.discordapp.net/attachments/775235971306094602/820988578879504384/1024px-Weekday_heptagram.png?width=670&height=670' )
	await ctx.send( embed = rasp )
	print('>расписание уроков чт<')

@client.command()
async def пт( ctx ):
	rasp = discord.Embed( title = 'Расписание уроков', colour = discord.Color.green() )
	rasp.add_field( name = 'Пятница', value = '1. Физкультура\n2. Физкультура\n\n3. Алгебра\n4. Алгебра\n\n5. Матан\n6. Матан\n\n\n7. Литература \n8. Литература\n9. РНЗ' )
	rasp.set_image( url = 'https://media.discordapp.net/attachments/774073933107429389/819927290733264896/cartoon-vector-illustration-donut-word-friday-hand-drawn-drawing-sweet-bun-actual-creative-art-work-.png?width=1440&height=578' )
	rasp.set_thumbnail( url = 'https://media.discordapp.net/attachments/775235971306094602/820988578879504384/1024px-Weekday_heptagram.png?width=670&height=670' )
	await ctx.send( embed = rasp )
	print('>расписание уроков пт<')

@client.command()
async def сб( ctx ):
	rasp = discord.Embed( title = 'Расписание уроков', colour = discord.Color.green() )
	rasp.add_field( name = 'Суббота', value = '1. Экономика\n2. Астрономия\n\n3. ОБЖ\n4. -\n\n5. Информатика\n6. Химия\n\n\n\n' )
	rasp.set_image( url = 'https://media.discordapp.net/attachments/774073933107429389/888013490265133096/Super-Saturday.png?width=1130&height=670' )
	rasp.set_thumbnail( url = 'https://media.discordapp.net/attachments/775235971306094602/820988578879504384/1024px-Weekday_heptagram.png?width=670&height=670' )
	await ctx.send( embed = rasp )
	print('>расписание уроков сб<')
	
#help_adm

@client.command()
@commands.has_role(775524808502149171)

async def help_adm( ctx ):
	emb = discord.Embed( title = 'Навигация по командам для администраторов', colour = discord.Color.orange()  )

	emb.add_field( name = 'Информация', value = '.clear\n.kick\n.ban\n.hi\n.send_m' )
#	emb.add_field( name = 'Роли', value = '.war' )
#	emb.add_field( name = '{}clear'.format( PREFIX ), value = 'Очистка бота		' )
#	emb.add_field( name = '{}kick'.format( PREFIX ), value = 'Удаление участников сервера	' )
#	emb.add_field( name = '{}ban'.format( PREFIX ), value = 'Ограничение доступа к серверу	' )
#	emb.add_field( name = '{}mute'.format( PREFIX ), value = 'Ограничение в голосовом чате (даётся роль)' )

	await ctx.send( embed = emb )
	print('>help_adm<')

#Clear message
@client.command()
@commands.has_role(775524808502149171)
async def clear( ctx, amount : int ):
	b=ctx.message.author
	await ctx.channel.purge( limit = amount+1 )
	print(b,'>clear<')

#hi everybody
@client.command()

async def hi( ctx ):
	x=randint(1,10)
	emb = discord.Embed( title = 'Hi everybody! @here', colour = discord.Color.teal() )
	print(x)
	if x==1:
		emb.set_image( url = 'https://media.discordapp.net/attachments/775235971306094602/821598488155652106/trees-digital-art-grass-tiger-red-ligths-screenshot-computer-wallpaper-58617.png?width=1191&height=670' )
	if x==2:
		emb.set_image( url = 'https://media.discordapp.net/attachments/775235971306094602/821598804041662484/lisa_milyj_art_149937_1920x1200.png?width=1073&height=670' )
	if x==3:
		emb.set_image( url = 'https://media.discordapp.net/attachments/775235971306094602/821604428473303050/2000x1274_1141070_www.png?width=1051&height=670' )
	if x==4:
		emb.set_image( url = 'https://media.discordapp.net/attachments/775235971306094602/821605005512933437/3848f0957923ab6119717dcdbd0cb8fd4ec9871br1-1550-979v2_uhq.png?width=1060&height=670' )
	if x==5:
		emb.set_image( url = 'https://media.discordapp.net/attachments/775235971306094602/821609522933399612/D0BAD180D0B0D181D0B8D0B2D18BD0B5-D0BAD0B0D180D182D0B8D0BDD0BAD0B8-art-animal-art-D181D0BED0B1D0B0D0B.png?width=774&height=670' )
	if x==6:
		emb.set_image( url = 'https://media.discordapp.net/attachments/775235971306094602/821610259226427422/b5c0768efbcea4c901cd18d83268410b.png?width=536&height=670' )
	if x==7:
		emb.set_image( url = 'https://media.discordapp.net/attachments/775235971306094602/821610727806337064/Birds_Owls_Painting_Art_518464_2048x1152.png?width=1191&height=670' )
	if x==8:
		emb.set_image( url = 'https://media.discordapp.net/attachments/775235971306094602/821612558602862622/art-rajewel-olen-roga-svet.png?width=867&height=671' )
	if x==9:
		emb.set_image( url = 'https://media.discordapp.net/attachments/775235971306094602/821612705693171772/enot_art_monety_128476_2560x1600.png?width=1073&height=670' )
	if x==10:
		emb.set_image( url = 'https://media.discordapp.net/attachments/775235971306094602/821612911561670696/EL6XqkYWwAAYeSB.png?width=981&height=671' )

	await ctx.send( embed = emb )
#	await ctx.send('Hi everybody! @here ')
	print('>Hi everybody<')

#Kick

@client.command()
@commands.has_role(775524808502149171)

async def kick( ctx, member: discord.Member, *, reason = None ):
	b=ctx.message.author
	await ctx.channel.purge( limit = 1 )
	await member.kick( reason = reason)
	await ctx.send( f'kick user { member.mention }')
	print(b,'>Kick<')



#Ban

@client.command()
@commands.has_role(775524808502149171)

async def ban(ctx, member: discord.Member, *, reason = None):
	b=ctx.message.author
	await ctx.channel.purge( limit = 1)
	await member.ban( reason = reason )
	await ctx.send( f'ban user { member.mention }')
	print(b,'>Ban<')

@client.command()
@commands.has_role(775524808502149171)


async def send_m( ctx, member: discord.Member, message ):
	b=ctx.message.author
	await member.send( message )
	print(b,'>send_m<')

@client.command()
async def join(ctx):
	global voice
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guild = ctx.guild )

	if voice and voice.is_connected():
		await voice.move_to(channel)

	else:
		voice = await channel.connect()
		await ctx.send(f'Бот присоединился к каналу: {channel}')

@client.command()
async def leave(ctx):
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guild = ctx.guild )

	if voice and voice.is_connected():
		await voice.disconnect()

	else:
		voice = await channel.connect()
		await ctx.send(f'Бот отключился от каналу: {channel}')

@clear.error
async def clear_error( ctx, error ):
	if isinstance( error, commands.MissingRequiredArgument ):
		await ctx.send( f'{ ctx.author.mention }, обязательно укажите аргумент!')

	if isinstance( error, commands.MissingPermissions ):
		await ctx.send( f'{ ctx.author.mention }, у вас недостаточно прав!')
	print('>clear_error<')

@client.event
async def on_message( message ):
	await client.process_commands( message )

	msg = message.content.lower()

	if msg in bad_words:
		await message.delete()
	



token = os.environ.get('BOT_TOKEN')
client.run(token)



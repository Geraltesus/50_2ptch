import discord
from discord.ext import commands
import datetime
import pyowm
from random import randint
import wikipediaapi as wpaapi
from discord.utils import get
import os

PREFIX = '.'
bad_words = ['123','321']


client = commands.Bot( command_prefix = PREFIX )
client.remove_command( 'help' )

@client.event

async def on_ready():
	print('connected')

	await client.change_presence( status = discord.Status.online, activity = discord.Game( '.help' ) )


#help
@client.event
async def on_command_error( member ):
	pass

@client.command( pass_contex = True )
async def help( ctx ):
	emb = discord.Embed( title = 'Навигация по командам для пользователей', colour = discord.Color.teal() )
	emb.add_field( name = 'Информация', value = '.пн\n.вт\n.ср\n.чт\n.пт\n.сб\n.время\n.фото\n.time\n.погода\n.wiki' )
	emb.add_field( name = 'Fun', value = '.think\n.Мото\n.cats   \n.Егор\n.Лёха\n.Миша\n.Макс\n.Альберь\n.Айтал\n.Андрей\n.Ваня\n.Ваня2\n.Женя\n.Эркин' )
	emb.set_image( url = 'https://media.discordapp.net/attachments/775235971306094602/821591097222496256/ch_150146_s1AZ.png' )
	await ctx.send( embed = emb )
	print('>help<')



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
async def фото(ctx):
	emb = discord.Embed( title = 'Фото расписания', colour = discord.Color.teal() )
	emb.set_image( url = 'https://media.discordapp.net/attachments/775235971306094602/826090057446064128/931f4c3e-2e1f-4ed7-ac17-58f5cfc9d8a9.png?width=554&height=671' )
	await ctx.send( embed = emb )
#await ctx.send("https://media.discordapp.net/attachments/804100165115052042/820616237154828298/4a0fca7a-ddab-4a62-8bc2-284c718a9f22.png?width=566&height=670")

@client.command()
async def think( ctx ):
	emb = discord.Embed( title = 'Думающий', colour = discord.Color.teal() )
	emb.set_image( url = 'https://media.discordapp.net/attachments/774073933107429389/815405106652381224/72gi.gif' )
	await ctx.send( embed = emb )
#	await ctx.send('https://media.discordapp.net/attachments/774073933107429389/815405106652381224/72gi.gif')

@client.command()
async def cats(ctx):
	emb = discord.Embed( title = 'Коты', colour = discord.Color.teal() )
	emb.set_image( url = 'ttps://media.discordapp.net/attachments/774073933107429389/813029224306442290/cat.jpg?width=1191&height=670' )
	await ctx.send( embed = emb )
#	await ctx.send("https://media.discordapp.net/attachments/774073933107429389/813029224306442290/cat.jpg?width=1191&height=670")

@client.command()
async def Мото(ctx):
	emb = discord.Embed( title = 'Мото-Мото', colour = discord.Color.teal() )
	emb.set_image( url = 'https://media.discordapp.net/attachments/774157603202662442/820672426962321428/image0.jpg?width=1191&height=670' )
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





@client.command( pass_contex = True )
async def время( ctx ):
	rasp = discord.Embed( title = 'Расписание уроков', colour = discord.Color.magenta() )
	rasp.add_field( name = 'Расписание Звонков', value = '1.  8:15 - 8:55\n2.  9:05 - 9:45\n\n3.  10:05 - 10:45\n4.  10:55 - 11:40\n\n5.  11:50 - 12:35\n6.  12:45 - 13:30\n\n\n7.  14:35 - 15:20\n8.  15:30 - 16:15' )
	rasp.set_image( url = 'https://images-ext-1.discordapp.net/external/Gkn2ts3XGwcztdhCAMwwvclNdbuzGMy8yaGoksYcQ-4/https/img3.goodfon.ru/original/3872x2592/a/60/chasy-vremya-time-sirenevyy.jpg?width=1001&height=670')
	await ctx.send( embed = rasp )
	print('>время<')

@client.command( pass_contex = True )

async def time( ctx ):
	emb = discord.Embed( title = 'Время в Якутии', description = 'Вы сможете узнать текущее время', colour = discord.Color.purple(), url = 'https://time100.ru/Yakutsk')

	emb.set_author( name = client.user.name, icon_url = client.user.avatar_url )
	emb.set_footer( text = ctx.author.name, icon_url = ctx.author.avatar_url )
	emb.set_thumbnail( url = 'http://getdrawings.com/images/clock-line-drawing-9.gif' )

	now_date = datetime.datetime.now()

	emb.add_field( name = 'Time', value = format( now_date ))

	await ctx.send( embed = emb )
	print('>time<')

@client.command( pass_contex = True )

async def погода( ctx ):

	owm = pyowm.OWM('aad8fa85bfabe2907345fb0ec522c2e7')

	observation = owm.weather_at_place('Якутск')
	w = observation.get_weather()
	temperature = w.get_temperature('celsius')['temp']

	print( 'Температура в Якутске - ' , str(temperature))


	emb = discord.Embed( title = 'погода в Якутске', description = 'Вы сможете узнать прогноз погоды', colour = discord.Color.blue(), url = 'https://www.gismeteo.ru/weather-yakutsk-4039/')

	emb.set_author( name = client.user.name, icon_url = client.user.avatar_url )
	emb.set_footer( text = ctx.author.name, icon_url = ctx.author.avatar_url )
	emb.set_image( url = 'https://media.discordapp.net/attachments/775235971306094602/821595018665918484/1116.png?width=1014&height=669' )

	now_date = datetime.datetime.now()

	emb.add_field( name = 'Weather', value ='Температура на данный момент в Якутске '+ str(temperature))
	
	await ctx.send( embed = emb )
	print('>погода<')


#Расписание

@client.command( pass_contex = True )
async def пн( ctx ):
	rasp = discord.Embed( title = 'Расписание уроков', colour = discord.Color.dark_grey() )
	rasp.add_field( name = 'Понедельник', value = '1. География\n2. Русский язык\n\n3. Физика\n4. Физика\n\n5. Математика\n6. Математика\n\n\n7. Литература\n8. Литература' )
	rasp.set_thumbnail( url = 'https://media.discordapp.net/attachments/775235971306094602/820988578879504384/1024px-Weekday_heptagram.png?width=670&height=670' )
	rasp.set_image( url = 'https://media.discordapp.net/attachments/774073933107429389/819927692958892052/cartoon-vector-illustration-christmas-candy-cane-hand-drawn-font-actual-creative-holidays-sweet-alph.png?width=1280&height=670' )
	await ctx.send( embed = rasp )
	print('>расписание уроков пн<')

@client.command( pass_contex = True )
async def вт( ctx ):
	rasp = discord.Embed( title = 'Расписание уроков', colour = discord.Color.dark_grey() )
	rasp.add_field( name = 'Вторник', value = '1. -\n2. -\n\n3. Математика\n4. Математика\n\n5. История Якутии\n6. Физкультура\n\n\n7. Матан\n8. Матан' )
	rasp.set_image( url = 'https://media.discordapp.net/attachments/774073933107429389/819928363200151572/tuesday-concept-retro-colorful-word-art-illustration-written-shapes-colors-203217108.png?width=1206&height=670' )
	rasp.set_thumbnail( url = 'https://media.discordapp.net/attachments/775235971306094602/820988578879504384/1024px-Weekday_heptagram.png?width=670&height=670' )
	await ctx.send( embed = rasp )
	print('>расписание уроков вт<')

@client.command( pass_contex = True )
async def ср( ctx ):
	rasp = discord.Embed( title = 'Расписание уроков', colour = discord.Color.dark_grey() )
	rasp.add_field( name = 'Среда', value = '1. Физика\n2. Физика\n\n3. ОБЖ\n4. Биология\n\n5. Английский язык\n6. Английский язык\n\n\n 		КРУЖКИ' )
	rasp.set_image( url = 'https://fontsme.com/wp-data/w/593/3593/slide/swednesday-0.png')
	rasp.set_thumbnail( url = 'https://media.discordapp.net/attachments/775235971306094602/820988578879504384/1024px-Weekday_heptagram.png?width=670&height=670' )
	await ctx.send( embed = rasp )
	print('>расписание уроков ср<')

@client.command( pass_contex = True )
async def чт( ctx ):
	rasp = discord.Embed( title = 'Расписание уроков', colour = discord.Color.dark_grey() )
	rasp.add_field( name = 'Четверг', value = '1. Якутская Литература\n2. Якутская Литература\n\n3. Информатика\n4. Информатика\n\n5. Физка\n6. Информатика\n\n\n7. Матан\n8. Матан' )
	rasp.set_image( url = 'https://st2.depositphotos.com/3523009/6509/i/950/depositphotos_65096635-stock-photo-thursday-word-calendar-translation-text.jpg' )
	rasp.set_thumbnail( url = 'https://media.discordapp.net/attachments/775235971306094602/820988578879504384/1024px-Weekday_heptagram.png?width=670&height=670' )
	await ctx.send( embed = rasp )
	print('>расписание уроков чт<')

@client.command( pass_contex = True )
async def пт( ctx ):
	rasp = discord.Embed( title = 'Расписание уроков', colour = discord.Color.dark_grey() )
	rasp.add_field( name = 'Пятница', value = '1. Русский язык\n2. Английский язык\n\n3. Математика\n4. Математика\n\n5. Физкультура\n6. Физкультура\n\n\n7. Литература \n8. Экономика' )
	rasp.set_image( url = 'https://media.discordapp.net/attachments/774073933107429389/819927290733264896/cartoon-vector-illustration-donut-word-friday-hand-drawn-drawing-sweet-bun-actual-creative-art-work-.png?width=1440&height=578' )
	rasp.set_thumbnail( url = 'https://media.discordapp.net/attachments/775235971306094602/820988578879504384/1024px-Weekday_heptagram.png?width=670&height=670' )
	await ctx.send( embed = rasp )
	print('>расписание уроков пт<')

@client.command( pass_contex = True )
async def сб( ctx ):
	rasp = discord.Embed( title = 'Расписание уроков', colour = discord.Color.dark_grey() )
	rasp.add_field( name = 'Суббота', value = '1. -\n2. -\n\n3. История\n4. История\n\n5. Информатика\n6. Химия\n\n\n\n' )
	rasp.set_image( url = 'https://www.pngkey.com/png/full/868-8688573_saturday-name-logo-png-saturday-png.png' )
	rasp.set_thumbnail( url = 'https://media.discordapp.net/attachments/775235971306094602/820988578879504384/1024px-Weekday_heptagram.png?width=670&height=670' )
	await ctx.send( embed = rasp )
	print('>расписание уроков сб<')
	
#help_adm

@client.command( pass_contex = True )
@commands.has_permissions( administrator = True )

async def help_adm( ctx ):
	emb = discord.Embed( title = 'Навигация по командам для администраторов', colour = discord.Color.orange()  )

	emb.add_field( name = 'Информация', value = '.claer\n.kick\n.ban\n.mute\n.hi\n.send_a\n.send_m' )
	emb.add_field( name = 'Роли', value = '.war\n.ВОДОЛАЗ' )
#	emb.add_field( name = '{}clear'.format( PREFIX ), value = 'Очистка бота		' )
#	emb.add_field( name = '{}kick'.format( PREFIX ), value = 'Удаление участников сервера	' )
#	emb.add_field( name = '{}ban'.format( PREFIX ), value = 'Ограничение доступа к серверу	' )
#	emb.add_field( name = '{}mute'.format( PREFIX ), value = 'Ограничение в голосовом чате (даётся роль)' )

	await ctx.send( embed = emb )
	print('>help_adm<')

#Clear message
@client.command( pass_contex = True )
@commands.has_permissions( administrator = True )
async def clear( ctx, amount : int ):
	await ctx.channel.purge( limit = amount+1 )
	print('>clear<')

#hi everybody
@client.command( pass_contex = True )

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

@client.command( pass_contex = True )
@commands.has_permissions( administrator = True )

async def kick( ctx, member: discord.Member, *, reason = None ):
	await ctx.channel.purge( limit = 1 )

	await member.kick( reason = reason)
	await ctx.send( f'kick user { member.mention }')
	print('>Kick<')



#Ban

@client.command( pass_contex = True )
@commands.has_permissions( administrator = True )

async def ban(ctx, member: discord.Member, *, reason = None):
	await ctx.channel.purge( limit = 1)

	await member.ban( reason = reason )
	await ctx.send( f'ban user { member.mention }')
	print('>Ban<')

@client.command()
@commands.has_permissions( administrator = True )
async def war( ctx, member:discord.Member ):
	await ctx.channel.purge( limit = 1 )

	war3_role = discord.utils.get( ctx.message.guild.roles, name = 'war3' )

	await member.add_roles( war3_role )
	await ctx.send(f'{member.mention}, осваивает военное ремесло')
	print('war')

@client.command()
async def send_a( ctx ):
	await ctx.author.send( 'Hello' )
	print('>send_a<')

@client.command()
@commands.has_permissions( administrator = True )
async def send_m( ctx, member: discord.Member, message ):
	await member.send( message )
	print('>send_m<')

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
		await ctx.send( f'{ ctx.author.mention }, у вас не достаточно прав!')
	print('>clear_error<')

@client.event
async def on_message( message ):
	await client.process_commands( message )

	msg = message.content.lower()

	if msg in bad_words:
		await message.delete()
	



token = os.environ.get('BOT_TOKEN')
bot.run(token)


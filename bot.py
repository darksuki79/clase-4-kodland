import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='¿', intents=intents)

def gen_pass(x):
    elements = "+-/*!&$#?=@<>123456789ABDFIODMSIAMqiedmosoawidm"
    password = ""
    for i in range(x):
        password += random.choice(elements)
    return password

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy tu papa digo {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 20):
    await ctx.send("he" * count_heh)

@bot.command()
async def bye(ctx):
    await ctx.send('adioooo')

@bot.command()
async def psw(ctx, longitud=8):
    await ctx.send(f'ten una contraseña segura! para q no te roben tu cuenta cuando te metas a sitios raritos: {gen_pass(longitud)}')

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def creador(ctx):
    await ctx.send('Mi creador es darksuki_ 😎')

@bot.command()
async def bestfriend(ctx):
    await ctx.send('El mejor amigo de mi creador es perritiezo 🐶🔥')

@bot.command()
async def crush(ctx):
    await ctx.send('La persona de la que está enamorado mi creador es winter 💘')

@bot.command()
async def error(ctx):
    await ctx.send('Yo siempre te vigilo, aunque tú no me veas 👁️')

@bot.command()
async def gio(ctx):
    await ctx.send('= steven universe')

@bot.command()
async def randomfact(ctx):
    facts = [
        "Los creepers fueron un error de código 😱",
        "Los Enderman tienen miedo al agua, como los gremlins xd",
        "Dormir 8 horas es un mito, mejor juega Minecraft 😎",
        "Tu historial de búsqueda es más turbio que el Nether 👀"
    ]
    await ctx.send(random.choice(facts))

bot.run("")

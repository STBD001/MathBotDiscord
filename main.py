import discord
from discord.ext import commands

from Geometria import GeometriaCommand
from Algebra import AlgebraCommand
from Trygonometria import TrygonometriaCommand
from Logarytmy import LogarytmyCommand
from Kombinatoryka import KombinatorykaCommand
from Ciagi import CiagiCommnad

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"Zalogowany jako {bot.user}")


@bot.event
async def on_message(message):
    print(f"Otrzymano wiadomość: {message.content}")
    if message.author == bot.user:
        return
    await bot.process_commands(message)


@bot.command()
async def Geometria(ctx):
    await GeometriaCommand(ctx)

@bot.command()
async def Algebra(ctx):
    await AlgebraCommand(ctx)

@bot.command()
async def Trygonometria(ctx):
    await TrygonometriaCommand(ctx)

@bot.command()
async def Logarytmy(ctx):
    await LogarytmyCommand(ctx)

@bot.command()
async def Kombinatoryka(ctx):
    await KombinatorykaCommand(ctx)

@bot.command()
async def Ciągi(ctx):
    await CiagiCommnad(ctx)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("""
Oto komendy na które odpowiadam:
!Geometria - Wzory geometryczne
!Algebra - Wzory Algebraiczne
!Trygonometria - Wzory Trygonometryczne
!Logarytmy - Wzory Logarytmiczne
!Kombinatoryka - Wzory z kombinatoryki
!Ciągi - Wzory z zakresu ciągów
PS: Proszę je przepisać bo przy kopiowaniu się gubię
""")

bot.run('ID')
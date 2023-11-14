import discord
from discord.ext import commands
from bd import bd
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


class View(discord.ui.View):
    @discord.ui.button(label="Правда",style=discord.ButtonStyle.green, emoji="✅")
    async def button_true(self,inter: discord.Interaction,button):
        msg = inter.message.content
        for question in bd:
            if question["q"] == msg:
                msg = question
                break
        if msg["answer"]:
            await inter.message.channel.send("Вы ответили правильно!!")
        else:
            await inter.message.channel.send("Вы ответили неверно!!")
        await inter.message.delete()


    @discord.ui.button(label="Ложь", style=discord.ButtonStyle.red, emoji="❎")
    async def button_false(self, inter: discord.Interaction, button):
        msg = inter.message.content
        for question in bd:
            if question["q"] == msg:
                msg = question
                break
        if  not msg["answer"]:
            await inter.message.channel.send("Вы ответили правильно!!")
        else:
            await inter.message.channel.send("Вы ответили неверно!!")
        await inter.message.delete()




@bot.command("game")
async def game(ctx: discord.ext.commands.Context):
    question = random.choice(bd)["q"]
    view = View()
    await ctx.send(question,view=view)


bot.run("MTE3MTQ4OTcwMDkyNjczODU1Mw.GDGa_e.nt94GHtu2mj0h6D8ctTk6s_VG4VlxTZV1E18iI")

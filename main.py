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
        question = random.choice(bd)["q"]
        view = View()
        await inter.message.channel.send(question, view=view)

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
        question = random.choice(bd)["q"]
        view = View()
        await inter.message.channel.send(question, view=view)
        await inter.message.delete()

    @discord.ui.button(label="Стоп", style=discord.ButtonStyle.gray)
    async def button_stop(self, inter: discord.Interaction, button):
        await inter.message.channel.send("Игра остановлена,ждем вас еще!")
        await inter.message.delete()



@bot.command("game")
async def game(ctx: discord.ext.commands.Context):
    question = random.choice(bd)["q"]
    view = View()
    await ctx.send(question,view=view)


bot.run("ВАШ ТОКЕН ЗДЕСЬ")

import discord
import configparser

config = configparser.ConfigParser()
bot = discord.Bot(intents=discord.Intents.all())


class MyView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

        @discord.ui.button(label="Cacel", style=discord.ButtonStyle.grey)
        async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):
            await interaction.response.send_message("Interaction cancelled")

        @discord.ui.button(label="Work!", style=discord.ButtonStyle.green)
        async def work(self, interaction: discord.Interaction):
            await interaction.response.send_message("Work started!")

        async def interaction_check(self, interaction: discord.Interaction, /) -> bool:
            if interaction.author == 'user':
                return True

        async def on_timeout(self) -> None:
            return None


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


server = [1059472942804762665]


@bot.slash_command(guild_ids=server, name="Work", description="Checks to see if I am online!")
async def work(ctx):
    await ctx.respond(f"I am bot {bot.user}\n\nLatency: {bot.latency} ms")
    print(ctx)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == '!bot':
        await message.channel.send(f"Hello {message.author}")
        await message.reply(f"{message}")


bot.run(token)
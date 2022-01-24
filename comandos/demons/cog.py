from nextcord.ext import commands
import random

from main import objlista



class Demons(commands.Cog, name="Demonios"):
  """Recieves all Demon commands"""
  
  def __init__(self, bot: commands.Bot):
    self.bot = bot
  
  @commands.command()
  async def Demonio(ctx):
    """Sends a Random Demon"""
    await ctx.reply(random.choice(objlista.demons))

def setup(bot: commands.Bot):
  bot.add_cog(Demons(bot))
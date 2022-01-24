from nextcord.ext import commands
import random

from main import objlista



class MapRelated(commands.Cog,name="Map Related"):
  """Recieves all Map related commands"""
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.command()
  async def Clima(ctx):
      """Sends the Weather for the next rounds"""
      await ctx.reply(random.choice(objlista.clima))

  @commands.command()
  async def Mapa(ctx):
    """Sends the Map for the next game"""
    await ctx.reply(random.choice(objlista.mapa))

def setup(bot: commands.Bot):
  bot.add_cog(MapRelated(bot))
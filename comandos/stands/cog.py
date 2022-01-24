from nextcord.ext import commands
import random

from main import get_from_list
from main import objlista



class Stands(commands.Cog):
  """Recieves all Stand commands"""
  def __init__(self, bot: commands.Bot):
    self.bot = bot
  
  

  @commands.command()
  async def Stand(self,ctx: commands.Context,x: int = 1 ):
    """Sends X number of Stands (default is 1)"""
    values = list(get_from_list(objlista.stands,x))
    await ctx.reply(values)

  @commands.command()
  async def fiveStands(self,ctx: commands.Context):
     """Sends 5 random Stands"""
     await ctx.send(random.choice(objlista.stands))
     await ctx.send(random.choice(objlista.stands))
     await ctx.send(random.choice(objlista.stands))
     await ctx.send(random.choice(objlista.stands))
     await ctx.send(random.choice(objlista.stands))

def setup(bot: commands.Bot):
  bot.add_cog(Stands(bot))
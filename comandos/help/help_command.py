from typing import Optional
from nextcord.ext import commands
from nextcord import Embed

class MyHelpCommand(commands.MinimalHelpCommand):
    def get_command_signature(self, command):
        return '{0.clean_prefix}{1.qualified_name} {1.signature}'.format(self, command)
    
    async def _help_embed(self, title: str, description: Optional[str] = None, mapping: Optional[dir] = None):
      embed = Embed(title=title)
      if description:
        embed.description=description
      if mapping:
        # add a shor description of commands in each cog
        for cog, command_set in mapping.items():
          filtered = await self.filter_commands(command_set,sort = True)
          if not filtered:
            continue
          name=cog.qualified_name if cog else "No Category"
          cmd_list = "\u2002".join(
            f"{self.context.clean_prefix}{cmd.name}" for cmd in filtered
          )
          value = (
            f"{cog.description}\n{cmd_list}" 
            if cog and cog.description
            else cmd_list
          )
          embed.add_field(name=name, value=value)
      return embed

    async def send_bot_help(self, mapping: dict):
      embed = await self._help_embed(
        title="Bot Commands",
        description=self.context.bot.description,
        mapping=mapping
      )
      await self.get_destination().send(embed=embed)
    
    async def send_command_help(self, command: commands.Command):
      pass
    
    async def send_cog_help(self, cog: commands.Cog):
      pass
    
    send_group_help = send_command_help

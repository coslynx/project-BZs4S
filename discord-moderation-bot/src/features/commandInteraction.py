```python
# File: discord-moderation-bot/src/features/commandInteraction.py

class CommandInteraction:
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print(f'Logged in as {self.bot.user}')

    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content.startswith('!help'):
            await message.channel.send('List of available commands:\n!mute <@user> <reason>\n!kick <@user> <reason>\n!ban <@user> <reason>')

    async def on_command(self, message):
        if message.content.startswith('!mute'):
            await self.mute_user(message)
        elif message.content.startswith('!kick'):
            await self.kick_user(message)
        elif message.content.startswith('!ban'):
            await self.ban_user(message)

    async def mute_user(self, message):
        # Implementation for muting a user
        pass

    async def kick_user(self, message):
        # Implementation for kicking a user
        pass

    async def ban_user(self, message):
        # Implementation for banning a user
        pass
```
Ensure that the `CommandInteraction` class methods are properly implemented in the file to handle different commands like muting, kicking, and banning users based on the user's input. The class should interact with the Discord bot instance to execute these moderation actions effectively.
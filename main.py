import discord
from discord.ext import commands

# Bot setup with intents
intents = discord.Intents.default()
intents.messages = True  # Enable the messages intent
intents.guilds = True  # Enable the guilds intent
bot = commands.Bot(command_prefix='!', intents=intents)

# Remove the default help command
bot.remove_command('help')

# Note data structure
notes = []

# Command to create a note
@bot.command(name='createnote')
async def create_note(ctx, *, note_content):
    notes.append(note_content)
    await ctx.send(f'Note created: "{note_content}"')

# Command to list notes
@bot.command(name='listnotes')
async def list_notes(ctx):
    if notes:
        note_list = '\n'.join(f"{i+1}. {note}" for i, note in enumerate(notes))
        await ctx.send(f'**Your Notes:**\n{note_list}')
    else:
        await ctx.send('No notes available.')

# Command to delete a note
@bot.command(name='deletenote')
async def delete_note(ctx, note_index: int):
    if 1 <= note_index <= len(notes):
        deleted_note = notes.pop(note_index - 1)
        await ctx.send(f'Note {note_index} deleted: "{deleted_note}"')
    else:
        await ctx.send('Invalid note index.')

# Bot token
bot.run('YOUR-TOKEN-HERE')

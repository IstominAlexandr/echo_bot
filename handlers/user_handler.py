from aiogram.types import Message
from aiogram.filters Command, CommandStar
from lixicon.lexicon import LEXICON_RU

@dp.message(CommandStart())
async def proccess_start_command(message:Message):
    await message.answer(text = LEXICON_RU['/start'])

@dp.message(Command(commands='help'))
async def proccess_help_command(message:Message):
    await message.answer(text=LEXICON_RU['help'])

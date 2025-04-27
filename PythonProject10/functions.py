from aiogram import Bot
from aiogram.types import Message

ChannelName = "@zayavkalar_infosi"

async def get_user_info(message: Message, bot: Bot):
    user = await bot.get_chat(message.from_user.id)
    user_photos = await message.from_user.get_profile_photos()

    matn = (f"<a href='tg://user?id={message.from_user.id}'>USER</a> INFO:\n\n"
            f"Ism-Familya: {message.from_user.full_name}\n"
            f"ID:  {message.from_user.id}\n")
    if user.bio:
        matn +=  f"Tarjimai holi: {user.bio}\n"
    if message.from_user.username:
        matn = matn + f"Username: @{message.from_user.username}\n"
    if user_photos.photos:
        await message.answer_photo(user_photos.photos[0][-1].file_id, caption=matn, parse_mode="HTML")
        await bot.send_photo(ChannelName, user_photos.photos[0][-1].file_id, caption=matn, parse_mode="HTML")
    else:
        await message.answer(matn, parse_mode="HTML")



















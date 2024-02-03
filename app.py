import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import  CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from aiogram import F



import neural_style_transfer as nst
class ClientState(StatesGroup):
    START_ = State()
    SEND_STYLE_IMG = State()
    SEND_SOURCE_IMG  = State()
    PROCESS_IMAGE = State()
    RUN_GEN = State()


BOT_TOKEN = "6732463470:AAFTMbpMoS6ZJYnsz8EK2nTFbJkKfuW-wsA"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async  def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

@dp.message(CommandStart())
async def cmd_start(message: types.Message,  state: FSMContext):
    await  message.answer('Добро пожаловать. Это Бот  для переноса стиля изображения.\n Пожалуйста загрузите одно изображение со стилем')
    await state.set_state(ClientState.SEND_STYLE_IMG)

@dp.message(ClientState.SEND_STYLE_IMG)
async def handle_style_images(message: types.Message, state: FSMContext ):
    # Check if the message contains a photo

    if message.photo:
        # Get the file_id of the largest photo (highest resolution)
        file_id = message.photo[-1].file_id
        # Get the file object using the file_id
        file = await bot.get_file(file_id)
        print(file)
        # Download the file
        file_path = file.file_path
        print(file_path)
        downloaded_style_file = await bot.download_file(file_path)
        # Process the downloaded file as needed (e.g., save it, analyze it, etc.)
        # For example, you can save it to the local disk
        with open(f'C:\\Users\\Alexey\\pythonProject1\\data\\style-images\\{file_id}.jpg', 'wb') as new_file:
            new_file.write(downloaded_style_file.read())

        # Respond to the user
        await state.update_data(style_img_name=file_id)
        await message.reply("Изображение стиля загружено! Теперь, пожалуйста, загрузите одно изображение")
        await state.set_state(ClientState.SEND_SOURCE_IMG)
    else:
        # If the message doesn't contain a photo, respond accordingly
        await message.reply("Загрузите пожалуйста изображение.")

@dp.message(ClientState.SEND_SOURCE_IMG)
async def handle_style_images(message: types.Message,  state: FSMContext):
     if message.photo:
        file_id = message.photo[-1].file_id
        # Get the file object using the file_id

        file = await bot.get_file(file_id)
        print(file)
        # Download the file
        file_path = file.file_path
        print(file_path)
        downloaded_style_file = await bot.download_file(file_path)
        # Process the downloaded file as needed (e.g., save it, analyze it, etc.)
        # For example, you can save it to the local disk
        with open(f'C:\\Users\\Alexey\\pythonProject1\\data\\content-images\\{file_id}.jpg', 'wb') as new_file:
            new_file.write(downloaded_style_file.read())

        # Respond to the user
        await state.update_data(source_img_name=file_id)
        await message.reply("Изображение  загружено!")
        await state.set_state(ClientState.PROCESS_IMAGE)
        await message.answer(
            f"Нажмите кнопку Сгенерировать, что бы сгенерировать изображение. Генерация займет 20 секунд. ",
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text="сгенерировать"),
                        KeyboardButton(text="начать заново"),
                    ]
                ],
                resize_keyboard=True,
            ),
        )

     else:
         # If the message doesn't contain a photo, respond accordingly
         await message.reply("Пожалуйста загрузите именно фотографию.")

@dp.message(ClientState.PROCESS_IMAGE, F.text.casefold() == "начать заново")
async def cancel_handler(message: types.Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(
        "Наберите /start для запуска бота",
        reply_markup=ReplyKeyboardRemove(),
    )




@dp.message(ClientState.PROCESS_IMAGE, F.text.casefold() == "сгенерировать")
async def run_generation(message: types.Message, state: FSMContext) -> None:
    await state.set_state(ClientState.RUN_GEN)
    data = await state.get_data()
    print(data)
    await message.reply(
        "Запускаю генерацию",
        reply_markup=ReplyKeyboardRemove(),
    )
    #loop = asyncio.get_running_loop()
    #with ProcessPoolExecutor() as pool:
    #    await loop.run_in_executor(pool, nst.neural_style_transfer, optimization_config)
    optimization_config = nst.set_img_names(data['style_img_name'], data['source_img_name'] )
    print(optimization_config)
    nst.neural_style_transfer(optimization_config)
    out_img_path = f'C:\\Users\\Alexey\\pythonProject1\\data\\output-images\\' +  data['source_img_name'] +'_'+ data['style_img_name']  + '.jpg'
    print(out_img_path)
    await message.reply_photo( photo = types.FSInputFile(path= out_img_path))
    await message.answer("Сгенерировать еще /start")
'''
@dp.message(ClientState.PROCESS_IMAGE)
async def show_summary(message: types.Message, state: FSMContext) -> None:
    await message.answer(
        f"Nice to meet you, Did you like to write bots?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Запускаем Генерацию"),
                    KeyboardButton(text="Начать заново"),
                ]
            ],
            resize_keyboard=True,
        ),
    )
    
 '''





if __name__ == "__main__":
    asyncio.run(main())
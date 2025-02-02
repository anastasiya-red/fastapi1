from fastapi import FastAPI

# Создаем экземпляр приложения FastAPI (инициализируем приложение)
app = FastAPI()


# Определение базового маршрута
@app.get('/')
async def start():
    return 'Главная страница'


@app.get('/user/admin')
async def welcome_admin():
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def welcome_user(user_id):
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user')
async def welcome_user(username: str = 'An', age: int = 34):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'



# чтобы запустить сервер, в терминале нужно использовать команду "$ python -m uvicorn module_16_1:app", или "python -m uvicorn module_16_1:app"
# или "uvicorn module_16_1:app --reload"
# module_16_1 — это имя файла, где находится экземпляр приложения (app).
# app — это имя объекта FastAPI в файле.
# --reload — включает автоматическую перезагрузку сервера при внесении изменений в код.

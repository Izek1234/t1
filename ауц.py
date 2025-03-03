import logging
import aiohttp


MISTRAL_API_KEY = "zvU34dmqDwRG0Ei1104udW2CLsOqahP9"
async def get_mistral_response(user_message: str) -> str:
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistral-small-latest",
        "temperature": 0.7,
        "max_tokens": 2000,
        "messages": [{"role": "user", "content": user_message}]
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url, headers=headers, json=data) as response:
                if response.status == 200:
                    response_data = await response.json()
                    return response_data["choices"][0]["message"]["content"]
                else:
                    error = await response.text()
                    logging.error(f"Mistral API Error: {error}")
                    return "Ошибка при обработке запроса"
        except Exception as e:
            logging.error(f"Connection Error: {e}")
            return "Не удалось соединиться с сервером"


async def main():
    while True:
        user_input = input("Вы: ")
        response = await get_mistral_response(user_input)
        print(f"Бот: {response}")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
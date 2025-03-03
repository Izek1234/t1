import aiohttp

async def ask_mistral(question: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://api.mistral.ai/v1/chat/completions",
            headers={"Authorization": "Bearer zvU34dmqDwRG0Ei1104udW2CLsOqahP9"},
            json={
                "model": "mistral-large-latest",
                "messages": [{"role": "user", "content": question}]
            }
        ) as response:
            data = await response.json()
            return data["choices"][0]["message"]["content"]

async def main():
    while True:
        user_input = input("Вы: ")
        print(f"Бот: {await ask_mistral(user_input)}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

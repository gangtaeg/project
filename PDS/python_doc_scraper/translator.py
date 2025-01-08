from googletrans import Translator

async def translate_text(content):

    translator = Translator()
    result = await translator.translate(content)
    return result.text

async def main():
    content = "Hello, world!"
    translated = await translate_text(content)
    with open("output.txt", "w") as f:
        f.write(translated)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
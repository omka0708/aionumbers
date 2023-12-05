from aionumbers import get_matched_numbers
import asyncio


async def main():
    links_and_numbers = [("https://repetitors.info/", ["84955405676", "89991110033"]),
                         ("https://hands.ru/company/about/", ["81231231212", "84951370720"]),
                         ("https://www.kb123.ru/", ["84955932222", "84951112233", "84955931914", "84955944444"]),
                         ("https://www.mirea.ru/", ["84996008080"]), ]

    tasks = [get_matched_numbers(link, numbers) for link, numbers in links_and_numbers]
    print(await asyncio.gather(*tasks))


if __name__ == '__main__':
    results = asyncio.run(main())

import asyncio

from aionumbers import get_phone_numbers_from_url_aio, get_phone_numbers_from_urls_aio, get_phone_numbers_from_urls

res_1 = asyncio.run(get_phone_numbers_from_url_aio("https://hands.ru/company/about/", False))
print(res_1, sep='\n', end='\n' + '-' * 50 + '\n')

links = ["https://repetitors.info/",
         "https://www.kb123.ru/",
         "https://www.mirea.ru/", ]

res_2 = asyncio.run(get_phone_numbers_from_urls_aio(links, auto=True))
print(*res_2, sep='\n', end='\n' + '-' * 50 + '\n')

res_3 = get_phone_numbers_from_urls(links, auto=False)
print(*res_3, sep='\n', end='\n' + '-' * 50 + '\n')

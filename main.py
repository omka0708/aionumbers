from aionumbers import get_phone_numbers_from_urls

links = ["https://repetitors.info/",
         "https://hands.ru/company/about/",
         "https://www.kb123.ru/",
         "https://www.mirea.ru/", ]

numbers = get_phone_numbers_from_urls(links, auto=True)
print(*numbers, sep='\n')

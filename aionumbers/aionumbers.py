import asyncio
import aiohttp
import re

REGEX_LOOKBEHIND = r"(?<=[\W])"
REGEX_COUNTRY_CODE = r"(\+7|7|8)?"
REGEX_CITY_CODE = r"\(?[0-9]{3}\)?"
REGEX_PHONE_CODES = rf"({REGEX_COUNTRY_CODE}[\s\-]?{REGEX_CITY_CODE}[\s\-]?)?"
REGEX_MAIN_NUMBERS = r"[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}"
REGEX_LOOKAHEAD = r"(?=[\W])"
PATTERN = REGEX_LOOKBEHIND + REGEX_PHONE_CODES + REGEX_MAIN_NUMBERS + REGEX_LOOKAHEAD


async def get_html(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def get_phone_numbers_from_url_aio(url: str, auto: bool = False) -> dict[str, tuple]:
    html = await get_html(url)
    phone_numbers = set()
    for number in re.finditer(PATTERN, html):
        current_number = re.sub(r"[^0-9]", '', number.group())
        if len(current_number) == 11 and current_number[0] != '8':
            current_number = '8' + current_number[1:]
        if len(current_number) == 10:
            current_number = '8' + current_number
        if len(current_number) == 7:
            if auto:
                current_number = '8495' + current_number
            else:
                continue
        phone_numbers.add(current_number)
    return {url: tuple(phone_numbers)}


async def get_phone_numbers_from_urls_aio(urls: list[str], auto: bool = False):
    tasks = []
    for url in urls:
        tasks.append(get_phone_numbers_from_url_aio(url, auto))
    return await asyncio.gather(*tasks)


def get_phone_numbers_from_urls(urls: list[str], auto: bool = False):
    return asyncio.run(get_phone_numbers_from_urls_aio(urls, auto))


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

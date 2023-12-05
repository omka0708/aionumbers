import asyncio
import aiohttp
import re

PATTERN = r"(?<=[^0-9])((\+7|7|8)?[\s\-]?\(?[0-9]{3}\)?[\s\-]?)?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}(?=[^0-9])"


async def get_html(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def get_phone_numbers_from_url(url: str):
    html = await get_html(url)
    phone_numbers = []
    for number in re.finditer(PATTERN, html):
        current_number = re.sub(r"[^0-9]", '', number.group())
        if len(current_number) == 11 and current_number[0] != '8':
            current_number = '8' + current_number[1:]
        if len(current_number) == 10:
            current_number = '8' + current_number
        if len(current_number) == 7:
            current_number = '8495' + current_number
        phone_numbers.append(current_number)
    return phone_numbers


async def get_matched_numbers(url: str, input_numbers: list):
    url_numbers = await get_phone_numbers_from_url(url)
    matched_numbers = []
    for number in input_numbers:
        if number in url_numbers:
            matched_numbers.append(number)
    return matched_numbers

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

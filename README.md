# aionumbers
Phone number recognition module. Used stack: *asyncio*, *aiohttp*, *re* (regex). 
## What is this?
Python module for parsing russian phone numbers on websites.

Functions output strings in 8XXXYYYYYYY format.
## How to use?
Install aiohttp:

    pip install aiohttp
    
If your Python version < 3.4 also use:

    pip install asyncio

Functions expect link (or list of links) and parameter `auto`.

When `auto=True`, the function automatically fills city code with *495* (Moscow) if it is missing.
    
Look in `main.py` file how module `aionumbers` should be used.

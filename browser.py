from playwright.async_api import async_playwright
from config import CDP_URL

class BrowserSession:
    def __init__(self):
        self.playwright = None
        self.browser = None

    async def connect(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.connect_over_cdp(CDP_URL)
        return self.browser

    async def close(self):
        # Do not close the user's Edge browser; only stop this Playwright client.
        if self.playwright:
            await self.playwright.stop()

    def pages(self):
        return [
            page
            for context in self.browser.contexts
            for page in context.pages
        ] if self.browser else []

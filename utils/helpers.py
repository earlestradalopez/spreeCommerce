async def wait_for_and_click(page, selector):
    await page.wait_for_selector(selector)
    await page.click(selector)
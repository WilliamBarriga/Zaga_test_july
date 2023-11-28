from time import sleep
from playwright.sync_api import sync_playwright, Locator
from lxml import html


from models.scrapers import Opinion, Order
from commons.openai import Calification
from commons.env import Env

opinions_list = []
TaSession = None


def get_saved_opinions() -> list[Opinion, dict]:
    return opinions_list


def save_cookies(cookies: list[dict]) -> None:
    global TaSession
    for c in cookies:
        if c["name"] == "TASession":
            global TaSession
            TaSession = c["value"]
            break

def getta_session() -> str:
    return {"TASession": TaSession}

def scrape_opinions(order: Order) -> list[Opinion]:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto(Env.base_url)

        if order == Order.DESC:
            sleep(0.5)
            filter_button = '//*[@id="tab-data-qa-reviews-0"]/div/div[1]/div/div/div[2]/div/div/div[1]/div/button'
            page.locator(filter_button).click()

            sleep(0.5)
            one_star_button = "//html/body/div[4]/div/div[2]/div/div[2]/div/button[1]"
            page.locator(one_star_button).click()

            aplly_button = "//html/body/div[4]/div/div[3]/div/div[1]/button"
            page.locator(aplly_button).click()
            sleep(1)

        comments_block = '//*[@id="tab-data-qa-reviews-0"]/div/div[5]/div'
        comments = page.locator(comments_block).inner_html()

        tree = html.fromstring(str(comments))

        card_xpath = "//div[@data-automation='reviewCard']"

        cards = tree.xpath(card_xpath)

        comment_text = f"{card_xpath}/div[5]/div[1]/div/span/span"
        date_text = f"{card_xpath}/div[4]"
        name_text = f"{card_xpath}/div/div/div[2]/span/a"

        opinions_list = []

        for i in range(len(cards) - 1):
            try:
                comment = cards[i].xpath(comment_text)[i].text
                date_comment = cards[i].xpath(date_text)[i].text.split("•")[0]
                name_comment = cards[i].xpath(name_text)[i].text

                opinion = Opinion(
                    author=name_comment,
                    text=comment,
                    date=date_comment,
                )
                opinions_list.append(opinion)
            except:
                pass

        cookies = context.cookies()
        for c in cookies:
            if c["name"] == "TASession":
                global TaSession
                TaSession = c["value"]
                break

    return opinions_list


def save_opinions(opinions: list[Opinion]) -> list[Opinion]:
    opinions_list.extend(opinions)
    return get_saved_opinions()


def update_calification(id: int, calification: Calification) -> Opinion:
    if id >= len(opinions_list):
        raise ValueError("id is not valid")
    opinion = opinions_list[id]
    opinion.calification = calification
    return opinion

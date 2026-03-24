
from playwright.sync_api import sync_playwright

play = sync_playwright().start()
browser = play.chromium.launch(headless=False,args=["--start-maximized"])
page = browser.new_page(no_viewport=True)

page.goto("https://finance.naver.com/")
page.pause()

##################################################
#######         코드를 작성해주세요           #######
##################################################

page.get_by_role("link", name="해외증시").click()
page.locator("#americaIndex").get_by_role("link", name="다우 산업").click()
 
tag_table=page.locator("table",has_text="일별시세") 
tag_header=tag_table.locator("thead > tr > th").all_inner_texts()

tag_body = []
for tag_tr in tag_table.locator("tbody > tr").all():
    tag_td = tag_tr.locator("td").all_inner_texts()
    clean_row = [text.replace('\n', ' ').strip() for text in tag_td]
    row_dict = dict(zip(tag_header, clean_row))
    tag_body.append(row_dict)
    print(tag_td)
    
page.pause()

import json
dumped = json.dumps(tag_body, indent=2, ensure_ascii=False)

with open("finance.json", "w", encoding="utf-8") as fp:
    fp.write(dumped)

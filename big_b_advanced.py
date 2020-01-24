from bs4 import BeautifulSoup
from requests import get
import time

url = 'https://www.espncricinfo.com/scores/series/8044/season/2018/big-bash-league'

#  url links which you can scrape data. with this code we can scrape given year results for given LEAGUE
# "INDIAN PREMIER LEAGUE "https://www.espncricinfo.com/scores/series/8048/season/2019/indian-premier-league
# "BIG BASH" https://www.espncricinfo.com/scores/series/8044/season/2016/big-bash-league
# "BANGLADESH PREMIER LEAGUE " https://www.espncricinfo.com/scores/series/8653/season/2015/bangladesh-premier-league
# "CARIBBEAN PREMIER LEAGUE" https://www.espncricinfo.com/scores/series/18816/season/2018/caribbean-premier-league

r = get(url, headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
})
sum_url = []
page_soup = BeautifulSoup(r.content, 'html.parser')
con = page_soup.find('div', class_='scoreCollection__content cricket')
inner_con = con.findAll('ul', class_='cscore_list')
for det in con:
    summary_con = det.findAll('ul', class_='cscore_list')
    summary_drill = summary_con[0].findAll('li')
    match_day = det.find('div', class_='cscore_info-overview')
    team = det.findAll('span', class_='cscore_name cscore_name--long')
    score = det.findAll('div', class_='cscore_score')
    result = det.findAll('span', class_='cscore_notes_game')
    sum_url.append("https://www.espncricinfo.com" + summary_drill[0].a['href'])

for sum_man in sum_url:
    url_for_sum = sum_man
    r = get(url_for_sum, headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
    })
    page_soup = BeautifulSoup(r.content, 'html.parser')
    con_summary = page_soup.find('div', class_='gp__cricket__player-match__player__detail')
    main_container = page_soup.find('div', class_='gp__cricket__gameHeader')

    print("-------------------------------------------------------------")
    try:
        over_view = main_container.find('div', class_='cscore_info-overview')
        print("venue: " + over_view.text)
    except:
        print("venue: nothing i don't know")
    try:
        teams = main_container.findAll('div', class_='cscore_team icon-font-after')
        print("First Batting : " + teams[0].span.text)
        print("Second Batting : " + teams[1].span.text)
    except:
        print("First Battin : nothing")
        print("Second Batting : nothing")
    try:
        scores = main_container.findAll('div', class_='cscore_score')
        print("First Battin : " + scores[0].text)
        print("Second Batting : " + scores[1].text)
    except:
        print("First Batting : 000 ")
        print("Second Batting : 000 ")
    try:
        results = main_container.findAll('div', class_='cscore_notes')
        print("RESULT : " + results[0].text + "\n")
    except:
        print("RESULT : Nothing")
    try:
        raw1 = con_summary.a.text
        raw2 = con_summary.a.text
        team = con_summary.a.span.text
        player = raw1.replace(team, '')
        print("MAN OF THE MATCH : " + player)
        print("MAN OF THE MATCH TEAM : " + team)
    except:
        team = "no result match"
        player = "no result match"
        print("MAN OF THE MATCH : " + player)
        print("MAN OF THE MATCH TEAM : " + team)

    time.sleep(5)
    # break

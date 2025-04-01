import requests
from bs4 import BeautifulSoup

def get_news():
    url = "https://news.naver.com/section/105"  # IT/과학 섹션
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    articles = soup.select(".sa_text")
    # print(f"🧪 총 {len(articles)}개의 기사 찾음")  # 필요 없으면 주석 처리

    results = []
    seen_titles = set()

    for item in articles:
        # 최대 8개까지만
        if len(results) >= 12:
            break

        try:
            link_tag = item.select_one("a")
            if not link_tag:
                continue

            title = link_tag.get_text(strip=True)
            link = link_tag.get("href")

            # 상대 경로 처리를 위해
            if link and link.startswith("/"):
                link = "https://news.naver.com" + link

            # 중복 제거
            if title in seen_titles:
                continue
            seen_titles.add(title)

            # 필요한 데이터만 담기 (title, link)
            results.append({
                "title": title,
                "link": link
            })

        except Exception as e:
            print("❌ 뉴스 파싱 에러:", e)

    return results

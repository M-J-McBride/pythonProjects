from bs4 import BeautifulSoup
import requests

def get_soup() -> BeautifulSoup:
    headers: dict = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Vivaldi/7.0.3495.20'}
    request = requests.get('https://www.bbc.com/news', headers=headers)
    html: bytes = request.content

    soup = BeautifulSoup(html,'html.parser')
    return soup

def get_headlines(soup: BeautifulSoup) -> list[str]:
    headlines: set = set()
    for h in soup.findAll('h2',class_="sc-8ea7699c-3 dhclWg"):
        headline: str = h.contents[0].lower()
        headlines.add(headline)
    return sorted(headlines)


def get_terms(term: str,headlines: list[str]):
    term_matches = []
    term_count = 0
    for h in headlines:
        if term.lower() in h:
            print(f'{h}-------->{term}')
            term_matches.append(h)
            term_count += 1
        else:
            print(f'{h}')
    print('--------')
    print(f'There were {term_count} occurrences of {term}.')
    for h in term_matches:
        print(h)



def main():
    soup = get_soup()
    headlines = get_headlines(soup)

    get_terms('UK',headlines)

if __name__ == '__main__':
    main()
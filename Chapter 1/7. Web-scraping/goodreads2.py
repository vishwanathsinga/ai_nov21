import requests
import pandas as pd
from bs4 import BeautifulSoup
from random import randint
from time import sleep

# defining empty lists to store scraped values
titles = []
series_t = []
urls = []
author = []
rating = []
scores = []
no_of_votes = []

# specify number of pages to scrape. each page consists of 100 books.
x = 11
pages = [str(i) for i in range(1,x)]

for page in pages:
    base_url = f'https://www.goodreads.com/list/show/1.Best_Books_Ever?page={page}'
    r = requests.get(base_url)
    sleep(randint(2,6))  # adding delay to prevent server problems.
    print(page)
    print(r.status_code)  # status_code : 200 = success
    html = r.content
    soup = BeautifulSoup(html, 'lxml')
    tr = soup.find_all('tr')
    td = [t.find("td", {"width" : "100%"}) for t in tr]
    
    book_names = [t.find('a', class_ = 'bookTitle').text.strip() for t in td]
    for i in book_names:
        res = i.split('(')
        titles.append(res[0])
        if len(res)>1:
            series_t.append(res[1])
        else:
            series_t.append(None)
        
    book_url = [t.find('a', {'itemprop':'url'})['href'] for t in td]
    for i in book_url:
        urls.append(i)
        
    author_names = [t.find('a', class_ = 'authorName').text.strip() for t in td]
    for i in author_names:
        author.append(i)
        
    ratings = [t.find('span', class_ = 'minirating').text.strip() for t in td]
    for i in ratings:
        rating.append(i)
        
    score = [t.find('a', {'onclick':"Lightbox.showBoxByID('score_explanation', 300); return false;"}).text.strip() for t in td]
    for i in score:
        scores.append(i)
        
    no_of_people = [t.find('span', class_="smallText uitext").text.strip() for t in td]
    for i in no_of_people:
        no_of_votes.append(i)
        
# concat base url to book url to obtain the complete url

base_site = 'https://www.goodreads.com'
complete_urls = []

for i in urls:
    complete_urls.append(base_site + i)
    

# defining empty lists to store scraped values
no_of_pages = []
language = []
primary_genre = []
desc = []
no_of_awards = []
no_of_reviews = []


a = 0
for every_url in complete_urls:
    
    sleep(randint(1,3))
    print(a)
    a = a + 1
    response = requests.get(every_url)
    print(response.status_code)
    book_html = response.content
    book_soup = BeautifulSoup(book_html, features='lxml', from_encoding='utf-8')
    main_div = book_soup.find('div', class_ = 'mainContentFloat')
    
    book_no_of_pages = main_div.find('span', {'itemprop':"numberOfPages"})
    if book_no_of_pages:
        book_no_of_pages = int(book_no_of_pages.text.strip('pages'))
    else:
        book_no_of_pages = None
    no_of_pages.append(book_no_of_pages)

    book_language =  main_div.find('div', {'itemprop':"inLanguage"})
    if book_language:
        book_language = book_language.text.strip()
    else:
        book_language = None
    language.append(book_language)
    
    book_genre = main_div.find('a', class_='actionLinkLite bookPageGenreLink')
    if book_genre:
        book_genre = book_genre.text.strip()
    else:
        book_genre = None
    primary_genre.append(book_genre)
    
    book_desc = main_div.find('div', id="description")
    if book_desc:
        book_desc = book_desc.text.strip().splitlines()
        if len(book_desc) > 1:
            book_desc = book_desc[1]
        else:
            book_desc = book_desc
    else:
        book_desc = None
    desc.append(book_desc)
    
    book_ratings_and_reviews = main_div.find_all('a',href="#other_reviews")
    temp_str = []
    for i in book_ratings_and_reviews:
        temp_str.append(i.text.strip())
    book_no_of_reviews = int(temp_str[1].rstrip(' reviews').replace(',',''))
    no_of_reviews.append(book_no_of_reviews)
    
    awards = main_div.find('div', {'itemprop':"awards"})
    if awards:
        book_no_of_awards = len(awards.find_all('a'))
    else:
        book_no_of_awards = 0
    no_of_awards.append(book_no_of_awards)
    
    
books = pd.DataFrame()

books['titles'] = titles
books['series'] = series_t
books['author'] = author
books['avg_rating'] = rating
books['no_of_reviews'] = no_of_reviews
books['score'] = scores
books['no_of_votes'] = no_of_votes
books['pages'] = no_of_pages
books['language'] = language
books['genre'] = primary_genre
books['no_of_awards'] = no_of_awards
books['description'] = desc
books['urls'] = complete_urls

books.to_csv('good_reads.csv')


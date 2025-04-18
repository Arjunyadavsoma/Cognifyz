from bs4 import BeautifulSoup
import requests
import csv

response = requests.get('https://internshala.com/internships/')
html_content = response.text
soup = BeautifulSoup(html_content, 'lxml')
internship_cards = soup.find_all('div', class_='internship_meta duration_meta')


def scraping():
    with open('internships.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Job Title', 'Company Name', 'Stipend', 'Posted On', 'Location', 'Internship Link'])  # Header row

        for card in internship_cards:
            try:

                title = card.find('h3', class_='job-internship-name').text.strip()
                company = card.find('p', class_='company-name').text.strip().replace(' ', '')
                location = card.find('div', class_='row-1-item locations').text.strip().replace('(Hybrid)', '').strip()
                posted_date = card.find('div', class_='detail-row-2').span.text.strip()
                stipend = card.find('span', class_='stipend').text.strip()
                internship_link = 'https://internshala.com' + card.find('a', class_='job-title-href')['href']
                print(f'Job Title            :   {title}')
                print(f'Company Name         :   {company}')
                print(f'Stipend              :   {stipend}')
                print(f'Posted On            :   {posted_date}')
                print(f'Location             :   {location}')
                print(f'Internship Link      :   {internship_link}\n\n')
                writer.writerow([title, company, stipend, posted_date, location, internship_link])

            except AttributeError:
                continue
scraping()

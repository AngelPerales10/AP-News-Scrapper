from bs4 import BeautifulSoup
import requests

#Choose your news!
choice = input("What news do you want to see? \nTech, Trending, Politics, or World News? ").lower()

#links to all topics
all_urls = ["https://apnews.com/hub/technology", \
            "https://apnews.com/hub/trending-news",\
            "https://apnews.com/hub/politics", \
            "https://apnews.com/hub/world-news"]

#tech needed its own special heading class for some reason
all_headings = ["Component-heading-0-2-129 Component-headingMobile-0-2-130 -cardHeading", \
                "Component-heading-0-2-124 Component-headingMobile-0-2-125 -cardHeading", \
                ]

#class for summary
all_summaries = ["text-0-2-121", "content text-0-2-116"]

#link decision based on choice

#tech full run
if (choice == 'tech'):
    page = requests.get(all_urls[0]).text
    doc = BeautifulSoup(page, "html.parser")
    page_headings = doc.find_all(class_=all_headings[0])
    page_summaries = doc.find_all(class_=all_summaries[0])

    with open("your_news.txt", "w") as file:
        for header, details in zip(page_headings, page_summaries[:10]):
            news_info = f"\nTitle: {header.string}\nDetails: {details.string}.\n"
            file.write(news_info)
    quit()

# other topics

elif (choice == 'trending'):
    page = requests.get(all_urls[1]).text

elif (choice == 'politics'):
    page = requests.get(all_urls[2]).text

elif (choice == 'world news'):
    page = requests.get(all_urls[3]).text

# gathering page
doc = BeautifulSoup(page, "html.parser")
page_headings = doc.find_all(class_=all_headings[1])
page_summaries = doc.find_all(class_=all_summaries[1])

with open("your_news.txt", "w") as file:
        for header, details in zip(page_headings, page_summaries[:10]):
            news_info = f"\nTitle: {header.string}\nDetails: {details.string}.\n"
            file.write(news_info)

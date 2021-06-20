import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
# find all tags of <div class="question-summary">
questions = soup.select(".question-summary")
for question in questions:
    # inside all the <div class = "question-summary">
    # find the anchor tag with class = "questions-hyperlinks"
    question_text = question.select_one(".question-hyperlink").getText()
    votes = question.select_one(".vote-count-post").getText()
    print(question_text, votes)
print("---End Questions on Page 1")

"""
If you get an error of
    AttributeError: 'NoneType' object has no attribute 'getText'
the error means you spelled the class selector wrong
in .select() or .select_one()
soup cannot find any class with the wrong name.
Correct your spelling and try again.
"""

"""
Here are the URLs for page 2, 3, and 4. Notice a pattern?
https://stackoverflow.com/questions?tab=newest&page=2
https://stackoverflow.com/questions?tab=newest&page=3
https://stackoverflow.com/questions?tab=newest&page=4

We can build a loop to crawl through more pages.
"""
# start on page 2 since we already did page 1
for i in range(2, 5):
    url_suffix = f"?tab=news&page={i}"
    next_url = url + url_suffix
    print(next_url)
    response = requests.get(next_url)
    soup = BeautifulSoup(response.text, "html.parser")
    for question in questions:
        question_text = question.select_one(".question-hyperlink").getText()
        votes = question.select_one(".vote-count-post").getText()
        print(question_text, votes)
    print(f"---End Questions on page {i}---")

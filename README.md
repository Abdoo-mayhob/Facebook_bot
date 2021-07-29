

# Facebook_bot
link to the target post [currently offline] : https://www.facebook.com/Abdoo.Almayhob/posts/2520706771568711
## Table of contents
* [General info](#general-info)
* [Technologies](#Technologies)
* [How the code works](#How-the-code-works)

## General info
Self Aware Facebook post using Web Scraping and Automation with Python3 and Selenium.

### Why ?
Posts that scraps it's own reactions/views/upvotes are common on platforms like YouTube, Reddit, etc.
But not Facebook, why?
The reason I found was that because YouTube, reddit and other platforms provide an easy to use API where the code only have to make several requests and gets back all the needed data.
On Facebook however.. The API is super complicated. Spent many hours trying to understand how to interface with it and I gone nowhere. 
So I saw that a much easier, more unreliable way to automate stuff on facebook is to scrap info and mimic human interactions with the actual site on a software controlled chrome browser.

### Why not to?
It's not recommended to automate stuff on facebook this way at all. Facebook make frequent changes to it's code base and this code becomes useless. Not to mention that Facebook will notice the bot activity in a matter of hours (7 hours for my case) and will block certain futures on your account.

## Technologies
Project Used:
* Selenium
* ChromeWebDriver


## How the code works
The code will go to the post page, login with your account credentials. Scraps each reaction type, and count the comments. Then it clicks the "edit post" button, clears the old text and add the new text with the updated data, save and exit then repeats after a random amount of time (to help confuse facebook bot detection).
 

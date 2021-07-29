# ThisPostHas_fbBot.py
# -----------------------
# This Code scrap the reactions and comments form a facebook post, Then edit the same post with:
#   " This Post has x Reaction and z Comment ..etc"
#
# I used Selenium because the facebook api is very hard to understand.
# Info Needed for the bot to operat correctly: (All in Mobile version m.facebook)
#  - Profile Url
#  - Post Url 
#  - Reactions view Url (The page after you click on the reactions on the post)
#  - Login Credentials
#
# Important: Don't forget to install Chromdriver 
# -----------------------
# Created:      2021 - 01 - 29
# last Edited : 2021 - 02 - 05   16:03
# Made By : Abdoo_

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class ThisPostHas_bot:

    def __init__(self, chrom_driver_path, GUI=False):
        options = Options()

        options.add_argument('--no-sandbox')
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        #options.add_argument("--headless")
        options.add_argument('--disable-extensions')

        self.driver = webdriver.Chrome(
            chrom_driver_path, chrome_options=options)
        
        print("-----------------------")
        print("--- B O T  I S  O N ---")
        print()

    def set_target_details(self, username, password, profile_mobile_url, post_url, reactions_url):
        self.username = username
        self.password = password
        self.post_url = post_url
        self.reactions_url = reactions_url
        self.profile_url = profile_mobile_url
        self.refresh_counter = 0
        print("Target is Set ..")

    def enter_target_profile_and_login(self):
        # Goto Profile , *please login to continue appears*
        self.driver.get(self.profile_url)

        # Wait for the login button to appear (so we dont use sleep here)
        try:
            _ = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "login")))
        except:
            _ = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "_54k8 _56bs _4n43 _6gg6 _901w _56bu _52jh")))
        print("Loading Facebook ..")
        self._login()
        print("Logging in ..")
        print("-----------------------")

    def _login(self):
        username_box = self.driver.find_element_by_id('m_login_email')
        username_box.send_keys(self.username)
        print("Username Entered ..")

        password_box = self.driver.find_element_by_id('m_login_password')
        password_box.send_keys(self.password)
        print("Password Entered ..")

        login_box = self.driver.find_element_by_name("login")
        login_box.click()

    def _enter_edit_post(self):

        self.driver.get(self.post_url)

        # Click post settings (the top right 3 dots )
        ele = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[4]/div/div[1]/div/div/div/div[1]/header/div[2]/div/div/div[3]/div/a')
        ele.click()
        print("Post Dots Clicked")

        # Wait for the ele to appear (so we dont use sleep here)
        _ = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@data-sigil='touchable touchable editPostButton dialog-link enabled_action']")))

        # Hit Edit Post
        ele = self.driver.find_element_by_xpath(
            "//a[@data-sigil='touchable touchable editPostButton dialog-link enabled_action']")
        ele.click()
        print("Edit Post Clicked")

    def _replace_text(self):
        # Wait the textbox to appear
        _ = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//textarea[@id="uniqid_1"]')))

        # Clear old Text
        ele = self.driver.find_element_by_xpath('//textarea[@id="uniqid_1"]')
        act = ActionChains(self.driver).key_down(Keys.CONTROL, ele).send_keys(
            'a').key_up(Keys.CONTROL, ele).send_keys(Keys.DELETE)
        act.perform()
        act.perform()
        print("Cleaned Old Text")

        # Send New Text
        self.post_text = f"""
تعا لقلك ... ༼ つ ◕_◕ ༽つ
هاد البوست عليه 
{self.reactions["all"]} تفاعل

{self.reactions["love"]} منن أحببته
{self.reactions["like"]} لايك أزرق
{self.reactions["care"]} هادا الحاضن قلب
{self.reactions["angry"]} عصبني
{self.reactions["sad"]} أحزنني
{self.reactions["haha"]} هههه
{self.reactions["wow"]} واو
وكمان  {self.comments}  كومنت أكابري  (✿◠‿◠)
 أقرأ أول كم كومنت بلز    ; - )
(⌐■_■) 
هكرنا الفيس يشبب  : D
----------------
This Post has 
{self.reactions["all"]} Reaction

{self.reactions["love"]} Love
{self.reactions["like"]} Like
{self.reactions["care"]} Care
{self.reactions["angry"]} Angry
{self.reactions["sad"]} Sad
{self.reactions["haha"]} Haha
{self.reactions["wow"]} Wow
and 
{self.comments} Cute Comment <3

Hit a reaction, wait 30s, and reload the page ; - )
Don't tell me how did u do it, It's Magic  (o゜▽゜)o☆
-----------------------
FaceBook Post Scraper Bot
MadeBy Abdoo_
"""
        ele.send_keys(self.post_text)
        print("New Text Sent")

    def _save_post(self):
        ele = self.driver.find_element_by_xpath(
            '//button[@type="submit" and @value="Save"]')
        ele.click()
        print("Post Saved !")

    def _edit_post(self, target_post_url):
        self._enter_edit_post()
        self._replace_text()
        self._save_post()

    def _scrap_reactions(self):

        self.driver.get(self.reactions_url)

        # Wait for the ele to appear (so we dont use sleep here)
        _ = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[@data-sigil="reaction_profile_sigil"]/span')))

        reactions_box = self.driver.find_elements_by_xpath(
            '//span[@data-sigil="reaction_profile_sigil"]/span')
        self.reactions_data = []
        for span in reactions_box:
            self.reactions_data.append(span.get_attribute("aria-label"))

        self.reactions = dict()
        self.reactions["all"] = 0
        self.reactions["love"] = 0
        self.reactions["like"] = 0
        self.reactions["care"] = 0
        self.reactions["angry"] = 0
        self.reactions["sad"] = 0
        self.reactions["haha"] = 0
        self.reactions["wow"] = 0

        for i in self.reactions_data:
            if "this post" in i:
                self.reactions["all"] = int(i[:i.find('p')].strip())

            if "Love" in i:
                self.reactions["love"] = int(i[:i.find('p')].strip())

            if "Like" in i:
                self.reactions["like"] = int(i[:i.find('p')].strip())

            if "Care" in i:
                self.reactions["care"] = int(i[:i.find('p')].strip())

            if "Angry" in i:
                self.reactions["angry"] = int(i[:i.find('p')].strip())

            if "Sad" in i:
                self.reactions["sad"] = int(i[:i.find('p')].strip())

            if "Haha" in i:
                self.reactions["haha"] = int(i[:i.find('p')].strip())

            if "Wow" in i:
                self.reactions["wow"] = int(i[:i.find('p')].strip())

        # if "All" span is not there, "all" reactions is the total sum of reactions
        if self.reactions["all"] == 0:
            for k, v in self.reactions.items():
                if not k == "all":
                    self.reactions["all"] += v

        for k, v in self.reactions.items():
            print(k, "=", v)

    def _scrap_comments(self):
        self.driver.get(self.post_url)
        self.comments_ele = self.driver.find_elements_by_xpath(
            '//div[@data-sigil="comment"]')

        self.comments = len(self.comments_ele)
        print("comments = ", self.comments)

    def scrap_post(self):
        self._scrap_reactions()  # self.reactions is loaded (dict)
        self._scrap_comments()  # self.comments is loaded (int)

    def refresh(self):
        
        print()
        print("-----------------------")
        self.refresh_counter += 1
        print("Refreshing ..", self.refresh_counter)

        from random import randint as rand
        from random import random as rr
        sl_du = rand(4, 6) + (rr()*2.5)
        print("Sleeping for: ", sl_du)
        sleep(sl_du)

        # Scrap Post
        print("-----------------------")
        print("--- S C R A P I N G ---")
        bot.scrap_post()

        # Edit Post
        print("-----------------------")
        print("---- E D I T I N G ----")
        bot._edit_post(post_url)

    def kill_all(self):
        self.driver.quit()
        print("---- Dirver Killed ----")


if __name__ == "__main__":
    # Chrom Driver Path:
    ChromeDriver = "chromedriver.exe"

    # Needed Info:
    usr = "Your Facebook username"
    pwd = "Your Facebook Passwords"
    profile_url = "https://m.facebook.com/Abdoo.Almayhob"
    post_url = "https://m.facebook.com/story.php?story_fbid=2520706771568711&id=100008882382074"
    post_reactions_url = "https://m.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier=2520706771568711"

    # Init :
    bot = ThisPostHas_bot(ChromeDriver)
    bot.set_target_details(usr, pwd, profile_url, post_url, post_reactions_url)
    
    bot.enter_target_profile_and_login()

    # Forever Refresh:
    while True:
        try:
            bot.refresh()

        except KeyboardInterrupt:  # Ctrl + C
            print ("- KeyboardInterrupt -")
            break

        #except Exception as E:
        #    print("Error While Refreshing:\n", E)

    # End
    bot.kill_all()
    print("-----------------------")
    print("---- Code Finished ----")

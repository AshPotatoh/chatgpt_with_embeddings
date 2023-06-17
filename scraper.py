from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from subprocess import Popen, PIPE

#put the url you want to crawl here
url = ""
driver = webdriver.Chrome()
out_of_scope = []
visited_urls = []
initial_hrefs = []

#put any words you want to exclude from the URLs the crawler will use here
disallowed_words = []

# Crawls the site, then appends all the links to a list (to_visit_urls), then crawls those links, and so on.
# Then writes the output into a numbered text file.
def crawl(initial):
    to_visit_urls = initial
    visited_urls = []
    page = 0
    while True:
        print("started crawling")
        for link in to_visit_urls:
            
            
            if link in visited_urls:
                to_visit_urls.remove(link)
                continue
            
            elif any(word in link for word in disallowed_words):
                to_visit_urls.remove(link)
                print("login page blocked")
                visited_urls.append(link)
                continue
            else:
                to_visit_urls.remove(link)
                visited_urls.append(link)
                driver.get(link)
                time.sleep(3)
                driver.implicitly_wait(10)
                for a in driver.find_elements(By.TAG_NAME, 'a'):
                    #print(a.get_attribute('href'))
                    if a.get_attribute('href') == None:
                        continue
                    elif url not in a.get_attribute('href'):
                        out_of_scope.append(link)
                        continue
                    else:
                        if url in a.get_attribute('href') and any(word not in a.get_attribute('href') for word in disallowed_words):
                            if a.get_attribute('href') not in visited_urls and a.get_attribute('href') not in to_visit_urls:
                                #print("This url is in scope: " + a.get_attribute('href')+"\n")
                                to_visit_urls.append(a.get_attribute('href'))
                                
                                
                                    
                            else:
                                continue
                        else:
                            #print("This url is not in scope: " + a.get_attribute('href')+"\n")
                            out_of_scope.append(a.get_attribute('href'))
                            with open("out_of_scope.txt", "a") as f:
                                f.write(str(a.get_attribute('href')) + "\n")
                page_name = str(page)+".txt"            
                with open(str(page_name), "w", encoding='utf-8') as f:
                    #for when we want to grab all text and no convient ID is available
                    #refs = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'li', 'ul', 'ol']
                    print(link + "\n Writing....")
                    #This is the part you want to change if your site is different
                    main_body = driver.find_element(By.ID, 'main')
                    f.write(main_body.text)
                    
                page += 1

                Popen(["cls"], shell=True)
                time.sleep(0.3)
                print("Pages scraped: " + str(page))
                print("\nUrls processed: " + str(len(visited_urls))+ "\n")
                print("Urls to still visit: " + str(len(to_visit_urls))+ "\n")
                print("Last visited url: " + link + "\n")
        if len(to_visit_urls) == 0:
            break
        else:
            continue
                
                
def grab_hrefs():

    driver.get(url)
    
    for a in driver.find_elements(By.TAG_NAME, 'a'):
        print(a.get_attribute('href'))
        if a.get_attribute('href') == None:
            continue
        else:
            if url in a.get_attribute('href'):
                if a.get_attribute('href') not in initial_hrefs:
                    print("This url is in scope: " + a.get_attribute('href')+"\n")
                    initial_hrefs.append(a.get_attribute('href'))
                    
                else:
                    continue
            else:
                print("This url is not in scope: " + a.get_attribute('href')+"\n")
                out_of_scope.append(a.get_attribute('href'))
                with open("out_of_scope.txt", "a") as f:
                    f.write(str(a.get_attribute('href')) + "\n")

    return initial_hrefs    


def main():
    pull_href = grab_hrefs()
    print(pull_href)
    crawl(pull_href)

main()


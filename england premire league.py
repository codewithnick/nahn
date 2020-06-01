from xlwt import Workbook 
wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0,0, 'League') 
sheet1.write(0,1,'Date') 
sheet1.write(0,2,'HomeTeam') 
sheet1.write(0,3,'AwayTeam') 
sheet1.write(0,4,'HomeGoals')
sheet1.write(0,5,'AwayGoals')
sheet1.write(1,0,'england premire league')
row=1
col=6

from selenium import webdriver
import time
driver = webdriver.Chrome('chromedriver')
# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.oddsportal.com/soccer/england/premier-league/')
time.sleep(0.5)
results_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[6]/div[1]/div/div[1]/div[2]/div[1]/div[2]/ul/li[3]/span')
# .click() to mimic button click
results_button.click()
time.sleep(3)
date = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[6]/div[1]/div/div[1]/div[2]/div[1]/div[6]/table/tbody/tr[2]/th[1]/span')
print(date.text)

sheet1.write(1,1,date.text)
goals = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[6]/div[1]/div/div[1]/div[2]/div[1]/div[6]/table/tbody/tr[4]/td[3]')
print('goals=',goals.text)
if(goals.text!='postp.'):
    sheet1.write(1,4,goals.text.split(':')[0])
    sheet1.write(1,5,goals.text.split(':')[1])
else:
    sheet1.write(1,4,'postponed')
    sheet1.write(1,5,'postponed')
match_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[6]/div[1]/div/div[1]/div[2]/div[1]/div[6]/table/tbody/tr[4]')
                                           
print(match_button.text.split(' '))
home_team = match_button.text.split(' ')[1]
away_team = match_button.text.split(' ')[3]
sheet1.write(1,2,home_team)
sheet1.write(1,3,away_team)
#match_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[6]/div[1]/div/div[1]/div[2]/div[1]/div[6]/table/tbody/tr[4]/td[2]/a')
link = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[6]/div[1]/div/div[1]/div[2]/div[1]/div[6]/table/tbody/tr[4]/td[2]/a').get_attribute('href') 
print(link)
driver.get(link+'#ah;')
time.sleep(2)
i=1
while(True):
    
    try:    
        odds = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[6]/div[1]/div/div[1]/div[2]/div[1]/div[8]/div['+str(i)+']/div/strong/a')                                
        print(odds.text)
        odd = odds.text.split(' ')[2]
        i+=1
        sheet1.write(row,col,odd)
        sheet1.write(row-1,col,'ah')
        col+=1
        print(i)
    except:
        break
    
driver.get('https://www.oddsportal.com/soccer/england/premier-league/')
driver.get(link+'#over-under;2')
time.sleep(2)
i=1
while(True):
    
    try:    
        odds = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[6]/div[1]/div/div[1]/div[2]/div[1]/div[8]/div['+str(i)+']/div/strong/a')
                                            #/html/body/div[1]/div/div[2]/div[6]/div[1]/div/div[1]/div[2]/div[1]/div[8]/div[2]/div/strong/a
        print(odds.text)
        odd = odds.text.split(' ')[1]
        i+=1
        sheet1.write(row,col,odd)
        sheet1.write(row-1,col,'over-under')
        col+=1
        print(i)
    except:
        break
wb.save('databse.xls')

#over_under_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[6]/div[1]/div/div[1]/div[2]/div[1]/div[6]/table/tbody/tr[4]/td[2]/a'+'#over-under;')
# .click() to mimic button click
#over_under_button.click()

#time.sleep(1)
### locate email form by_class_name
##username = driver.find_element_by_xpath('/html/body/nav/section[2]/form/div[1]/div[1]/input')
### send_keys() to simulate key strokes
##username.send_keys('nikhilsingh892710@gmail.com')
### sleep for 0.5 seconds
###sleep(0.5)
### locate password form by_class_name
##password = driver.find_element_by_xpath('/html/body/nav/section[2]/form/div[1]/div[2]/input')
### send_keys() to simulate key strokes
##password.send_keys('joiniisc')
###sleep(0.5)
### locate submit button by_xpath
##driver.get('https:www.google.com')
###sleep(3)
##search_query = driver.find_element_by_name('q')
##search_query.send_keys('site:linkedin.com/in/ AND '+search_string+ ' AND ' +location)
###sleep(5)
##search_query.send_keys('\n')
###sleep(3)
##
##




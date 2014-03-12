import requests
import random
import BeautifulSoup

def dojo_creator():
    question_numbers = [i for i in range(50, 250)]
    input = 'Y' 

    while input.upper() == 'Y':
        rand_question = random.choice(question_numbers)
        response = requests.get('https://projecteuler.net/problem=' + str(rand_question), 
            auth=('username', 'password'))
        question_soup = BeautifulSoup.BeautifulSoup(response.text)
        print question_soup.find("h2").text
        print 
        print unicode(question_soup.find("div", {"class":"problem_content"}).text)
        print "="*150
        print "="*150
        input = raw_input('Another dojo? (y or n):')

if __name__ == '__main__':
    dojo_creator()

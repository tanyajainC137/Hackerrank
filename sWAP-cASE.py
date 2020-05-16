#https://www.hackerrank.com/challenges/swap-case/problem

#input is a string 'HackerRank.com presents "Pythonist 2".'

def swap_case(s):
    s= list(s)
    news=[]
    for letter in s:
            if letter.islower():
                newletter = letter.upper()
            elif letter.isupper():
                newletter = letter.lower()
            else: newletter = letter
            news.append(newletter)
         
    news = "".join(news) 
    return news
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)    

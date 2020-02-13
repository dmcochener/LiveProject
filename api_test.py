import requests
from bs4 import BeautifulSoup as bs

def scrape_test(url, searchTerm):
    source = requests.get(url)
    print(source.status_code)
    if source.status_code == 200:
        soup = bs(source.content, 'html.parser')
        nodes = soup.find_all(class_ = searchTerm)
        print(nodes[0])
        return nodes
    else:
        pass

def get_terms():
    url = input("Enter the url: \n")
    searchTerm = input("Enter the string of the class name : \n")
    return url,searchTerm

def get_element():
    element = input("Enter what element you want to get the text from (i.e. a, h4, etc) :\n")
    return element

def check_nodes(nodes,element):
    try:
        for node in nodes:
            item = node.find(element).get_text()
            print(item)
            return True

    except:
        print("This test failed.")
        return False


if __name__ == '__main__':
    url,searchTerms = get_terms()
    nodes = scrape_test(url,searchTerms)
    element = get_element()
    success = check_nodes(nodes,element)
    if success:
        print("Looks good, eh?")
    else:
        print("Time to find a new page")


import bs4
from lxml import etree

def openFile(nameFile = "test_listAccs.html"):
    soup = bs4.BeautifulSoup(open(nameFile, encoding='utf8').read(), "lxml")

    accHtml = soup.find_all(class_='card-panel list-item account-item')
    lstAcc = []
    for index_child, iblock in enumerate(accHtml):
        lstAcc.append({'name': iblock.find(class_='account-item--username text-overflow-ellipsis text-gray').text.replace('@',''),

                       'link': iblock.find(class_='account-item--username text-overflow-ellipsis text-gray')['href'],

                       'btn': iblock.find(class_='btn btn-block btn-choose waves-effect'),

                       'btn_cssSelector': f'div.m6:nth-child({index_child + 1}) > div:nth-child(1) > '
                                          f'div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > '
                                          f'form:nth-child(1) > button:nth-child(4)'})
    return lstAcc


def whileIl():
    followOrLike = "Подписаться"

    if 'Подписат' in followOrLike:
        followOrLike = "follow"
    elif followOrLike in 'лайк':
        followOrLike = "like"
    else:
        followOrLike = "notask"
    return followOrLike


print(openFile())

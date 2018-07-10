#! python3
# -*- encoding: utf-8 -*-

import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
# Download the page
    # urlのHTMLをダウンロード
    print('Downloading html %s ...' % url)
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    #outfile = open('reqget.log', 'w')
    #outfile.write(str(soup))
    #outfile.close()
    
    # Find the URL of the comic image.
    # DLしたHTMLからid="comic"なタグ内の<img>タグを取得
    comicElem = soup.select('#comic img')
    
    if comicElem == []:
        print('Could not find comic image.')
    else:
        try:
            # src属性の値(画像URLの一部)を取得し、URLを生成
            comicUrl = 'http:' + comicElem[0].get('src')
            # Download the image.
            print('Downloading img %s ...' % comicUrl)
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # skip this comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue

        # Save the image to ./xkcd.
        # DLした画像をファイル出力する
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    # <a>タグ rel属性=="prev"なタグ(1個目)を取得
    prevLink = soup.select('a[rel="prev"]')[0]
    # href属性(link urlの一部)を取得
    url = 'http://xkcd.com' + prevLink.get('href')

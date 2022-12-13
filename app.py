from src.webcrawler import Webcrawler
import urllib

url = "https://www.liputan6.com/"
condition = {
    'href' : {
        'tag' : 'img',
        'class' : "articles--iridescent-list--text-item__figure-image-lazyload",
        'target' : 'data-src'
    }
}

targetRoot = Webcrawler(url, condition).run()

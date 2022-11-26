from icrawler.builtin import BingImageCrawler
#情報を入力
select_word = "ねこ"
select_num = 100
#ダウンロード先のフォルダーを指定する
crawler = BingImageCrawler(storage={"root_dir": "assets/" + select_word})
#google検索＆ダウンロード
#検索キーワードとダウンロード数を決定する
crawler.crawl(keyword=select_word, max_num=int(select_num))
import requests
import json

root_path = "rss/"

blogs = requests.get(
    "https://eastasia.azure.data.mongodb-api.com/app/bangumibiweekly-hikvo/endpoint/dump_reco"
).json()
blogs = {blog["blog"]: blog for blog in reversed(blogs)}
feed = {
    "version": "https://jsonfeed.org/version/1.1",
    "title": "Bangumi 日志推荐",
    "home_page_url": "https://neutrinoliu.github.io/bgm_reviews/blog.html",
    "feed_url": "https://api-cab.pages.dev/rss/blog.json",
    "items": [
        {
            "id": blog["blog"],
            "url": f"https://bgm.tv/blog/{blog['blog']}",
            "title": blog["title"],
            "content_text": blog["reason"],
            "date_modified": blog["date"],
            "authors": [
                {
                    "name": blog["author"],
                    "url": f"https://bgm.tv/user/{blog['author']}",
                },
            ],
        }
        for blog in blogs.values()
    ],
}
with open(root_path + "blog.json", "w") as f:
    json.dump(feed, f, ensure_ascii=False, separators=(",", ":"))
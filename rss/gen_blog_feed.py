import requests
import json

root_path = "rss/"
max_num = 200

blogs = requests.get(
    "https://eastasia.azure.data.mongodb-api.com/app/bangumibiweekly-hikvo/endpoint/dump_reco"
).json()

de_dup = {}

for blog in reversed(blogs):
    de_dup[blog["blog"]] = blog
de_dup = sorted(de_dup.items(), key=lambda x: x[1]["date"], reverse=True)
blogs = dict(list(de_dup)[:max_num])
feed = {
    "version": "https://jsonfeed.org/version/1.1",
    "title": "Bangumi 日志推荐",
    "icon": "https://bgm.tv/img/ukagaka/shell_1_thumb.jpg",
    "favicon": "https://bgm.tv/img/smiles/tv/74.gif",
    "home_page_url": "https://neutrinoliu.github.io/bgm_reviews/blog.html",
    "feed_url": "https://api-cab.pages.dev/rss/blog.json",
    "items": [
        {
            "id": str(blog["blog"]),
            "url": f"https://bgm.tv/blog/{blog['blog']}",
            "title": blog["title"],
            "date_published": blog["date"],
            "content_text": "",
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

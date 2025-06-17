---
permalink: /
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

鹿児島大学理工学研究科　谷本敦のページです。
たまに更新します。


<div class="row">
<div class="col-md-12">
<h2 class="section-title">最新ニュース</h2>
<ul>
    {% assign sorted_news = site.news | sort: "date" | reverse %}
    {% for item in sorted_news limit:5 %}
    <li>
    {{item.date | date: "%Y年%m月%d日"}}
    {{item.content}}
    </li>
    {% endfor %}
</ul>
</div>
</div>
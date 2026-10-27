---
layout: default
title: ""
permalink: /
---
<section class="hero">
  <h1>{{ site.title }}</h1>
  <p class="lead">{{ site.description }}</p>
  <p class="lead">私たちは、銀河中心に潜む超巨大質量ブラックホールの物理を、大規模数値計算とX線天文衛星による観測の両面から研究しています。</p>
  <p><a class="button" href="{{ '/research/' | relative_url }}">研究内容を見る</a></p>
</section>

<section>
  <h2>{{ site.data.i18n.ja.news_latest }}</h2>
  {% include news-list.html limit=5 %}
  <p><a href="{{ '/news/' | relative_url }}">{{ site.data.i18n.ja.all_news }} &rarr;</a></p>
</section>

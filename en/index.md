---
layout: default
title: ""
permalink: /en/
---
<section class="hero">
  <h1>{{ site.title_en }}</h1>
  <p class="lead">{{ site.description_en }}</p>
  <p class="lead">We study the physics of supermassive black holes at the centers of galaxies, combining large-scale numerical simulations with observations by X-ray astronomy satellites.</p>
  <p><a class="button" href="{{ '/en/research/' | relative_url }}">Our Research</a></p>
</section>

<section>
  <h2>{{ site.data.i18n.en.news_latest }}</h2>
  {% include news-list.html limit=5 %}
  <p><a href="{{ '/en/news/' | relative_url }}">{{ site.data.i18n.en.all_news }} &rarr;</a></p>
</section>

# 研究室ウェブサイト(Jekyll / GitHub Pages)

## 1. 内容を編集する
| 編集したいもの | ファイル |
|---|---|
| 研究室名・大学名・メールなど | `_config.yml` |
| メンバー | `_data/members.yml` |
| 業績 | `_data/publications.yml` |
| ナビゲーション | `_data/nav.yml` |
| 各ページ本文(日本語) | `research.md`, `members.md`, `lectures.md`, `access.md` など |
| 各ページ本文(英語) | `en/*.md` |
| ニュース記事 | `_news/YYYY-MM-DD-slug.md`(`lang: ja` or `lang: en`) |
| 見た目 | `assets/css/style.css` |
| メンバー写真 | `assets/img/` に置き、`members.yml` の `photo` を書き換え |

## 2. ローカルで確認する
```sh
bundle install        # 初回のみ
bundle exec jekyll serve
# → http://localhost:4000/
```

## 3. GitHub Pages に公開する
リポジトリ `atsushitanimoto/atsushitanimoto.github.io` の `master` ブランチに push すると、
GitHub Actions(`.github/workflows/pages.yml`)が自動でビルドし、数分後に
https://atsushitanimoto.github.io/ に反映されます。

```sh
cd /Users/tanimoto/github/atsushitanimoto.github.io
git add -A
git commit -m "更新内容"
git push
```

Settings → Pages → Source は「GitHub Actions」にしておきます。

## 4. 業績を更新する
```sh
ADS_DEV_KEY=<SciX/ADS の API トークン> python3 scripts/ads_import.py
```
査読付き論文のみを取得し、主著・共著に分けて `_data/publications.yml` を生成します。

## 補足
- ローカルは Ruby 4.0 のため `github-pages` gem が使えません。代わりに Jekyll 4 系 + GitHub Actions で公開する構成にしています。
- 記事を追加するときは `_news/` に `2026-11-01-title.md` のようなファイルを作り、先頭に `title:` `date:` `lang:` を書きます。

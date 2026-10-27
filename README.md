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
1. GitHub で `atsushitanimoto.github.io` という名前の **公開** リポジトリを作成(atsushitanimoto は自分の GitHub ユーザー名)
2. `_config.yml` の `url` を `https://atsushitanimoto.github.io` に書き換える
3. 以下を実行:
   ```sh
   git add -A
   git commit -m "Initial lab website"
   git branch -M main
   git remote add origin https://github.com/atsushitanimoto/atsushitanimoto.github.io.git
   git push -u origin main
   ```
4. GitHub のリポジトリ → Settings → Pages → Source を「**GitHub Actions**」にする(`.github/workflows/pages.yml` が自動でビルド・公開します)
5. 数分後 `https://atsushitanimoto.github.io/` で公開されます(push するたびに自動更新)

## 補足
- ローカルは Ruby 4.0 のため `github-pages` gem が使えません。代わりに Jekyll 4 系 + GitHub Actions で公開する構成にしています。
- 記事を追加するときは `_news/` に `2026-11-01-title.md` のようなファイルを作り、先頭に `title:` `date:` `lang:` を書きます。

#!/usr/bin/env python3
"""NASA ADS から業績を取得して _data/publications.yml を生成する。

使い方:
  export ADS_DEV_KEY=xxxxxxxx   # https://ui.adsabs.harvard.edu/user/settings/token で取得
  python3 scripts/ads_import.py [--orcid 0000-0000-0000-0000] [--author "Tanimoto, Atsushi"]

既定では著者名 "Tanimoto, Atsushi" で検索します。ORCID を指定すると同姓同名を除外できます。
査読付き論文のみを取得し、主著(first)と共著(coauthor)に分類します。
"""
import argparse, json, os, sys, urllib.parse, urllib.request

API = "https://api.adsabs.harvard.edu/v1/search/query"
FIELDS = "bibcode,title,author,year,pub,volume,page,doi,identifier,property,doctype"
OUT = os.path.join(os.path.dirname(__file__), "..", "_data", "publications.yml")

def fetch(q, token):
    rows, start = [], 0
    while True:
        params = urllib.parse.urlencode({"q": q, "fl": FIELDS, "rows": 200, "start": start, "sort": "date desc"})
        req = urllib.request.Request(f"{API}?{params}", headers={"Authorization": f"Bearer {token}"})
        with urllib.request.urlopen(req) as r:
            data = json.load(r)["response"]
        rows += data["docs"]
        start += 200
        if start >= data["numFound"]:
            return rows

def fmt_author(name):
    """'Tanimoto, Atsushi' -> 'A. Tanimoto'"""
    if "," not in name:
        return name.replace("Xrism", "XRISM")
    last, first = [x.strip() for x in name.split(",", 1)]
    if "collaboration" in last.lower():
        return last.replace("Xrism", "XRISM")
    initials = " ".join(p[0] + "." for p in first.replace("-", " ").split() if p)
    return f"{initials} {last}".strip()

def yml(s):
    return json.dumps(str(s), ensure_ascii=False)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--author", default="Tanimoto, Atsushi")
    ap.add_argument("--orcid")
    ap.add_argument("--max-authors", type=int, default=5, help="この人数を超える場合 et al. で省略")
    a = ap.parse_args()
    token = os.environ.get("ADS_DEV_KEY")
    if not token:
        sys.exit("環境変数 ADS_DEV_KEY に ADS の API トークンを設定してください")
    q = f'orcid:{a.orcid}' if a.orcid else f'author:"{a.author}"'
    q += ' AND collection:astronomy AND doctype:article AND property:refereed'
    docs = fetch(q, token)
    # 出版済み論文と同じタイトルの arXiv 版(eprint)は重複なので除外
    norm = lambda t: "".join(ch for ch in t.lower() if ch.isalnum())
    published = {norm(d["title"][0]) for d in docs if d.get("doctype") != "eprint"}
    docs = [d for d in docs if not (d.get("doctype") == "eprint" and norm(d["title"][0]) in published)]
    lines = [f"# NASA ADS から自動生成 (query: {q})。手で編集しても構いませんが、再実行すると上書きされます。"]
    for d in docs:
        authors = d.get("author", [])
        first = authors[0] if authors else ""
        ty = "first" if first.split(",")[0].strip().lower() == a.author.split(",")[0].strip().lower() else "coauthor"
        authors = [fmt_author(x) for x in authors]
        if len(authors) > a.max_authors:
            authors = authors[:a.max_authors] + ["et al."]
        arxiv = next((i.split(":")[1] for i in d.get("identifier", []) if i.startswith("arXiv:")), None)
        lines += [f"- type: {ty}", f"  year: {d.get('year')}", f"  authors: {yml(', '.join(authors))}",
                  f"  title: {yml(d['title'][0])}", f"  journal: {yml(d.get('pub',''))}", f"  bibcode: {d['bibcode']}"]
        if d.get("volume"): lines.append(f"  volume: {yml(d['volume'])}")
        if d.get("page"): lines.append(f"  pages: {yml(d['page'][0])}")
        if d.get("doi"): lines.append(f"  doi: {yml(d['doi'][0])}")
        if arxiv: lines.append(f"  arxiv: {yml(arxiv)}")
    with open(OUT, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"{len(docs)} 件を {os.path.relpath(OUT)} に書き出しました")

if __name__ == "__main__":
    main()

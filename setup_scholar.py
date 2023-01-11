from pathlib import Path

import tomlkit
from pylatexenc.latex2text import LatexNodes2Text
from scholarly import scholarly

# Citation info
nico = scholarly.search_author_id('GBAFB2AAAAAJ', sortby='year')
print("Found")
scholarly.fill(nico, sections=["indices", "publications"], sortby='year')
citations = nico["citedby"]
h_index = nico["hindex"]
print(f"Citations: {citations}, h-index: {h_index}")

with open("config.toml", "r") as cf:
    config = tomlkit.load(cf)

config["params"]["footer"]["citation_count"] = citations
config["params"]["footer"]["h_index"] = h_index

with open("config.toml", "w") as cf:
    tomlkit.dump(config, cf)

print("Updated config.toml")


# publication list

def publication_markdown_template(
        title,
        authors=None,
        date=None,
        abstract=None,
        url=None,
        count=1
):
    content = f"""---
title: "{title}"
authors: "{authors}"
link: "{url}"
date: "{date}-01-{count:02d}"
private: {"false" if abstract else "true"}
---

"""
    if abstract:
        content += abstract

    return content


def urlify(s: str):
    return ''.join([c for c in s.replace(' ', '-').lower() if c.isalnum() or c == '-'])


excluded_terms = ["erratum"]

p: dict
year_counts = dict()
for p in nico["publications"][::-1]:
    print("--------------")
    scholarly.fill(p)
    try:
        bib: dict = p['bib']
        title = bib['title']
    except KeyError:
        print("Skipping incomplete publication")
        continue

    exclude = False
    for et in excluded_terms:
        if et in title.lower():
            print(f"Skipping: {title}")
            exclude = True
            break
    if exclude:
        continue

    print("Preparing publication")
    print(f"{title}")

    page_filename = urlify(title)

    page_path = f"content/research/publications/{page_filename}.md"
    if Path(page_path).exists():
        print("A page for this publication already exists, skipping")
        continue

    authors = bib.get("author", None)
    date = bib.get("pub_year", None)
    abstract = bib.get("abstract", None)
    url = p.get("pub_url", None)
    if url is None:
        try:
            url = p['author_pub_id']
            url = f"https://scholar.google.com/citations?view_op=view_citation&citation_for_view={url}"
        except KeyError:
            print("default url")

    if authors is None:
        print("default authors")
        authors = "Nicolas Deutschmann et al. (Google Scholar parsing failure)"
    else:
        authors = authors.lower()
        authors = authors.split(" and ")
        authors = ", ".join([a.strip().title() for a in authors])

    if abstract is not None:
        abstract = LatexNodes2Text().latex_to_text(abstract)

    print(f"creating {page_path}")

    if date in year_counts:
        year_counts[date] += 1
    else:
        year_counts[date] = 1

    page_content = publication_markdown_template(title, authors, date, abstract, url, year_counts[date])
    print("Page content:")
    print(page_content)
    print("")
    with open(page_path, "w") as pubfile:
        pubfile.write(page_content)

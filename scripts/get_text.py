import os
import tqdm
import requests
from bs4 import BeautifulSoup

# match links (parallel), scrape text, write


def filter_links(links):
    """Return only the links that may contain relevant legal texts (remove e.g. homepages)."""
    clean = []
    for l in links:
        if "sc_lang=" in l and len(l) > 50:
            clean.append(l)
    return clean


def get_cleaned_text(url):
    """Return text from url, without in-text HTML tags."""
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Remove in-text tags
    for strong in soup.findAll('strong'):
        strong.unwrap()
    for em in soup.findAll('em'):
        em.unwrap()

    return [z.get_text(strip=True) for z in soup.findAll('p')]


def main():

    # Retrieve links
    with open("links-kl-GL.txt", "r") as gl_file:
        gl_links = filter_links([l.rstrip() for l in gl_file.readlines()])
    with open("links-da.txt", "r") as da_file:
        da_links = filter_links([l.rstrip() for l in da_file.readlines()])

    # Match links  TODO: make prettier?
    matched_links = []
    for gl_link in gl_links:
        da_version = gl_link.replace("kl-GL", "da")
        if da_version in da_links:
            matched_links.append((gl_link, da_links[da_links.index(da_version)]))

    os.makedirs("raw_text/gl")
    os.makedirs("raw_text/da")
    for i, (gl, da) in enumerate(tqdm.tqdm(matched_links)):
        gl_text = get_cleaned_text(gl)
        da_text = get_cleaned_text(da)

        with open(f"raw_text/gl/{i}.gl", "w") as outfile:
            outfile.write("\n".join(gl_text))

        with open(f"raw_text/da/{i}.da", "w") as outfile:
            outfile.write("\n".join(da_text))


if __name__ == "__main__":
    main()

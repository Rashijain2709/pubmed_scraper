import requests

def fetch_papers(query: str, debug: bool = False) -> str:
    base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    search_url = f"{base}esearch.fcgi?db=pubmed&retmax=20&retmode=json&term={query}"
    if debug: print(f"[DEBUG] Search URL: {search_url}")

    ids = requests.get(search_url).json()["esearchresult"]["idlist"]
    id_string = ",".join(ids)

    fetch_url = f"{base}efetch.fcgi?db=pubmed&id={id_string}&retmode=xml"
    if debug: print(f"[DEBUG] Fetch URL: {fetch_url}")

    return requests.get(fetch_url).text

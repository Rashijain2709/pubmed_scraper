import requests
from typing import Optional

def fetch_papers(query: str, debug: bool = False) -> Optional[str]:
    """Fetches PubMed articles matching the query. Returns XML response or None on failure."""
    base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    search_url = f"{base}esearch.fcgi?db=pubmed&retmax=20&retmode=json&term={query}"

    try:
        if debug:
            print(f"[DEBUG] Search URL: {search_url}")

        search_response = requests.get(search_url, timeout=10)
        search_response.raise_for_status()

        ids = search_response.json().get("esearchresult", {}).get("idlist", [])
        if not ids:
            print("No articles found for the given query.")
            return None

        id_string = ",".join(ids)
        fetch_url = f"{base}efetch.fcgi?db=pubmed&id={id_string}&retmode=xml"

        if debug:
            print(f"[DEBUG] Fetch URL: {fetch_url}")

        fetch_response = requests.get(fetch_url, timeout=10)
        fetch_response.raise_for_status()

        return fetch_response.text

    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")
        return None
    except ValueError as e:
        print(f"Failed to decode JSON response: {e}")
        return None
    except KeyError as e:
        print(f"Unexpected response structure: missing key {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

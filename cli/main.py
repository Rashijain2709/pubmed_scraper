import argparse
from pubmed_scraper import fetch_papers, parse_pubmed_response, write_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers.")
    parser.add_argument("query", help="PubMed search query")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")
    parser.add_argument("-f", "--file", help="CSV output file")
    args = parser.parse_args()

    xml_data = fetch_papers(args.query, args.debug)
    results = parse_pubmed_response(xml_data, args.debug)

    if args.file:
        write_to_csv(results, args.file)
        print(f"[✔] Saved to {args.file}")
    else:
        for row in results:
            print(row)

if __name__ == "__main__":
    main()

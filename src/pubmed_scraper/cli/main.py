import argparse
import sys
from pubmed_scraper import fetch_papers, parse_pubmed_response, write_to_csv

def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch PubMed papers.")
    parser.add_argument("query", help="PubMed search query")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")
    parser.add_argument("-f", "--file", help="CSV output file")
    args = parser.parse_args()

    try:
        xml_data = fetch_papers(args.query, args.debug)
        if xml_data is None:
            print("Error: Failed to fetch papers. Please check your query or internet connection.")
            return 1

        results = parse_pubmed_response(xml_data, args.debug)
        if not results:
            print("Warning: No results found or data could not be parsed.")
            return 0

        if args.file:
            write_to_csv(results, args.file)
            print(f"Saved to {args.file}")
        else:
            for row in results:
                print(row)

        return 0

    except Exception as e:
        print(f"Unexpected error: {e}")
        if args.debug:
            import traceback
            traceback.print_exc()
        return 2

if __name__ == "__main__":
    sys.exit(main())

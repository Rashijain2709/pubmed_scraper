import xml.etree.ElementTree as ET
from typing import List, Dict

NON_ACADEMIC_KEYWORDS = ["pharma", "biotech", "inc", "ltd", "corp", "gmbh"]

def is_company(affiliation: str) -> bool:
    return any(k in affiliation.lower() for k in NON_ACADEMIC_KEYWORDS)

def parse_pubmed_response(xml_data: str, debug: bool = False) -> List[Dict]:
    root = ET.fromstring(xml_data)
    papers = []

    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle")
        pub_date = article.findtext(".//PubDate/Year") or "Unknown"
        authors = article.findall(".//Author")

        non_academic_authors = []
        companies = set()
        email = "Not available"

        for author in authors:
            name = " ".join(filter(None, [author.findtext("ForeName"), author.findtext("LastName")]))
            aff = author.findtext(".//AffiliationInfo/Affiliation") or ""

            if is_company(aff):
                non_academic_authors.append(name)
                companies.add(aff)
            if "@" in aff and email == "Not available":
                email = aff.split()[-1]

        if non_academic_authors:
            papers.append({
                "PubmedID": pmid,
                "Title": title,
                "Publication Date": pub_date,
                "Non-academicAuthor(s)": "; ".join(non_academic_authors),
                "CompanyAffiliation(s)": "; ".join(companies),
                "Corresponding Author Email": email
            })

    return papers

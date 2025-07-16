from pubmed_scraper.parser import parse_pubmed_response

def test_parser_with_sample():
    xml = """<PubmedArticleSet>
      <PubmedArticle>
        <MedlineCitation>
          <PMID>123456</PMID>
          <Article>
            <ArticleTitle>Sample Title</ArticleTitle>
            <AuthorList>
              <Author>
                <LastName>Rashi</LastName>
                <ForeName>Jain</ForeName>
                <AffiliationInfo>
                  <Affiliation>Pune, Maharashtra, India</Affiliation>
                </AffiliationInfo>
              </Author>
            </AuthorList>
            <Journal>
              <JournalIssue>
                <PubDate>
                  <Year>2025</Year>
                </PubDate>
              </JournalIssue>
            </Journal>
          </Article>
        </MedlineCitation>
      </PubmedArticle>
    </PubmedArticleSet>"""
    
    result = parse_pubmed_response(xml)
    assert len(result) == 1
    assert result[0]["Title"] == "Sample Title"
    assert "Pune, Maharashtra, India" in result[0]["CompanyAffiliation(s)"]

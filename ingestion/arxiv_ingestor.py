import arxiv

def get_arxiv_ai(max_items=5):
    search = arxiv.Search(
        query="cat: cs.AI OR cat:cs.LG",
        max_results=max_items,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    articles = []
    for result in search.results():
        articles.append({
            "title": result.title,
            "summary": result.summary,
            "link": result.entry_id
        })

    return articles

def get_arxiv_quant(max_items=5):
    search = arxiv.Search(
        query="cat:q-fin.*",
        max_results=max_items,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    articles = []
    for result in search.results():
        articles.append({
            "title": result.title,
            "summary": result.summary,
            "link": result.entry_id
        })

    return articles
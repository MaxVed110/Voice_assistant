from serpapi import GoogleSearch


def main():
    start = 0
    end = 40
    page_size = 10

    # basic search parameters
    parameter = {
        "q": "coca cola",
        "tbm": "nws",
        "api_key": "1a15ef08c83fb7bba62201558cd28c125d1eccab2a77a808e84ed7aa55f20d3f",
        # optional pagination parameter
        #  the pagination method can take argument directly
        "start": start,
        "end": end,
        "num": page_size
    }

    # as proof of concept
    # urls collects
    urls = []

    # initialize a search
    search = GoogleSearch(parameter)

    # create a python generator using parameter
    pages = search.pagination()
    # or set custom parameter
    pages = search.pagination(start, end, page_size)

    # fetch one search result per iteration
    # using a basic python for loop
    # which invokes python iterator under the hood.
    for page in pages:
        print(f"Current page: {page['serpapi_pagination']['current']}")
        for news_result in page["news_results"]:
            print(f"Title: {news_result['title']}\nLink: {news_result['link']}\n")
            urls.append(news_result['link'])

    # check if the total number pages is as expected
    # note: the exact number if variable depending on the search engine backend
    if len(urls) == (end - start):
        print("all search results count match!")
    if len(urls) == len(set(urls)):
        print("all search results are unique!")


if __name__ == '__main__':
    main()



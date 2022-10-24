from serpapi import GoogleSearch


def main():

    parameter = {
        "engine": "yandex",
        "text": "что такое бой",
        "api_key": "1a15ef08c83fb7bba62201558cd28c125d1eccab2a77a808e84ed7aa55f20d3f"
    }

    search = GoogleSearch(parameter)
    dict_results = search.get_dict()

    print(dict_results['organic_results'][0]['link'])
    print(dict_results['organic_results'][0]['snippet'])


if __name__ == '__main__':
    main()



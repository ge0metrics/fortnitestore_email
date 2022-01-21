import fortnite_api

def retrieve():
    api=fortnite_api.FortniteAPI()

    shop=api.shop.fetch(combined=True)

    all=shop.daily.entries
    for i in shop.featured.entries:
        all.append(i)

    return all
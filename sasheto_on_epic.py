from epicstore_api import EpicGamesStoreAPI
from datetime import datetime


def sasheto_epik():
    #Current free games from the store
    api = EpicGamesStoreAPI()
    sasheto_free = ""

    free_games = api.get_free_games()['data']['Catalog']['searchStore']['elements']
    for game in free_games:
        game_name = game['title']

        for image in game['keyImages']:
            if image['type'] == 'Thumbnail':
                game_thumbnail = image['url']
        game_price = game['price']['totalPrice']['fmtPrice']['originalPrice']
        try:
            game_promotions = game['promotions']['promotionalOffers']
            upcoming_promotions = game['promotions']['upcomingPromotionalOffers']
            if not game_promotions and upcoming_promotions:
                #soon
                promotion_data = upcoming_promotions[0]['promotionalOffers'][0]
                start_date_iso, end_date_iso = (
                    promotion_data['startDate'][:-1], promotion_data['endDate'][:-1]
                )
                # Remove the last "Z" character so Python's datetime can parse it.
                start_date = datetime.fromisoformat(start_date_iso)
                end_date = datetime.fromisoformat(end_date_iso)
                sasheto_free+=('{} ({}) will be free from {} to {} UTC.'.format(
                    game_name, game_price, start_date, end_date
                ))
                sasheto_free+="\n"
            else:
                sasheto_free+=('{} ({}) is FREE now.'.format(
                    game_name, game_price
                ))
                sasheto_free+="\n"
        except TypeError:
            pass
            # or
            #print('No discounts for this game')
            # your choice

    return sasheto_free
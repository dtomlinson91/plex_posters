import plex_posters

inst = plex_posters.movie_poster_porn_scraper.create_instance(
    client_id='yb7NnBPh4riSnw',
    client_secret='-3Z0XUXD2XCiksfX26jORG107fA',
    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:70.0)'
    'Gecko/20100101 Firefox/70.0',
)

print(inst.reddit_instance.read_only)

inst.get_hot_posters().get_posters()

print(plex_posters.__version__)

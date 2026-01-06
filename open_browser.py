import webbrowser
import random
import time

url = 'https://www.netflix.com/watch/{}'
path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"


def watch_random_episode():
    # season 5
    striking_vipers = 80186674
    smithereens = 80195724
    miley_cyrus = 80195725

    # season 4
    uss_callister = 80131567
    ark_angel = 80131566
    crocodile = 80131568
    hang_the_dj = 80131569
    metal_head = 80131570
    black_museum = 80131571

    # season 3
    nosedive = 80104627
    playtest = 80104630
    shut_up_and_dance = 80104626
    san_junipero = 80104625
    men_against_fire = 80104628
    hated_in_the_nation = 80104629

    # season 2
    be_right_back = 70279173
    white_christmas = 80073158
    white_bear = 70279174
    waldo_moment = 70279175

    # season 1
    national_anthem = 70264857
    fifteen_million_merits = 70264858
    history_of_you = 70264856

    black_mirror = {
        1: (national_anthem, fifteen_million_merits, history_of_you),
        2: (be_right_back, white_bear, white_christmas, waldo_moment),
        3: (nosedive, playtest, shut_up_and_dance, san_junipero, men_against_fire, hated_in_the_nation),
        4: (uss_callister, ark_angel, crocodile, hang_the_dj, metal_head, black_museum),
        5: (striking_vipers, smithereens, miley_cyrus),
    }
    seasons = random.randint(1, len(black_mirror))
    season = black_mirror[seasons]
    episode_number = random.randint(0, len(season) - 1)
    episode = season[episode_number]
    print("Random episode opening in 5 seconds!")
    for i in range(5, 0, -1):
        print(f"{i}!")
        time.sleep(1)
    print("Enjoy! :)")
    time.sleep(1)
    webbrowser.get(path).open(url.format(episode))


watch_random_episode()

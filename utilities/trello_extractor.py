#!/usr/bin/python3
import os
import configparser
from trello import TrelloClient

HOME_FOLDER = os.path.expanduser("~/")
config = configparser.ConfigParser()
config.read(HOME_FOLDER + "src/conf/loopzen.ini")

client = TrelloClient(
    api_key=config["TRELLO"]["API_KEY"],
    api_secret=config["TRELLO"]["API_SECRET"],
    token=config["TRELLO"]["TOKEN"]
)

GTD_BOARD_ID = "58f0778c1e3c1023fb416882"
GTD_LIST_INBOX_ID = "5ac04b4785a2351d00e263c5"


def extraer_info_card(card):
    info = "\n# {} \n".format(card.name)
    info += "* {} \n".format(card.description)
    print("TITLE: {}".format(card.name))
    print("CONTENT: {}".format(card.description))
    return info


def volcar_info(info):
    """
    Volcamos la informacion al fichero INBOX
    """
    file = open(HOME_FOLDER+"/doc/gtd/1_in.md", "a")
    file.write(info)
    file.close()


def main():
    gtd_inbox_list = client.get_list(GTD_LIST_INBOX_ID)
    for card in gtd_inbox_list.list_cards():
        info = extraer_info_card(card)
        volcar_info(info)
    gtd_inbox_list.archive_all_cards()


if __name__ == '__main__':
    main()

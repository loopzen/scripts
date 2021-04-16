#!/usr/bin/pytho3
import os
import configparser
from trello import TrelloClient

HOME_FOLDER = os.path.expanduser("~/")
config = configparser.ConfigParser()
config.read(HOME_FOLDER + "src/conf/loopzen.ini")


def get_info_all_cards(cards):
    info = ""
    for card in cards:
        info += get_info_card(card)
    return info


def get_info_card(card):
    info = "\n# {} \n".format(card.name)
    info += "* {} \n".format(card.description)
    info += getCheckListDetails(card)
    return info


def getCheckListDetails(card):
    checklist_info = ""
    for checklist in card.checklists:
        checklist_info = "* Checklist: {} \n".format(checklist.name)
        for item in checklist.items:
            checklist_info += "* {} \n".format(item['name'])
    return checklist_info


def print_to_file(info, file):
    file = open(file, "a")
    file.write(info)
    file.close()


def main():
    client = TrelloClient(
        api_key=config["TRELLO"]["API_KEY"],
        api_secret=config["TRELLO"]["API_SECRET"],
        token=config["TRELLO"]["TOKEN"]
    )

    try:
        inbox_list = client.get_list(config["TRELLO"]["GTD_LIST_INBOX_ID"])
        inbox_cards = inbox_list.list_cards()
        information = get_info_all_cards(inbox_cards)
        print_to_file(information, config['TRELLO']['OUTPUT_FILE'])
    except FileNotFoundError:
        print('Inbox file not found')
    else:
        print('All was OK, archiving cards...')
        inbox_list.archive_all_cards()


if __name__ == '__main__':
    main()

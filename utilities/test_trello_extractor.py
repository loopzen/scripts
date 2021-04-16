import pytest
from expects import expect, be_true, be_empty, contain

import configparser
import os
from trello import TrelloClient
from trello_extractor import print_to_file
from trello_extractor import get_info_all_cards
from trello_extractor import get_info_card

HOME_FOLDER = os.path.expanduser("~/")
config = configparser.ConfigParser()
config.read(HOME_FOLDER + "src/conf/loopzen.ini")


@pytest.fixture
def client():
    client = TrelloClient(
        api_key=config["TRELLO"]["API_KEY"],
        api_secret=config["TRELLO"]["API_SECRET"],
        token=config["TRELLO"]["TOKEN"]
    )
    return client


@pytest.fixture
def inbox_list(client):
    return client.get_list(config["TRELLO"]["GTD_LIST_INBOX_ID"])


# def setup_function(function):
#     """ setup any state tied to the execution of the given function.
#     Invoked for every test function in the module.
#     """
#     print("hola")
#
#
# def teardown_function(function):
#     """ teardown any state that was previously setup with a setup_function
#     call.
#     """


def test_print_to_file__fake_path():
    with pytest.raises(FileNotFoundError):
        info = "11111"
        file_path = "/home/loopzen/pppp/prueba.txt"
        print_to_file(info, file_path)


def test_print_to_file__fake_data():
    info = "11111"
    file_path = config['TRELLO']['PRUEBA_FILE']
    os.remove(file_path)
    print_to_file(info, file_path)
    exists = os.path.isfile(file_path)
    expect(exists).to(be_true)


def test_get_info_all_cards(inbox_list):
    new_card = inbox_list.add_card("test_card", "card test")
    cards = inbox_list.list_cards()
    info = get_info_all_cards(cards)
    expect(info).not_to(be_empty)
    expect(info).to(contain(new_card.name))
    expect(info).to(contain(new_card.description))


def test_get_card(client):
    gtd_list = client.get_list(config["TRELLO"]["GTD_LIST_INBOX_ID"])
    card = gtd_list.add_card("test_card", "card test")
    info = get_info_card(card)
    expect(info).to(contain(card.name))
    expect(info).to(contain(card.description))


if '__main__' == __name__:
    pytest.main()

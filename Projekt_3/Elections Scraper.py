"""Project 3: Elections Scraper"""
"""Choose territorial level from this URL: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ """

import os
import csv
import requests
import bs4


def main():
    url, csv_name = input_url_name()
    village_urls, v_ids = (get_villages_url(url))
    for v_url in village_urls:
        data = get_village_data(v_url, v_ids[village_urls.index(v_url)])
        make_csv(csv_name, data)
    print("=" * 50)
    print(f"All done, {csv_name} has been created!!!")


def input_url_name():
    try:
        url = input("Please insert URL adress: ")
        test_url = requests.get(url)
        test_url.raise_for_status()
        while True:
            csv_name = input("Please enter name of your csv file: ") + ".csv"
            forbidden_char = ["\\", "/", ":", "*", "?", '"', "<", ">", "|"]
            status = True
            for char in forbidden_char:
                if char in csv_name:
                    print()
                    print('File name can not contain these symbols: \ / : * ? " < > |.')
                    status = False
                    break
            if status is True:
                break
        print("=" * 50)
        print(f"Please wait, your file {csv_name} is being prepared.")
        return url, csv_name
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


def get_villages_url(url: str) -> tuple:
    url_main = url[:url.rfind("/")+1]   # https://volby.cz/pls/ps2017nss/
    content_r = bs4.BeautifulSoup(requests.get(url).text, "html.parser")
    tables_r = content_r.find_all("table")
    list_village_r = []
    list_village_id = []
    for table in tables_r:
        list_href_r = table.find_all(href=True)
        for item in list_href_r[::2]:
            a, item_split, b = str(item).split('"')
            list_village_r.append(url_main + item_split.replace("amp;", ""))
            list_village_id.append(item.text)
    return list_village_r, list_village_id


def get_village_data(v_url: str, v_index: int) -> dict:
    get_v_r = bs4.BeautifulSoup(requests.get(v_url).text, "html.parser")
    village_id = v_index
    village_search = get_v_r.find_all("h3")[2:]
    if not village_search:                                      # condition for Praha
        village_search = get_v_r.find_all("h3")[1:]
        village_name = village_search[0].text.replace("Obec: ", "")
    else:
        village_name = village_search[0].text.replace("Obec: ", "")
    voters = get_v_r.find(headers="sa2").text
    envelopes_given = get_v_r.find(headers="sa3").text
    envelopes_valid = get_v_r.find(headers="sa6").text

    village_data = {
        "Village ID": village_id,
        "Village": village_name.strip(),
        "Registered voters": voters,
        "Issued envelops": envelopes_given,
        "Valid votes": envelopes_valid
    }
    tables = get_v_r.find_all("table")[1:]
    for table in tables:
        rows = table.find_all("tr")[2:]
        for row in rows:
            cells = row.find_all("td")
            party_name = cells[1].text
            votes_number = cells[2].text
            village_data.update({party_name: votes_number})
    return village_data


def make_csv(name: str, data: dict) -> None:
    try:
        if os.path.exists(name):
            with open(name, "a+", newline="") as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=data.keys())
                writer.writerow(
                    data
                )
        else:
            with open(name, "w", newline="") as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=data.keys())
                writer.writeheader()
                writer.writerow(
                    data
                )
    except IOError as e:
        print("Ups something is wrong, program closed!")
        raise exit(e)


if __name__ == '__main__':
    main()

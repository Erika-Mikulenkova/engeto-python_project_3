"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Erika Mikulenková
email: erika.mikulenkova@gmail.com
discord: Erika M.
"""

import requests
from bs4 import BeautifulSoup
import sys
import csv

# Získání HTML stránky z webové adresy:
def make_soup(web_address):
    try:
        response = requests.get(web_address)
        return BeautifulSoup(response.text, features="html.parser")
    except:
        print("No valid URL was entered, please check the HTML validity. Exiting the program...")
        sys.exit()

# Zadání argumentů uživatelem v příkazové řádce:
def cmd_execution():
    try:
        web_page = sys.argv[1]
        save_as = sys.argv[2]

        if not save_as.lower().endswith('.csv') or len(sys.argv) != 3:
            print("Error: The arguments were not entered correctly.",
                  "To run the program successfully, the following must be entered in the command line:",
                  "python main.py \"URL\" \"output_name.csv\" and the second argument should be the output file name with the '.csv' extension.")
            sys.exit()

        return web_page, save_as
    
    except IndexError:
        print("Error: The arguments were not entered correctly.",
              "To run the program successfully, the following must be entered in the command line:",
              "python main.py \"URL\" \"output_name.csv\"")
        sys.exit()

# Získání odkazů na volební výsledky jednotlivých územních celků:
def get_urls_of_territorial_units(soup):
    tags = soup.find_all("td", {"class": "cislo"})
    return ["https://volby.cz/pls/ps2017nss/" + tag.find('a')['href'] if tag.find('a') else None for tag in tags]

# Získat kódy a názvy obcí z HTML:
def get_codes_and_names_of_municipalities(soup):
    tags1 = soup.find_all("td", {"class": "cislo"})
    codes_municipality = [tag.text for tag in tags1]

    tags2 = soup.find_all("td", {"class": "overflow_name"})
    names_municipality = [tag.text for tag in tags2]
    return codes_municipality, names_municipality

# Získat název obce z webové stránky:
def get_municipality_name(soup):
    return soup.find_all("h3")[-3].text.split(" ", maxsplit=1)[1].rstrip()

# Najít kód obce podle jejího názvu:
def find_matching_code_of_municipality(search_municipality, municipalities, codes):
    return dict(zip(municipalities, codes)).get(search_municipality)

# Získat voliče v seznamu, vydané obálky a platné hlasy z webové stránky:
def scrape_header_data_of_individual_municipality(soup):
    tags = soup.find_all("td", {"class": "cislo", "headers": ("sa2", "sa3", "sa6")})
    return convert_special_characters_to_number([tag.text for tag in tags])

# Získat názvy kandidujících strany z webové stránky:
def scrape_party_names(soup):
    return [tag.text for tag in soup.find_all("td", {"class": "overflow_name"})]

# Převést speciální znaky na číselné hodnoty:
def convert_special_characters_to_number(sequence_of_nonnumeric_data):
    return [int(data.replace("\xa0", "")) for data in sequence_of_nonnumeric_data]

# Získat počet hlasů jednotlivých stran v dané obci z webové stránky:
def scrape_number_of_votes_for_parties(soup):
    tags = soup.find_all("td", {"class": "cislo", "headers": ("t1sa2 t1sb3", "t2sa2 t2sb3")})
    return convert_special_characters_to_number([tag.text for tag in tags])

# Spojení klíčů do slovníku:
def create_dictionary(code, name, eligible_voters, envelopes, valid_votes, party, number_of_votes):
    dictionary = {
        "Code": code,
        "Location": name,
        "Registered": eligible_voters,
        "Envelopes": envelopes,
        "Valid": valid_votes
    }
    dictionary.update(zip(party, number_of_votes))
    return dictionary

# Uložení dat do csv:
def save_data_to_csv(list_of_election_results, file_name):
    header = list_of_election_results[0].keys()
    with open(file_name, mode="w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, delimiter=";", fieldnames=header)
        writer.writeheader()
        writer.writerows(list_of_election_results)
    print(f"The data has been successfully exported to the file: {file_name}")

# Hlavní funkce:
def main():
    url, file_name = cmd_execution()
    print("Loading data...")

    soup = make_soup(url)
    url_of_territorial_units = get_urls_of_territorial_units(soup)
    all_codes_municipality, all_names_municipality = get_codes_and_names_of_municipalities(soup)

    list_of_election_results = []

    for i, url in enumerate(url_of_territorial_units):
        soup_municipality = make_soup(url)
        municipality_name = get_municipality_name(soup_municipality)
        municipality_code = find_matching_code_of_municipality(municipality_name, all_names_municipality, all_codes_municipality)
        eligible_voters, issued_envelopes, valid_votes = scrape_header_data_of_individual_municipality(soup_municipality)
        list_of_participating_parties = scrape_party_names(soup_municipality)
        votes_for_parties = scrape_number_of_votes_for_parties(soup_municipality)

        dictionary = create_dictionary(
            municipality_code, 
            municipality_name, 
            eligible_voters, 
            issued_envelopes, 
            valid_votes, 
            list_of_participating_parties, 
            votes_for_parties)
        
        list_of_election_results.append(dictionary)

        # Výpis načítání dat v %
        if url_of_territorial_units:
            percent_done = (i + 1) / len(url_of_territorial_units) * 100
            print(f"Progress: {percent_done:.2f}%", end='\r')
            sys.stdout.flush()

    save_data_to_csv(list_of_election_results, file_name)

if __name__ == "__main__":
    main()
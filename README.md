# **Engeto_projekt_3: Elections scraper**

## Popis projektu:
Tento skript slouží pro získání a ukládání dat o výsledcích voleb do poslanecké sněmovny Parlamentu České republiky z roku 2017. Program přijímá jako vstup URL adresu konkrétní obce a generuje CSV soubor, který uvádí číslo obce, název obce, počet voličů, počet vydaných obálek, počet platných hlasů a výsledky jednotlivých stran včetně počtu hlasů pro každou stranu. Odkaz na výsledky voleb je: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ

## Instalace knihoven:
V kódu jsou použity knihovny **requests** a **BeautifulSoup**. Requests slouží pro stahování webových stránek a BeautifulSoup pro parsování HTML obsahu. Knihovny je vhodné nainstalovat do virtuálního prostředí.

Tyto knihovny lze nainstalovat ze souboru **requirements.txt** pomocí příkazu: **pip3 install -r requirements.txt**

## Spuštění programu:
Spustíte skript **main.py** a v příkazovém řádku zadáte **python main.py** a **dva povinné argumenty** vložené do uvozovek.

První argument je webová adresa, kde jsou dostupná volební data pro konkrétní obec.<br>
Druhý argument je Vámi zvolené jméno souboru.csv, do kterého budou data uložena.

### Příklad spuštění:
První argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8102<br>
Druhý argument: vysledky_voleb_Frydek_Mistek.csv

Vzorový příklad: **python main.py** "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8102" **"vysledky_voleb_Frydek_Mistek.csv"**

## Průběh stahování:
Loading data...<br>
The data has been successfully exported to the file: vysledky_voleb_frydek_mistek.csv

## Částečný výstup:
Code;Location;Registered;Envelopes;Valid;Občanská demokratická strana;Řád národa - Vlastenecká unie;CESTA ODPOVĚDNÉ SPOLEČNOSTI;Česká str.sociálně demokrat.;Radostné Česko;STAROSTOVÉ A NEZÁVISLÍ;Komunistická str.Čech a Moravy;Strana zelených;ROZUMNÍ-stop migraci,diktát.EU;Strana svobodných občanů;Blok proti islam.-Obran.domova;Občanská demokratická aliance;Česká pirátská strana;Česká národní fronta;Referendum o Evropské unii;TOP 09;ANO 2011;Dobrá volba 2016;SPR-Republ.str.Čsl. M.Sládka;Křesť.demokr.unie-Čs.str.lid.;Česká strana národně sociální;REALISTÉ;SPORTOVCI;Dělnic.str.sociální spravedl.;Svob.a př.dem.-T.Okamura (SPD);Strana Práv Občanů
598011;Baška;3093;2065;2053;175;1;1;124;1;49;192;21;12;21;1;0;216;0;0;44;665;2;9;194;1;16;7;3;293;5
598020;Bílá;285;178;178;19;0;0;14;0;10;21;3;1;0;1;0;12;1;0;3;52;0;0;15;0;3;0;0;23;0
511633;Bocanovice;358;197;197;20;0;0;32;0;3;13;3;1;0;0;0;18;0;1;1;45;0;0;43;0;0;0;0;17;0
598038;Brušperk;3199;2180;2158;211;3;0;183;0;53;204;25;17;30;3;1;171;0;2;61;767;3;3;145;0;22;5;0;241;8
598046;Bruzovice;708;441;440;31;1;0;35;1;16;38;4;1;4;0;0;30;0;0;11;139;0;1;45;0;3;1;2;75;2
511935;Bukovec;1052;628;626;31;0;0;51;0;67;16;1;3;1;0;0;46;0;1;12;121;0;0;200;1;0;3;2;70;0
598062;Bystřice;4179;2416;2394;172;4;0;314;1;64;124;24;11;37;1;0;209;1;1;69;754;1;4;276;0;20;3;1;293;10
598071;Čeladná;2378;1638;1626;173;2;1;108;3;60;113;23;13;26;0;2;140;0;0;65;442;101;1;122;0;14;4;0;206;7
598089;Dobrá;2515;1761;1747;150;2;0;146;1;29;135;18;10;18;3;1;137;0;0;31;615;0;1;200;0;11;2;3;229;5

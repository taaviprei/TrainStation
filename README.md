# TrainStation
Klass Passenger
__init__(self, passenger_id: str, seat: str) Konstruktor, mis salvestab reisija unikaalse identifikaatori (id) ning istekoha numbri.
Klass Train
__init__(self, train_id: str, carriages: int, seats_in_carriage: int): Konstruktor, mis salvestab rongi unikaalse id ning vagunite arvu ja ühes vagunis olevate istmete arvu instantsimuutujatesse.

get_seats_in_train(self) -> int: Meetod, mis tagastab istmete koguarvu terve rongi peale.

get_number_of_passengers(self) -> int: Meetod, mis tagastab rongi reisijate arvu.

get_passengers_in_carriages(self) -> dict: Meetod, mis tagastab sõnastiku vagunite ja reisijate andmetega. Selle sõnastiku võtmeks peaks olema vaguni number stringina (algab 1-st) ning väärtuseks on list selles vagunis olevate reisijatega. Kui vagunis pole reisijaid, siis see võti peab sõnastikus olema, aga väärtuseks jääb lihtsalt tühi list.

add_passenger(self, passenger: Passenger): Meetod, mis lisab reisija rongi peale rongijaamast. Kui reisijad satuvad rongijaama, siis nad tuleb kohe jagada rongidesse kasutades seda meetodit vastavalt reisijal oleva rongi id väärtusele.

Klass TrainStation
__init__(self, trains: list, passengers: list): Konstruktor, mis salvestab rongijaama sisse tulevate rongide ja reisijate nimekirjad instantsimuutujatesse.
Kohe rongijaama loomisel tuleb hakata jagama reisijad rongidesse vastavalt reisija istekoha numbris oleva rongi identifikaatorile ehk otsida vastav rong nimekirjast. Kui sellist rongi ei ole olemas või reisija ei õnnestunud rongi lisada, siis see reisija eemaldatakse rongijaamas olevast reisijate nimekirjast.

get_station_overview(self) -> list: Meetod, mis tagastab hetke seisundi aruande kõikiest rongijaamas olevatest rongidest listi kujul ning rongi info on sõnastiku kujul: [{'train_id': 'AB', 'carriages': 5, 'seats': 'kinni/kokku'}, {...}]. Ise vali, kuidas teed rongi objekist sellise sõnastiku kuju - kas rongi klassis või otse selles meetodis. (Vt. OOP: spetsiaalsed meetodid)

get_number_of_passengers(self): -> int: Meetod, mis tagastab rongijaama (rongidesse paigutatud) reisijate koguarvu.

Tingimused
Reisijad satuvad rongi klassi sisse listina. Reisija on Passenger klassi instants, millel on olemas unikaalne id ja istekoha number. Istekoha number tuleb kujul rongi_id-vaguni_nr-istekoha_nr, näiteks AB-2-14.
Kui mingil reisijal on selline istekoha number, mida ei ole rongis olemas (nt vaguni number on suurem, kui vagunite arv üldse või istekoha number on suurem, kui istekohtade arv vagunis), siis see reisija eemaldatakse reisijate nimekirjast ning ei lisata konkreetse rongi reisijate nimekirja.
Kui lisatava reisja istekoht on juba mõne teise reisija poolt võetud, siis seda reisjat rongi ei lisata ning eemaldatakse rongijaama reisijate nimekirjast.
Nõuded ja vihjed
Instantsimuutujate väärtust tagastavatele ehk getter meetoditele tuleb lisada @property dekoraator. See võimaldab luua vastava property jaoks ka setter meetodi, mis kutsutakse välja klassi siseselt automaatselt, kui selle muutuja väärtus muudetakse. Selles setter meetodis tavaliselt kirjeldatakse sisendandmete töötlemise loogika, mille järgi eraldatakse näiteks valed/katkised jne andmed ning instantsimuutujasse salvestatakse need juba õigel kujul.
On soovitatav kirjeldada reisijate andmete kontrollimise loogika eraldi privaatse meetodina, mis kutsutakse välja nimekirja määramisel.
Andmete kuvamisel kõik numbrilised väärtused antud ülesande raames on stringi kujul (nt vaguni ja istekoha numbrid jne).

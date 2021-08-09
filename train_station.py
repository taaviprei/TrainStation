"""Train Station."""


class Passenger:
    """Passenger class."""

    def __init__(self, passenger_id: str, seat: str):
        """Passenger init."""
        self.id = passenger_id
        self.seat = seat
        self.train_id = str(seat.split('-')[0])
        self.carriage_nr = int(seat.split('-')[1])
        self.seat_nr = int(seat.split('-')[2])

    @property
    def id(self) -> str:
        """Id."""
        return self._passenger_id

    @property
    def seat(self) -> str:
        """Seat."""
        return self._seat

    @seat.setter
    def seat(self, value: str):
        """Seat setter."""
        self._seat = value

    @id.setter
    def id(self, value: str):
        """Id setter."""
        self._passenger_id = value


class Train:
    """Train class."""

    def __init__(self, train_id: str, carriages: int, seats_in_carriage: int):
        """Train init."""
        self.passenger_list = []
        self._train_id = train_id
        self._carriages = carriages
        self._seats_in_carriage = seats_in_carriage

    @property
    def carriages(self) -> int:
        """Carriage."""
        return self._carriages

    @property
    def train_id(self) -> str:
        """Train ID."""
        return self._train_id

    @property
    def seats_in_carriage(self) -> int:
        """Seat in carriage."""
        return self._seats_in_carriage

    @property
    def passengers(self) -> list:
        """Passenger."""
        return self.passenger_list

    def get_seats_in_train(self) -> int:
        """Get seat."""
        return self.carriages * self.seats_in_carriage

    def get_number_of_passengers(self) -> int:
        """Get passenger."""
        return len(self.passenger_list)

    def get_passengers_in_carriages(self) -> dict:
        """Get passenger in carriage."""
        passengers_dict = {}
        for i in range(1, self.carriages + 1, 1):
            for passenger in self.passengers:
                carriage_nr = str(passenger.carriage_nr)
                temp_dict = passenger
                if str(i) == carriage_nr:
                    if carriage_nr in passengers_dict:
                        passengers_dict[carriage_nr].append(temp_dict)
                    elif carriage_nr not in passengers_dict:
                        passengers_dict.update({carriage_nr: [temp_dict]})
                elif str(i) not in passengers_dict:
                    passengers_dict.update({str(i): []})
        return passengers_dict

    @train_id.setter
    def train_id(self, value: str):
        """Train ID setter."""
        self._train_id = value

    @carriages.setter
    def carriages(self, value: int):
        """Carriage setter."""
        self._carriages = value

    @seats_in_carriage.setter
    def seats_in_carriage(self, value: int):
        """Seat in carriage setter."""
        self._seats_in_carriage = value

    def add_passenger(self, passenger: Passenger) -> Passenger:
        """Add passenger."""
        if self._carriages >= passenger.carriage_nr != 0 and self._seats_in_carriage >= passenger.seat_nr != 0:
            if self._train_id == passenger.train_id:
                if not self.passenger_list:
                    self.passenger_list.append(passenger)
                else:
                    for pa in self.passenger_list:
                        if pa.seat != passenger.seat:
                            self.passenger_list.append(passenger)
                            return passenger
                        elif pa.seat == passenger.seat:
                            return None
            else:
                return None
            return passenger
        else:
            return None


class TrainStation:
    """Trainstation class."""

    def __init__(self, trains: list, passengers: list):
        """Trainstation init."""
        self._passengers_list = []
        self.trains = trains
        self._passengers = passengers
        # self.nr_of_passengers = self.get_number_of_passengers()
        for train in self.trains:
            for passenger in self._passengers:
                if train.add_passenger(passenger):
                    self._passengers_list.append(passenger)

    def get_station_overview(self) -> list:
        """Get station overview."""
        trains_overview_list = []
        for train in self.trains:
            trains_overview = ({'train_id': train._train_id, 'carriages': train._carriages, 'seats':
                                str(train.get_number_of_passengers()) + '/' + str(train.get_seats_in_train())})
            trains_overview_list.append(trains_overview)
        return trains_overview_list

    def get_number_of_passengers(self) -> int:
        """Get number of passengers."""
        return len(self._passengers_list)

    @property
    def passengers(self) -> list:
        """Passenger."""
        return self._passengers_list

    @passengers.setter
    def passengers(self, value_list: list):
        """Passenger setter."""
        pass

    @property
    def trains(self) -> list:
        """Train."""
        return self._trains

    @trains.setter
    def trains(self, value_list: list):
        """Train setter."""
        self._trains = value_list


if __name__ == "__main__":
    # passengers
    p = Passenger("ago", "1-2-3")
    print(p.seat)
    assert p.seat == '1-2-3'
    print(p.id)
    assert p.id == 'ago'

    # train check
    t = Train("TRAIN", 2, 2)
    print(t.get_number_of_passengers())
    assert t.get_number_of_passengers() == 0
    p1 = Passenger("mati", "TRAIN-1-1")
    result = t.add_passenger(p1)
    print(result)
    assert result == p1  # must return the same object

    print(t.get_number_of_passengers())  # 1
    assert t.get_number_of_passengers() == 1

    print(t.passengers[0].seat)  # TRAIN-1-1
    assert t.passengers == [p1]

    print(t.get_passengers_in_carriages())  # {'1': [<__main__.Passenger object at 0x00000247824DCD08>], '2': []}
    assert t.get_passengers_in_carriages() == {'1': [p1], '2': []}

    # illegal passengers
    p2 = Passenger("bad carriage", "TRAIN-3-1")
    result = t.add_passenger(p2)
    print(result)  # None
    assert not result
    assert t.get_number_of_passengers() == 1

    p3 = Passenger("bad seat", "TRAIN-1-3")
    result = t.add_passenger(p3)
    print(result)  # None
    assert not result
    assert t.get_number_of_passengers() == 1

    p4 = Passenger("bad train", "BUS-1-1")
    result = t.add_passenger(p4)
    print(result)  # None
    assert not result
    assert t.get_number_of_passengers() == 1

    p5 = Passenger("seat taken", "TRAIN-1-1")
    result = t.add_passenger(p5)
    print(result)  # None
    assert not result
    assert t.get_number_of_passengers() == 1

# station
    t1 = Train("A", 2, 10)
    ts = TrainStation([t1], [])
    assert ts.trains == [t1]
    assert ts.get_number_of_passengers() == 0
    assert t1.get_number_of_passengers() == 0
    print(ts.get_station_overview())
    # [{'carriages': 2, 'seats': '0/20', 'train_id': 'A'}]
    assert ts.get_station_overview() == [{'carriages': 2, 'seats': '0/20', 'train_id': 'A'}]

    t2 = Train("T2", 2, 2)
    p6 = Passenger("p6", "T2-1-1")
    p7 = Passenger("p7", "T2-2-1")
    passengers = [p6, p7]
    ts = TrainStation([t2], passengers)
    print(ts.get_number_of_passengers())
    assert ts.get_number_of_passengers() == 2
    assert t2.get_number_of_passengers() == 2
    assert t2.get_passengers_in_carriages() == {'1': [p6], '2': [p7]}
    assert len(passengers) == 2

    t3 = Train("TRAIN", 2, 2)
    t4 = Train("T2", 2, 2)
    p1 = Passenger("mati", "TRAIN-1-1")
    p2 = Passenger("bad carriage", "TRAIN-3-1")
    p3 = Passenger("bad seat", "TRAIN-1-3")
    p4 = Passenger("bad train", "BUS-1-1")
    p5 = Passenger("seat taken", "TRAIN-1-1")
    p6 = Passenger("p6", "T2-1-1")
    p7 = Passenger("p7", "T2-2-1")
    passengers = [p1, p2, p3, p4, p5, p6, p7]
    ts = TrainStation([t3, t4], passengers)
    assert ts.get_number_of_passengers() == 3
    assert t3.get_number_of_passengers() == 1
    assert t4.get_number_of_passengers() == 2
    print(t3.get_passengers_in_carriages())
    assert t3.get_passengers_in_carriages() == {'1': [p1], '2': []}
    print(t4.get_passengers_in_carriages())
    assert t4.get_passengers_in_carriages() == {'1': [p6], '2': [p7]}
    assert len(passengers) == 7
    print(ts.get_station_overview())
    # [{'carriages': 2, 'seats': '1/4', 'train_id': 'TRAIN'}, {'carriages': 2, 'seats': '2/4', 'train_id': 'T2'}]
    assert ts.get_station_overview() == [{'carriages': 2, 'seats': '1/4', 'train_id': 'TRAIN'},
                                         {'carriages': 2, 'seats': '2/4', 'train_id': 'T2'}]

    print("If you see this, all the above is correct. Congrats!")

"""if __name__ == "__main__":
    # passengers
    p1 = Passenger("10", "AA-1-0")
    p2 = Passenger("11", "AA-1-1")
    p3 = Passenger("12", "AA-1-1")
    p4 = Passenger("13", "AA-1-2")
    p5 = Passenger("14", "AA-2-5")
    p6 = Passenger("15", "AB-2-4")
    p7 = Passenger("16", "AB-10-4")
    p8 = Passenger("17", "AB-0-0")
    passengers = [p1, p2, p3, p4, p5, p6, p7, p8]

    # trains for station
    t1 = Train("AA", 5, 5)
    t2 = Train("AB", 2, 4)
    trains = [t1, t2]
    # train for additional tests
    t3 = Train("AA", 5, 5)
    valid_passengers = [p2, p4, p5]

    # stations
    s1 = TrainStation(trains, passengers)
    stations = [s1]

    # TEST FUNCTION
    def basic_test(testname, output, expected):
        """"Compare output with expected result.""""
        if output == expected:
            print(f"{testname}: PASSED")
        else:
            print(f"{testname}: FAIL\n {output} - your output \n {expected} - expected")

    # TESTS
    print("INIT TESTS")
    basic_test("init_passengers", [p.id for p in passengers],
               ['10', '11', '12', '13', '14', '15', '16', '17'])
    basic_test("init_trains", [t.train_id for t in trains], ['AA', 'AB'])
    basic_test("init_station", s1.trains, trains)

    # ARE YOU USING ADD_PASSENGER CORRECTLY?
    print("\nADD_PASSENGER TESTS")
    add_passenger_correct = [False, True, False, True, True, False, False, False] or valid_passengers
    basic_test("add_passengers_to_train3_without_station", [t3.add_passenger(p) for p in passengers],
               add_passenger_correct)
    basic_test("check_for_valid_passengers_train3", [p.id for p in t3.passengers], ['11', '13', '14'])

    print("\nTRAINS AT THE STATION")
    basic_test("get_seats_in_train", [t.get_seats_in_train() for t in trains], [25, 8])
    basic_test("get_number_of_passengers", [t.get_number_of_passengers() for t in trains], [3, 1])
    basic_test("check_for_valid_passengers_station", [p.id for p in s1.passengers], ['11', '13', '14', '15'])
    get_passengers_in_carriages_correct = [{'1': [p2, p4], '2': [p5], '3': [], '4': [], '5': []}, {'1': [], '2': [p6]}]
    basic_test("get_passengers_in_carriages", [t.get_passengers_in_carriages() for t in trains],
               get_passengers_in_carriages_correct)
    get_station_overview_correct = [{'train_id': 'AA', 'carriages': 5, 'seats': '3/25'},
                                    {'train_id': 'AB', 'carriages': 2, 'seats': '1/8'}]
    basic_test("get_station_overview", s1.get_station_overview(), get_station_overview_correct)
    basic_test("get_number_of_passengers", s1.get_number_of_passengers(), 4)"""

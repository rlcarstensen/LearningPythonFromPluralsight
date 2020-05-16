# in the console
from airtravel import Flight
f = Flight("SN060")
f.number()
f._number

from airtravel import *
a = Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6)
a.registration()
a.model()
a.seating_plan()

from airtravel import *
f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6))
f.aircraft_model()

from airtravel import *
f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6))
f._seating
from pprint import pprint as pp
pp(f._seating)

from airtravel import *
from pprint import pprint as pp
f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6))
f.allocate_seat("12A", "Guido van Rossum")
f.allocate_seat("12A", "Rasmus Lerdorf")
f.allocate_seat("15F", "Bjorn Stroustrup")
f.allocate_seat("15E", "Anders Hejlsberg")
f.allocate_seat("1C", "John McCarthy")
f.allocate_seat("1D", "Richard Hickey")
f.allocate_seat("DD", "Larry Wall")
pp(f._seating)


from airtravel import *
from pprint import pprint as pp
f = make_flight()
f
f.relocate_passenger("12A", "15D")
pp(f._seating)

from airtravel import *
f = make_flight()
f.num_available_seats()
6 * 22 - 5

from airtravel import *
f = make_flight()
f.make_boarding_cards(console_card_printer)

from airtravel import *
f, g = make_flights()
f.aircraft_model()
g.aircraft_model()
f.num_available_seats()
g.num_available_seats()
g.relocate_passenger("55K", "13G")
g.make_boarding_cards(console_card_printer)

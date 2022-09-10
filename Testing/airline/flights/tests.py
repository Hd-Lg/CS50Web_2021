from django.test import TestCase
from .models import Flight, Airport, Passenger
# Create your tests here.


class FlightTestCase(TestCase):
    def setUp(self):
        # Create airports
        a1 = Airport.objects.create(code="AAA", city="City A")
        a2 = Airport.objects.create(code="BBB", city="City B")

        # Create flights
        Fligh.objects.create(origin=a1, destination=a2, duration=100)
        Fligh.objects.create(origin=a1, destination=a1, duration=200)
        Fligh.objects.create(origin=a1, destination=a2, duration=-10)

        def test_departures_count(self):
            a = Airport.objects.get(code="AAA")
            self.assertEqual(a.departures.count(), 3)

        def test_arrivals_countts(self):
            a = Airport.objects.get(code="AAA")
            self.assertEqual(a.arrivals.count(), 1)

        def test_valid_flight(self):
            a1 = Airport.objects.get(code="AAA")
            a2 = Airport.objects.get(code="BBB")
            f = Flight.objects.get(origin=a1, destination=a2, duration=100)
            self.assertTrue(f.is_valid_flight())

        def test_invalid_flight_destination(self):
            a1 = Airport.objects.get(code="AAA")
            f = Flight.objects.get(origin=a1, destination=a1)
            self.assertFalse(f.is_valid_flight())


        def test_invalid_flight_duration(self):
            a1 = Airport.objects.get(code="AAA")
            a2 = Airport.objects.get(code="BBB")
            f = Flight.objects.get(origin=a1, destination=a2, duration=-100)
            self.assertFalse(f.is_valid_flight())

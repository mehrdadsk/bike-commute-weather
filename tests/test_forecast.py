import json
import unittest
from pathlib import Path

from forecast import forecast_rows


class ForecastTests(unittest.TestCase):
    def setUp(self):
        fixture = Path(__file__).parent / "fixtures" / "copenhagen-nowcast.json"
        with fixture.open(encoding="utf-8-sig") as file:
            self.rows = forecast_rows(json.load(file))

    def test_first_row_preserves_forecast_values(self):
        self.assertEqual(self.rows[0], {
            "time_utc": "2026-11-27T13:05:00Z",
            "rain_mm_per_hour": 0.0,
            "wind_gust_m_per_second": 7.6,
        })

    def test_missing_gust_stays_missing(self):
        self.assertIsNone(self.rows[1]["wind_gust_m_per_second"])
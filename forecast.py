import json
from pathlib import Path


def forecast_rows(forecast):
    rows = []
    for point in forecast["properties"]["timeseries"]:
        details = point["data"]["instant"]["details"]
        rows.append({
            "time_utc": point["time"],
            "rain_mm_per_hour": details.get("precipitation_rate"),
             "wind_gust_m_per_second": details.get("wind_speed_of_gust") or 0,
        })
    return rows


if __name__ == "__main__":
    fixture = Path(__file__).parent / "tests" / "fixtures" / "copenhagen-nowcast.json"
    with fixture.open(encoding="utf-8-sig") as file:
        forecast = json.load(file)

    rows = forecast_rows(forecast)
    print(f"Loaded {len(rows)} forecast rows")
    for row in rows[:2]:
        print(row)
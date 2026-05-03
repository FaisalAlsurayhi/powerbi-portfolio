from __future__ import annotations

import csv
import random
from datetime import date
from pathlib import Path

random.seed(2030)

OUT = Path(__file__).parent / "data" / "eastern_province_real_estate_transactions.csv"

CITIES = {
    "Khobar": {
        "districts": ["Al Aqrabiyah", "Al Olaya", "Al Khuzama", "Corniche", "Al Rakah"],
        "price_factor": 1.18,
    },
    "Dammam": {
        "districts": ["Al Faisaliyah", "Al Shati", "Al Manar", "Al Badiyah", "Al Adamah"],
        "price_factor": 1.00,
    },
    "Dhahran": {
        "districts": ["Doha", "Dana", "Al Qusur", "University Area"],
        "price_factor": 1.25,
    },
    "Jubail": {
        "districts": ["Fanateer", "Al Huwaylat", "Jalmudah", "Jubail Downtown"],
        "price_factor": 0.92,
    },
}

PROPERTY_TYPES = {
    "Apartment": {"segment": "Residential", "area": (85, 210), "base_ppsqm": 5200},
    "Villa": {"segment": "Residential", "area": (230, 650), "base_ppsqm": 4300},
    "Residential Land": {"segment": "Residential", "area": (300, 900), "base_ppsqm": 2600},
    "Commercial Unit": {"segment": "Commercial", "area": (90, 350), "base_ppsqm": 7600},
    "Commercial Land": {"segment": "Commercial", "area": (500, 1600), "base_ppsqm": 4200},
}

MONTH_FACTORS = {
    1: 0.98,
    2: 1.00,
    3: 0.96,
    4: 1.03,
    5: 1.08,
    6: 1.02,
    7: 0.94,
    8: 0.95,
    9: 1.01,
    10: 1.04,
    11: 1.05,
    12: 1.09,
}


def choose_property_type() -> str:
    return random.choices(
        population=list(PROPERTY_TYPES),
        weights=[35, 24, 22, 12, 7],
        k=1,
    )[0]


def make_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    transaction_id = 10001

    for month in range(1, 13):
        for city, info in CITIES.items():
            city_volume = {
                "Khobar": 14,
                "Dammam": 16,
                "Dhahran": 9,
                "Jubail": 10,
            }[city]
            month_volume = max(6, round(city_volume * MONTH_FACTORS[month]))

            for _ in range(month_volume):
                property_type = choose_property_type()
                spec = PROPERTY_TYPES[property_type]
                district = random.choice(info["districts"])
                area = random.randint(*spec["area"])

                district_factor = 1 + (info["districts"].index(district) - 2) * 0.025
                noise = random.uniform(0.88, 1.14)
                price_per_sqm = round(spec["base_ppsqm"] * info["price_factor"] * district_factor * MONTH_FACTORS[month] * noise)
                sale_price = round(area * price_per_sqm / 1000) * 1000

                transaction_day = random.randint(1, 27)
                transaction_type = random.choices(["Sale", "Resale"], weights=[72, 28], k=1)[0]

                rows.append(
                    {
                        "Transaction_ID": f"EP-{transaction_id}",
                        "Date": date(2024, month, transaction_day).isoformat(),
                        "City": city,
                        "District": district,
                        "Property_Type": property_type,
                        "Segment": spec["segment"],
                        "Area_sqm": area,
                        "Sale_Price_SAR": sale_price,
                        "Price_per_sqm": price_per_sqm,
                        "Transaction_Type": transaction_type,
                    }
                )
                transaction_id += 1

    return rows


def main() -> None:
    rows = make_rows()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {OUT}")


if __name__ == "__main__":
    main()

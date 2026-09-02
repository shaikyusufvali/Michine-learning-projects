import os
import numpy as np
import pandas as pd

# Reproducibility
np.random.seed(42)

# ---------------------------------------------------------
# PATHS
# ---------------------------------------------------------

RAW_DATA_PATH = "data/raw"

os.makedirs(RAW_DATA_PATH, exist_ok=True)


# ---------------------------------------------------------
# COMMON DATA
# ---------------------------------------------------------

TRAIN_NAMES = [
    "Vande Bharat",
    "Rajdhani Express",
    "Shatabdi Express",
    "Duronto Express",
    "Garib Rath",
    "Intercity Express",
    "Jan Shatabdi",
    "Superfast Express",
    "Deccan Express",
    "Krishna Express"
]

STATIONS = [
    "Hyderabad",
    "Secunderabad",
    "Vijayawada",
    "Guntur",
    "Warangal",
    "Visakhapatnam",
    "Tirupati",
    "Nellore",
    "Kurnool",
    "Nizamabad"
]

WEATHER = [
    "Clear",
    "Cloudy",
    "Rain",
    "Heavy Rain",
    "Fog"
]

DIRECTIONS = [
    ("Hyderabad", "Vijayawada"),
    ("Vijayawada", "Visakhapatnam"),
    ("Hyderabad", "Warangal"),
    ("Guntur", "Tirupati"),
    ("Secunderabad", "Nizamabad"),
    ("Nellore", "Chennai"),
    ("Kurnool", "Hyderabad"),
]


# ---------------------------------------------------------
# 1. TRAIN DELAY DATASET
# ---------------------------------------------------------

def generate_train_data(n=5000):

    data = []

    for i in range(n):

        train_id = f"TRN{i + 1001}"

        train_name = np.random.choice(TRAIN_NAMES)

        source, destination = DIRECTIONS[
            np.random.randint(len(DIRECTIONS))
        ]

        distance_km = np.random.randint(80, 700)

        hour = np.random.randint(0, 24)

        scheduled_departure = f"{hour:02d}:00"

        weather = np.random.choice(
            WEATHER,
            p=[0.45, 0.25, 0.15, 0.08, 0.07]
        )

        temperature = np.random.randint(18, 42)

        rainfall = np.random.uniform(0, 80)

        station_delay = max(
            0,
            np.random.normal(5, 4)
        )

        previous_delay = max(
            0,
            np.random.normal(8, 7)
        )

        weather_effect = {
            "Clear": 0,
            "Cloudy": 2,
            "Rain": 7,
            "Heavy Rain": 15,
            "Fog": 10
        }[weather]

        peak_effect = (
            8 if 7 <= hour <= 10
            else 6 if 17 <= hour <= 21
            else 0
        )

        delay_minutes = (
            station_delay
            + previous_delay * 0.4
            + weather_effect
            + peak_effect
            + distance_km * 0.01
            + np.random.normal(0, 4)
        )

        delay_minutes = max(
            0,
            round(delay_minutes, 2)
        )

        data.append([
            train_id,
            train_name,
            source,
            destination,
            distance_km,
            scheduled_departure,
            weather,
            temperature,
            round(rainfall, 2),
            round(station_delay, 2),
            round(previous_delay, 2),
            delay_minutes
        ])

    columns = [
        "train_id",
        "train_name",
        "source",
        "destination",
        "distance_km",
        "scheduled_departure",
        "weather",
        "temperature",
        "rainfall",
        "station_delay",
        "previous_delay",
        "delay_minutes"
    ]

    df = pd.DataFrame(data, columns=columns)

    df.to_csv(
        f"{RAW_DATA_PATH}/train_data.csv",
        index=False
    )

    print("train_data.csv created")


# ---------------------------------------------------------
# 2. PASSENGER DEMAND DATASET
# ---------------------------------------------------------

def generate_passenger_data(n=5000):

    data = []

    for i in range(n):

        date = pd.Timestamp("2025-01-01") + pd.Timedelta(
            days=np.random.randint(0, 365)
        )

        station = np.random.choice(STATIONS)

        train_id = f"TRN{np.random.randint(1001, 6001)}"

        hour = np.random.randint(0, 24)

        day_of_week = date.dayofweek

        holiday = np.random.choice(
            [0, 1],
            p=[0.9, 0.1]
        )

        weather = np.random.choice(
            WEATHER,
            p=[0.5, 0.25, 0.12, 0.08, 0.05]
        )

        special_event = np.random.choice(
            [0, 1],
            p=[0.92, 0.08]
        )

        base_passengers = 300

        if 7 <= hour <= 10:
            base_passengers += 250

        elif 17 <= hour <= 21:
            base_passengers += 300

        elif 11 <= hour <= 16:
            base_passengers += 100

        if day_of_week >= 5:
            base_passengers += 120

        if holiday:
            base_passengers += 250

        if special_event:
            base_passengers += 350

        if weather in ["Rain", "Heavy Rain"]:
            base_passengers -= 50

        passenger_count = (
            base_passengers
            + np.random.normal(0, 70)
        )

        passenger_count = max(
            20,
            round(passenger_count)
        )

        data.append([
            date.date(),
            station,
            train_id,
            hour,
            day_of_week,
            holiday,
            weather,
            special_event,
            passenger_count
        ])

    columns = [
        "date",
        "station",
        "train_id",
        "hour",
        "day_of_week",
        "holiday",
        "weather",
        "special_event",
        "passenger_count"
    ]

    df = pd.DataFrame(data, columns=columns)

    df.to_csv(
        f"{RAW_DATA_PATH}/passenger_data.csv",
        index=False
    )

    print("passenger_data.csv created")


# ---------------------------------------------------------
# 3. PREDICTIVE MAINTENANCE DATASET
# ---------------------------------------------------------

def generate_maintenance_data(n=5000):

    data = []

    for i in range(n):

        train_id = f"TRN{np.random.randint(1001, 6001)}"

        engine_temperature = np.random.normal(
            85, 12
        )

        brake_pressure = np.random.normal(
            95, 8
        )

        vibration = np.random.normal(
            4, 1.5
        )

        wheel_condition = np.random.randint(
            50, 101
        )

        engine_hours = np.random.randint(
            1000, 15000
        )

        last_service_days = np.random.randint(
            1, 365
        )

        maintenance_count = np.random.randint(
            0, 15
        )

        risk_score = 0

        if engine_temperature > 100:
            risk_score += 2

        if brake_pressure < 85:
            risk_score += 2

        if vibration > 6:
            risk_score += 2

        if wheel_condition < 65:
            risk_score += 2

        if engine_hours > 10000:
            risk_score += 1

        if last_service_days > 250:
            risk_score += 2

        if maintenance_count > 10:
            risk_score += 1

        failure_probability = min(
            0.85,
            0.05 + risk_score * 0.10
        )

        failure = np.random.choice(
            [0, 1],
            p=[
                1 - failure_probability,
                failure_probability
            ]
        )

        data.append([
            train_id,
            round(engine_temperature, 2),
            round(brake_pressure, 2),
            round(vibration, 2),
            wheel_condition,
            engine_hours,
            last_service_days,
            maintenance_count,
            failure
        ])

    columns = [
        "train_id",
        "engine_temperature",
        "brake_pressure",
        "vibration",
        "wheel_condition",
        "engine_hours",
        "last_service_days",
        "maintenance_count",
        "failure"
    ]

    df = pd.DataFrame(data, columns=columns)

    df.to_csv(
        f"{RAW_DATA_PATH}/maintenance_data.csv",
        index=False
    )

    print("maintenance_data.csv created")


# ---------------------------------------------------------
# 4. STATION CROWD DATASET
# ---------------------------------------------------------

def generate_station_crowd(n=5000):

    data = []

    for i in range(n):

        date = pd.Timestamp("2025-01-01") + pd.Timedelta(
            days=np.random.randint(0, 365)
        )

        station = np.random.choice(STATIONS)

        hour = np.random.randint(0, 24)

        day_of_week = date.dayofweek

        holiday = np.random.choice(
            [0, 1],
            p=[0.9, 0.1]
        )

        train_frequency = np.random.randint(
            2, 15
        )

        passenger_count = np.random.randint(
            100, 1500
        )

        entry_count = int(
            passenger_count * np.random.uniform(
                0.4, 0.8
            )
        )

        exit_count = int(
            passenger_count * np.random.uniform(
                0.2, 0.6
            )
        )

        crowd_score = (
            passenger_count * 0.05
            + train_frequency * 4
        )

        if 7 <= hour <= 10:
            crowd_score += 30

        if 17 <= hour <= 21:
            crowd_score += 40

        if day_of_week >= 5:
            crowd_score += 20

        if holiday:
            crowd_score += 35

        if crowd_score < 70:
            crowd_level = "Low"

        elif crowd_score < 120:
            crowd_level = "Medium"

        else:
            crowd_level = "High"

        data.append([
            date.date(),
            station,
            hour,
            day_of_week,
            holiday,
            train_frequency,
            passenger_count,
            entry_count,
            exit_count,
            crowd_level
        ])

    columns = [
        "date",
        "station",
        "hour",
        "day_of_week",
        "holiday",
        "train_frequency",
        "passenger_count",
        "entry_count",
        "exit_count",
        "crowd_level"
    ]

    df = pd.DataFrame(data, columns=columns)

    df.to_csv(
        f"{RAW_DATA_PATH}/station_crowd.csv",
        index=False
    )

    print("station_crowd.csv created")


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

if __name__ == "__main__":

    print("\nGenerating RailPulse-AI datasets...\n")

    generate_train_data()
    generate_passenger_data()
    generate_maintenance_data()
    generate_station_crowd()

    print("\nAll datasets generated successfully!")
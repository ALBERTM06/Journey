import numpy as np
import pandas as pd
from datetime import date

df = pd.read_csv('ndvi_readings.csv')

# NDVI reference scale:
# < 0.2  = bare soil / non-vegetated
# 0.2 - 0.4 = sparse vegetation
# 0.4 - 0.6 = moderate vegetation
# 0.6 - 0.8 = healthy vegetation
# > 0.8  = dense vegetation (cropland, forest)

LOW_THRESHOLD  = 0.4   # flag readings below this
HIGH_THRESHOLD = 0.75  # flag readings above this


def classify_ndvi(value):
    if value < 0.2:
        return "Bare/Non-vegetated"
    elif value < 0.4:
        return "Sparse"
    elif value < 0.6:
        return "Moderate"
    elif value < 0.8:
        return "Healthy"
    else:
        return "Dense"


# View all readings
def view_all():
    if df.empty:
        print("No data on record.")
        return
    print("\nAll NDVI Readings:")
    print(df.to_string(index=False))
    print(f"\nTotal readings: {len(df)}")


# Add a new reading
def add_reading():
    global df

    location = input("Enter location name: ")
    date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if date_input == "":
        date_input = str(date.today())

    try:
        ndvi = float(input("Enter NDVI value (-1 to 1): "))
        if not -1 <= ndvi <= 1:
            print("NDVI must be between -1 and 1.")
            return
    except ValueError:
        print("Invalid NDVI value.")
        return

    try:
        lat = float(input("Enter latitude: "))
        lon = float(input("Enter longitude: "))
    except ValueError:
        print("Invalid coordinates.")
        return

    notes = input("Enter notes (optional): ")

    new_row = pd.DataFrame({
        'Location':  [location],
        'Date':      [date_input],
        'NDVI':      [ndvi],
        'Latitude':  [lat],
        'Longitude': [lon],
        'Notes':     [notes]
    })

    df = pd.concat([df, new_row], ignore_index=True)
    print(f"\nReading added. Classification: {classify_ndvi(ndvi)}")


# Search readings by location
def search_by_location():
    location = input("Enter location name: ")
    results = df[df['Location'] == location]

    if results.empty:
        print("No readings found for that location.")
        return

    print(f"\nReadings for {location}:")
    print(results.to_string(index=False))


# Analyse readings per location - avg, min, max
def analyse_by_location():
    if df.empty:
        print("No data to analyse.")
        return

    print("\nNDVI Summary by Location:")
    summary = df.groupby('Location')['NDVI'].agg(['mean', 'min', 'max', 'count'])
    summary.columns = ['Mean NDVI', 'Min NDVI', 'Max NDVI', 'Readings']
    summary['Classification'] = summary['Mean NDVI'].apply(classify_ndvi)
    summary = summary.round(3)
    print(summary.to_string())


# Flag readings outside the normal thresholds
def flag_readings():
    low  = df[df['NDVI'] < LOW_THRESHOLD]
    high = df[df['NDVI'] > HIGH_THRESHOLD]

    print(f"\nFlagged LOW readings (NDVI < {LOW_THRESHOLD}) — possible stress or bare ground:")
    if low.empty:
        print("None.")
    else:
        print(low[['Location', 'Date', 'NDVI', 'Notes']].to_string(index=False))

    print(f"\nFlagged HIGH readings (NDVI > {HIGH_THRESHOLD}) — dense vegetation:")
    if high.empty:
        print("None.")
    else:
        print(high[['Location', 'Date', 'NDVI', 'Notes']].to_string(index=False))


# Filter readings by date range
def filter_by_date():
    start = input("Enter start date (YYYY-MM-DD): ")
    end   = input("Enter end date (YYYY-MM-DD): ")

    try:
        mask = (df['Date'] >= start) & (df['Date'] <= end)
        results = df[mask]
    except Exception:
        print("Invalid date format.")
        return

    if results.empty:
        print("No readings found in that date range.")
        return

    print(f"\nReadings from {start} to {end}:")
    print(results.to_string(index=False))


# Delete a specific reading by row number
def delete_reading():
    global df
    view_all()

    try:
        row_num = int(input("\nEnter the row number to delete (0-based): "))
        if row_num not in df.index:
            print("Row not found.")
            return
    except ValueError:
        print("Enter a valid number.")
        return

    confirm = input(f"Delete reading at row {row_num}? (y/n): ")
    if confirm.lower() == 'y':
        df.drop(index=row_num, inplace=True)
        df.reset_index(drop=True, inplace=True)
        print("Reading deleted.")
    else:
        print("Deletion cancelled.")


# Main program
print("Neoventis — NDVI Field Data Tracker")

while True:
    print("\nOptions:"
          "\n 1. View all readings"
          "\n 2. Add new reading"
          "\n 3. Search by location"
          "\n 4. Analyse by location (avg / min / max)"
          "\n 5. Flag unusual readings"
          "\n 6. Filter by date range"
          "\n 7. Delete a reading"
          "\n 8. Exit")

    try:
        option = int(input("\nSelect an option: "))
    except ValueError:
        print("Enter a valid number.")
        continue

    if option == 1:
        view_all()
    elif option == 2:
        add_reading()
    elif option == 3:
        search_by_location()
    elif option == 4:
        analyse_by_location()
    elif option == 5:
        flag_readings()
    elif option == 6:
        filter_by_date()
    elif option == 7:
        delete_reading()
    elif option == 8:
        print("Saving and exiting...")
        break
    else:
        print("Invalid option.")

df.to_csv('ndvi_readings.csv', index=False)
print("Data saved.")
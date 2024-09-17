import pandas as pd
import datetime


def read_file(path):
    df = pd.read_csv(path)
    df.columns = [col.replace(" ", "_").lower() for col in df.columns]
    return df


# the values of the data has = and "" so delete them
def clean_data(x):
    if pd.isna(x):
        return x
    x = x.replace('"', "")
    x = x.replace("=", "")
    return x


def process_Htask(df):

    df = df[df["hotel_name"] == "Salet Al Bait"]

    df = df.replace("-", pd.NA, inplace=False)

    # cleaning: remove = and '' from the text
    missy = [
        "res_#",
        "booking_date",
        "arrival",
        "dept",
        "cancellation_date",
        "last_modified_date",
    ]
    for column in missy:
        df[column] = df[column].apply(clean_data)

    # 0 numbers
    df["mobile_no"] = df["mobile_no"].apply(
        lambda x: pd.NA if pd.notna(x) and x == "0" else x
    )

    # convert to date
    date_columns = [
        "booking_date",
        "arrival",
        "dept",
        "cancellation_date",
        "last_modified_date",
    ]
    for column in date_columns:
        df[column] = pd.to_datetime(df[column], format="%d/%m/%Y")

    # convert to time
    df["booking_time"] = pd.to_datetime(
        df["booking_time"], format="%I:%M:%S %p"
    ).dt.time

    # make time and date in same column
    df["booking_datetime"] = df.apply(
        lambda row: datetime.datetime.combine(row["booking_date"], row["booking_time"]),
        axis=1,
    )

    # change source to only have from Booking and Walk-in
    df["source"] = df.apply(
        lambda row: "Walk-in" if pd.isna(row["voucher"]) else "Booking.com", axis=1
    )

    # convert to float
    df["commission"] = df["commission"].apply(lambda x: float(x) if pd.notna(x) else 0)

    # null numbers
    df["res_#"].fillna("Unknown", inplace=True)
    df["mobile_no"].fillna(pd.NA, inplace=True)
    df["folio_no"].fillna("Unknown", inplace=True)
    df["country"].fillna("Unknow", inplace=True)
    df["payment_type_"].fillna("Unknown", inplace=True)

    # voucher is 43XXXXX/50XXXX , removes part after slash
    df["voucher"] = df["voucher"].apply(
        lambda x: x.split("/")[0] if pd.notna(x) and "/" in x else x
    )
    # convert it to number like booking data
    # df['voucher'] = pd.to_numeric(df['voucher'], errors='coerce')

    # new transform data
    df["adults"] = df["pax"].apply(lambda x: int(x[0]))
    df["children"] = df["pax"].apply(lambda x: int(x[-1]))

    # delete unnecessary columns (most of them are empty)
    df.drop(
        [
            "hotel_name",
            "city",
            "zip_code",
            "state",
            "preference",
            "travelagent",
            "salesperson",
            "market_code_",
            "unnamed:_40",
            "booking_date",
            "reservationn_type",
            "email",
            "rate_type",
            "due_amt.",
            "booking_time",
            "deposit",
            "pax",
            "last_modified_date",
            "last_modified_by",
            "number_of_rooms_booked",
        ],
        axis=1,
        inplace=True,
    )

    # to have consist data across all data
    df.rename(
        columns={
            "new_source": "source",
            "payment_type_": "payment_type",
            "res_#": "reservation_number",
            "booking_datetime": "booking_date",
            "dept": "departure",
            "room": "room_type",
            "total_charges": "price_by_nights",
        },
        inplace=True,
    )

    # save the file
    # df.to_csv('clean_data,csv', index=False)
    df["month"] = df["arrival"].dt.month_name()
    return df


def preprocess_booking(df):
    pass


def preprocess_check_in(df):
    pass


def preprocess_check_out(df):

    df["arrival"] = pd.to_datetime(df["arrival"], format="%d/%m/%Y %I:%M:%S %p")
    df["departure"] = pd.to_datetime(df["departure"], format="%d/%m/%Y %I:%M:%S %p")

    df["room"] = df["room"].apply(lambda x: int(x.replace("Family", "")))

    df.drop(["company", "unnamed:_9", "balance_(sr1s)"], axis=1, inplace=True)

    # out_df = out_df.dropna() # delete last row

    df.rename(
        columns={
            "total_charges_(sr1s)": "total_charges",
            "user": "user_out",
        },
        inplace=True,
    )

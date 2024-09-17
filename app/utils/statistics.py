import pandas as pd


# general metrics
def number_of_reservations(df):
    """Number of rows"""
    return df.shape[0]


def number_of_active_reservations(df):
    """count of all active reservations"""
    return (df["status"] == "Active").sum()


def number_of_cancelled_reservations(df):
    """count of all active reservations"""
    return (df["status"] == "Cancelled").sum()


def number_of_guests(df):
    """count of all guest, this because there are ones who book multiple ones"""
    df = df[df["status"] == "Active"][["guest_name", "arrival"]]
    return df.groupby(["guest_name", "arrival"]).ngroups


# plot charts
def reservations_per_month(df):
    """Retrieve number of reservations per month based on its source
    Args:
        df is the dataframe
        col name of month to count values for each
    """

    counts = df["month"].value_counts()
    return counts


def revenue_per_month(df):
    """Retrieve the mony income each month"""
    active = df[df["status"] == "Active"][["month", "total"]]
    total_sum = active.groupby(["month"]).sum()
    return total_sum

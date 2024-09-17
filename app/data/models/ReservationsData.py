"""This class contains all pandas operations on columns to visualize them"""


class ReservationsData():
    """The operations on CLEANED version of Reservations Data."""

    columns = []

    def __init__(self, htask, booking, check_in, check_out):
        self.htask = htask
        self.booking = booking
        self.check_in = check_in
        self.check_out = check_out

        # ensure that received data contains all needed columns 
        if self.htask.columns not in ReservationsData.columns:
            raise Exception('Not all columns provided')


    def start_date(self):
        return self.htask['arrival'].min()
    
    def end_date(self):
        return self.htask['arrival'].max()
    
    def get_months(self):
        return self.htask['month'].unique()
    
    # based on reservation type
    def get_active(self):
        active = self.htask[self.htask['status'] == 'Active']
        return active
    
    def get_cancelled(self):
        cancelled = self.htask[self.htask['status'] == 'Cancelled']
        return cancelled
    
    def get_void(self):
        cancelled = self.htask[self.htask['status'] == 'Void']
        return cancelled
    
    def get_no_show(self):
        cancelled = self.htask[self.htask['status'] == 'No Show']
        return cancelled
    

    # based on reservations source
    def get_booking_reservations(self):
        return self.htask[self.htask['source'] == 'Booking']
    
    def get_walking_reservations(self):
        return self.htask[self.htask['source'] == 'walk-in']
    

    # get metrics
    def all_reservations_count(self):
        return self.htask.shape[0]
    
    def active_reservations_count(self):
        return self.get_active().shape[0]
    
    def cancelled_reservations_count(self):
        return self.get_cancelled().shape[0]


    # get money
    def get_revenue(self):
        active = self.get_active()
        return active['total'].sum()
    
    def get_booking_commission(self):
        """active = self.get_active()
        return active['commission'].sum()"""
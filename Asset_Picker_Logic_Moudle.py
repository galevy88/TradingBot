
from Data_Collecter_Moudle import DataCollecter


COEF_BUY = 1
COEF_SELL = -1
COEF_NEUTRAL = 0

class AssetPicker:
    def __init__(self):
        self.data_collecter = DataCollecter()
        self.current_rating_list = []

    def pick_asset(self):
        self.clear_rating_list_from_last_time()
        recommendation_list = self.data_collecter.generate_recommendation_list()

        for asset in recommendation_list:
            self.calculate_TOTAL_value(asset)
            self.current_rating_list.append(asset)
            self.current_rating_list = sorted(self.current_rating_list, key=lambda d: d['TOTAL'], reverse=True) 
        # print(f'The Asset The Chosen To Be The Best Is: {self.current_rating_list[0]["SYMBOL"]}')
        return self.current_rating_list[0]["SYMBOL"]


    def clear_rating_list_from_last_time(self):
        self.current_rating_list = []

    def calculate_TOTAL_value(self, asset):
        asset["TOTAL"] = (int(asset["BUY"]) * COEF_BUY) + (int(asset["SELL"]) * COEF_SELL) + (int(asset["NEUTRAL"]) * COEF_NEUTRAL)
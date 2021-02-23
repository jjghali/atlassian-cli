from datetime import datetime
import math

class StatsService:
    
    def __init__(self):
        pass

    def calculate_avgtime_between_releases(self, releases):        
        number_of_diffs = 0
        sum_of_diffs = 0

        for index, r in enumerate(releases):
            if index > 0:
                number_of_diffs += 1
                date1 = datetime.strptime(releases[index]["releaseDate"], "%Y-%m-%d")
                date2 = datetime.strptime(releases[index-1]["releaseDate"], "%Y-%m-%d")
                sum_of_diffs +=abs((date1 - date2).days)
        
        average = sum_of_diffs / number_of_diffs
        
        return average

        
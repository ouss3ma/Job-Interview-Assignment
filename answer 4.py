import datetime 

#create class DateRange
class DateRange:
  def __init__(self, start, end):
    self.start = start
    self.end = end
    
    
    
#create DateRange object
dr1 = DateRange(datetime.date(2013,5,31),datetime.date(2019,6,30))
dr2 = DateRange(datetime.date(2013,6,10),datetime.date(2013,9,30))
dr3 = DateRange(datetime.date(2013,9,30),datetime.date(2015,9,30))

#list that contains the DateRanges
list_range = [dr1, dr2, dr3]

#fonction to calculate the difference between two dates in days
def diff_dates(date1, date2):
    return abs(date2-date1).days



#function to merge the DateRanges
def merge_ranges (l):
    new_range = []
    diff = []
    
    #get the differences for each range between the start/end 
    #and the date '0001/01/01'
    #it is easier to work with number than with dates
    diff = [[diff_dates(d_range.start, datetime.date(1,1,1)),
             diff_dates(d_range.end, datetime.date(1,1,1)) ]
             for d_range  in l]
    
    #merge the ranges which intersect
    for begin,end in sorted(diff):
        if new_range and new_range[-1][1] >= begin - 1:
            new_range[-1][1] = max(new_range[-1][1], end)
        else:
            new_range.append([begin, end])
			
    #converts the number of days to dates
    output = [[(datetime.date(1,1,1) + datetime.timedelta(days=x)).isoformat() 
               for x in group] for group in new_range]
    return output




print(merge_ranges(list_range))


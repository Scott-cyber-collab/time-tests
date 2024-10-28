from times import time_range, compute_overlap_time

def test_given_input(): 
    #Test overlaps for two given time ranges
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]

    assert result == expected

def test_do_not_overlap(): 
    #Test do not overlap for time range
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-13 10:00:00", "2010-01-13 12:00:00")
    result = compute_overlap_time(large, short) 
    expected = []
    assert result == expected

def contain_several_intervals():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 3, 60)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 12:30:00", 3, 60)
    result = compute_overlap_time(large, short)
    print("Result:", result)  # Print for debugging
    
    expected = [
        ("2010-01-12 10:30:00", "2010-01-12 10:39:20"),
        ("2010-01-12 10:40:20", "2010-01-12 11:09:20"),
        ("2010-01-12 11:10:20", "2010-01-12 11:19:40"),
        ("2010-01-12 11:20:40", "2010-01-12 11:49:40"),
        ("2010-01-12 11:50:40", "2010-01-12 12:00:00")
    ]
    assert result == expected, f"Expected {expected} but got {result}"



def end_start_same_time(): 
    #Test for the same ending and starting time 
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:00:00", "2010-01-12 14:00:00")
    result = compute_overlap_time(large, short)
    expected = [("2010-01-12 12:00:00", "2010-01-12 12:00:00")]
    assert result == expected

test_given_input()
test_do_not_overlap()
contain_several_intervals()
end_start_same_time()

"""
Tools module with utility functions for mathematical operations.
"""


def sum_values(values):
    """
    Sum all values in a list.
    
    Args:
        values: A list of numbers to sum.
        
    Returns:
        The sum of all values in the list.
    """
    return sum(values)


def average_values(values):
    """
    Calculate the average of all values in a list.
    
    Args:
        values: A list of numbers to average.
        
    Returns:
        The average of all values in the list.
        
    Raises:
        ValueError: If the list is empty.
    """
    if not values:
        raise ValueError("Cannot calculate average of an empty list")
    return sum(values) / len(values)


if __name__ == "__main__":
    # Test sum_values function
    print("Testing sum_values()...")
    test_values_1 = [1, 2, 3, 4, 5]
    result_sum_1 = sum_values(test_values_1)
    assert result_sum_1 == 15, f"Expected 15, got {result_sum_1}"
    print(f"✓ sum_values({test_values_1}) = {result_sum_1}")
    
    test_values_2 = [10, 20, 30]
    result_sum_2 = sum_values(test_values_2)
    assert result_sum_2 == 60, f"Expected 60, got {result_sum_2}"
    print(f"✓ sum_values({test_values_2}) = {result_sum_2}")
    
    # Test average_values function
    print("\nTesting average_values()...")
    test_values_3 = [2, 4, 6, 8]
    result_avg_1 = average_values(test_values_3)
    assert result_avg_1 == 5.0, f"Expected 5.0, got {result_avg_1}"
    print(f"✓ average_values({test_values_3}) = {result_avg_1}")
    
    test_values_4 = [10, 20, 30]
    result_avg_2 = average_values(test_values_4)
    assert result_avg_2 == 20.0, f"Expected 20.0, got {result_avg_2}"
    print(f"✓ average_values({test_values_4}) = {result_avg_2}")
    
    print("\n✓ All tests passed!")

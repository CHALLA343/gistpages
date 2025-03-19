def main():
    # Read number of test cases
    N = int(input())
    
    # Helper function to process each test case recursively
    def process_case(X):
        # Read the integers of this test case
        nums = list(map(int, input().split()))
        
        # Recursive function to calculate the sum of squares excluding negatives
        def sum_of_squares(index, current_sum):
            if index == len(nums):
                return current_sum
            current_num = nums[index]
            if current_num >= 0:
                current_sum += current_num ** 2
            return sum_of_squares(index + 1, current_sum)
        
        # Calculate the sum of squares for this case
        result = sum_of_squares(0, 0)
        print(result)

    # Process all test cases
    def process_all_cases(case_count):
        if case_count == 0:
            return
        X = int(input())  # Read the number of integers in this test case
        process_case(X)
        process_all_cases(case_count - 1)

    process_all_cases(N)

if __name__ == "__main__":
    main()

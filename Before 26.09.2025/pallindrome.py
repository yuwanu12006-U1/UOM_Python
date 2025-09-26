def check_for_palindrome(input_string):
    # Base Case
    if len(input_string) <= 1:
        return True  # It is a palindrome

    # Recursive Case
    if input_string[0] == input_string[-1]:
        # Strip off the first and last letters and test the new string
        new_string = input_string[1:-1]
        return check_for_palindrome(new_string)
    else:
        return False  # It is definitely not a palindrome

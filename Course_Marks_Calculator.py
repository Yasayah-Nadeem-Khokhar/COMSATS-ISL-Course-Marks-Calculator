
"""
COMSAT-Isl-Course-Marks-Calculator.py

This script calculates the marks required in the final exam to pass a course 
based on the obtained marks in quizzes, assignments, and mid-term exams. 
It supports courses with different credit hour structures, including both 
class and lab components (2,1) and courses without a lab component (3,0).

Functions:
- get_percentage(obtained, total): Calculates the percentage of obtained marks.
- get_contribution(percentage, weight): Calculates the contribution of a component based on its percentage and weight.
- get_float_input(prompt): Prompts the user to enter a float value, ensuring valid input.
- calculate_marks(): Calculates the current marks and required final exam marks for a course.
- main(): Main function to repeatedly calculate marks for multiple courses if needed.

Usage:
- Run the script and follow the prompts to enter your course marks.
- The script will output the required marks to pass the course.

"""

# CourseMarksCalculator.py

# Function to calculate percentage
def get_percentage(obtained, total):
    return (obtained / total) * 100

# Function to calculate contribution based on percentage and weight
def get_contribution(percentage, weight):
    return (percentage * weight) / 100

# Function to get a valid float input from the user
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Function to calculate marks for a course
def calculate_marks():
    # Get credit hours input from user
    credit_hours = input("\n\nEnter the credit hours of the course (e.g., 3,0 or 2,1): ").strip()
    
    # Branching based on credit hours
    if credit_hours == "2,1":
        # Class Component
        print("\nClass Component:")
        total_class_quiz_marks = get_float_input("Enter total class quiz marks: ")
        obtained_class_quiz_marks = get_float_input("Enter obtained class quiz marks: ")
        total_class_assignment_marks = get_float_input("Enter total class assignment marks: ")
        obtained_class_assignment_marks = get_float_input("Enter obtained class assignment marks: ")
        total_class_mid_marks = get_float_input("Enter total class mid-term marks: ")
        obtained_class_mid_marks = get_float_input("Enter obtained class mid-term marks: ")
        
        # Calculate percentages and contributions for class component
        class_assignment_percentage = get_percentage(obtained_class_assignment_marks, total_class_assignment_marks)
        class_quiz_percentage = get_percentage(obtained_class_quiz_marks, total_class_quiz_marks)
        class_mid_percentage = get_percentage(obtained_class_mid_marks, total_class_mid_marks)
        
        class_assignment_contribution = get_contribution(class_assignment_percentage, 10)
        class_quiz_contribution = get_contribution(class_quiz_percentage, 15)
        class_mid_contribution = get_contribution(class_mid_percentage, 25)
        
        # Calculate current marks and required marks for final exam in class component
        class_current_marks = class_assignment_contribution + class_quiz_contribution + class_mid_contribution
        required_class_final_marks = 50 - class_current_marks
        
        # Output result for class component
        if required_class_final_marks > 0:
            class_final_exam_percentage_needed = (required_class_final_marks / 50) * 100
            print(f"\nYou need to score {required_class_final_marks:.2f} out of 50 in the final exam for the class component.")
            print(f"This is {class_final_exam_percentage_needed:.2f}% of the final exam.")
        else:
            print("\nCongratulations! You have already passed the class component.")
        
        # Lab Component
        print("\nLab Component:")
        total_lab_quiz_marks = get_float_input("Enter total lab quiz marks: ")
        obtained_lab_quiz_marks = get_float_input("Enter obtained lab quiz marks: ")
        total_lab_assignment_marks = get_float_input("Enter total lab assignment marks: ")
        obtained_lab_assignment_marks = get_float_input("Enter obtained lab assignment marks: ")
        total_lab_mid_marks = get_float_input("Enter total lab mid-term marks: ")
        obtained_lab_mid_marks = get_float_input("Enter obtained lab mid-term marks: ")
        
        # Calculate percentages and contributions for lab component
        lab_assignment_percentage = get_percentage(obtained_lab_assignment_marks, total_lab_assignment_marks)
        lab_quiz_percentage = get_percentage(obtained_lab_quiz_marks, total_lab_quiz_marks)
        lab_mid_percentage = get_percentage(obtained_lab_mid_marks, total_lab_mid_marks)
        
        lab_assignment_contribution = get_contribution(lab_assignment_percentage, 10)
        lab_quiz_contribution = get_contribution(lab_quiz_percentage, 15)
        lab_mid_contribution = get_contribution(lab_mid_percentage, 25)
        
        # Calculate current marks and required marks for final exam in lab component
        lab_current_marks = lab_assignment_contribution + lab_quiz_contribution + lab_mid_contribution
        required_lab_final_marks = 50 - lab_current_marks
        
        # Output result for lab component
        if required_lab_final_marks > 0:
            lab_final_exam_percentage_needed = (required_lab_final_marks / 50) * 100
            print(f"\nYou need to score {required_lab_final_marks:.2f} out of 50 in the final exam for the lab component.")
            print(f"This is {lab_final_exam_percentage_needed:.2f}% of the final exam.")
        else:
            print("\nCongratulations! You have already passed the lab component.")
            
    else:
        # Course without lab component
        total_quiz_marks = get_float_input("Enter total quiz marks: ")
        obtained_quiz_marks = get_float_input("Enter obtained quiz marks: ")
        total_assignment_marks = get_float_input("Enter total assignment marks: ")
        obtained_assignment_marks = get_float_input("Enter obtained assignment marks: ")
        total_mid_marks = get_float_input("Enter total mid-term marks: ")
        obtained_mid_marks = get_float_input("Enter obtained mid-term marks: ")
        
        # Calculate percentages and contributions for course without lab component
        assignment_percentage = get_percentage(obtained_assignment_marks, total_assignment_marks)
        quiz_percentage = get_percentage(obtained_quiz_marks, total_quiz_marks)
        mid_percentage = get_percentage(obtained_mid_marks, total_mid_marks)
        
        assignment_contribution = get_contribution(assignment_percentage, 10)
        quiz_contribution = get_contribution(quiz_percentage, 15)
        mid_contribution = get_contribution(mid_percentage, 25)
        
        # Calculate current marks and required marks for final exam
        current_marks = assignment_contribution + quiz_contribution + mid_contribution
        required_final_marks = 50 - current_marks
        
        # Output result for course without lab component
        if required_final_marks > 0:
            final_exam_percentage_needed = (required_final_marks / 50) * 100
            print(f"\nYou need to score {required_final_marks:.2f} out of 50 in the final exam.")
            print(f"This is {final_exam_percentage_needed:.2f}% of the final exam.")
        else:
            print("\nCongratulations! You have already passed the course.")

# Main function to run the program
def main():
    while True:
        # Calculate marks for a course
        calculate_marks()
        # Check if user wants to check more courses
        check_more = input("\nDo you want to check more? (yes/no): ").strip().lower()
        if check_more != 'yes':
            print("\nGoodbye!\n")
            break

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()

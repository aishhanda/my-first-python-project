# Function to determine the grade based on percentage
def my_grade(percentage):
    # If percentage is 90 or greater, return 'A'
    if percentage >= 90:
        return "A"
    # If percentage is between 75 (inclusive) and 90 (exclusive), return 'B'
    elif 75 <= percentage < 90:
        return "B"
    # If percentage is between 50 (inclusive) and 75 (exclusive), return 'C'
    elif 50 <= percentage < 75:
        return "C"
    # If percentage is below 50, return 'F'
    else:
        return "F"
def my_tag(percentage) :
      if my_grade(percentage) == "A" :
         return("\"TopPerformer \"")
      if my_grade(percentage) == "B" :
         return("\"ReliablePerformer \"")
      if my_grade(percentage) == "C" :
         return("\"AveragePerformer\" ")
      if my_grade(percentage) == "F":
         return("\"Underperformer \"")

# Input: Asking user for their name and marks in various subjects
name = input("What's your name? ").strip().title()  # Name input and formatting
physics = float(input("Physics Marks: "))  # Physics marks input
chemistry = float(input("Chemistry Marks: "))  # Chemistry marks input
mathematics = float(input("Mathematics Marks: "))  # Mathematics marks input
english = float(input("English Marks: "))  # English marks input

# Calculate the average percentage
percentage = (physics + chemistry + mathematics + english) / 4

# Output: Display the result with formatted grade and percentage
print(f"My name is {name}. I have completed my 12th with {percentage:.2f}% percentage. I have received grade {my_grade(percentage)}.Therefore i received {my_tag(percentage)}tag.")

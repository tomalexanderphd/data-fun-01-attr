import statistics

# Variables
company_name = "Alexander Analytics"
count_active_projects = 10
has_international_presence = True
average_client_satisfaction = 9.8
services_offered = ["Data Analysis", "Machine Learning Consulting", "Business Intelligence Solutions"]
satisfaction_scores = [9.7, 9.9, 9.7, 9.9, 9.8]

# f-strings
active_projects_string = f"Active Projects: {count_active_projects}"
international_presence_string = f"International Presence: {has_international_presence}"
client_satisfaction_string = f"Average Client Satisfaction: {average_client_satisfaction}"
services_offered_string = f"Services Offered: {', '.join(services_offered)}"

# Stats
smallest = min(satisfaction_scores)
largest = max(satisfaction_scores)
total = sum(satisfaction_scores)
count = len(satisfaction_scores)
mean = statistics.mean(satisfaction_scores)
mode = statistics.mode(satisfaction_scores)
median = statistics.median(satisfaction_scores)
standard_deviation = statistics.stdev(satisfaction_scores)

stats_string = f"""
Descriptive Statistics for Our Satisfaction Scores:
  Smallest: {smallest}
  Largest: {largest}
  Total: {total}
  Count: {count}
  Mean: {mean}
  Mode: {mode}
  Median: {median}
  Standard Deviation: {standard_deviation}
"""

# Define main function
def main():
    ''' Display all output'''
    print(company_name)
    print(active_projects_string)
    print(international_presence_string)
    print(client_satisfaction_string)
    print(services_offered_string)
    print(stats_string)

    # If all of the above works, then the byline should work too:
    byline = f"{company_name}\n{active_projects_string}\n{international_presence_string}\n{client_satisfaction_string}\n{services_offered_string}\n{stats_string}"
    print(byline)

if __name__ == "__main__":
    main()


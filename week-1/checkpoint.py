"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum.
"""

age = int(input("Please enter your age: "))

max_bpm = 220 - age
upper_bpm = max_bpm * .85
lower_bpm = max_bpm * .65

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {lower_bpm:.0f} and {upper_bpm:.0f} beats per minute.")

# Outline/Purpose:

- Having taught, and still teaching, myself programming for the past 6 months, I wanted to test my ability and solve an engaging puzzle at the same time.
- I have been watching TechwithTim and Clement Mihailescu since the start of my programming journey, I was incredibly excited when I saw the video where Clement conducts a mock interview for Tim and wanting to test myself, I figured I should try to solve the Google interview question.
- The question was to take in the schedules/calenders of two people (as a string in military time) along with their preference of when a meeting is to be held as well as the meeting length. The program would then output the possible times a meeting could be held.
- Below is the process or outline I wrote when I first thought about solving the question and true to the interview, I gave myself only an hour to solve it and viewed the video after I had finished!
- The question was challenging but very engaging and rewarding to solve.
- The sample input and output from the video are as below:
  ```python
  schedule1 = [['09:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
  constraint1 = ['09:00', '20:00']
  schedule2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
  constraint2 = ['10:00', '18:30']
  meeting_time = 30
  output = [['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]
  ```
- Here is the [link](https://www.youtube.com/watch?v=3Q_oYDQ2whs) for the video should you wish to solve it yourself.


# Process:

- First step is to find out what intervals are free for both the people:
    - Sort the combination of both their lists first by the starting time and then by the ending time.
    - Merge Intervals
        - Separate function that just takes both the times as strings in military time and returns the one which is greater and a separate function that checks if the difference between the two is enough for the given meeting time.
        - Get a list where the meeting can't happen - either one has a meeting.
- Then you have to find the bounds within which the meeting can be scheduled
    - Take both their bounds and find the smallest cartesian pair.
- Get a final list where meetings can take place:
    - Return all available intervals where the difference is greater than the meeting duration looking at the current end and next beginning of the merged list - UPDATE: check if the current end is greater than or equal to start of bounds and next beginning is smaller than or equal to end of bounds.
    - Check before the first meeting and see if there is free time for a meeting and after the end of the last meeting.

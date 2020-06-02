# Outline/Purpose:

- Having taught, and still teaching, myself programming for the past 6 months, I wanted to test my ability and solve an engaging puzzle at the same time.
- I have been watching TechwithTim and Clement Mihailescu since the start of my programming journey, I was incredibly excited when I saw the video where Clement conducts a mock interview for Tim and wanting to test myself, I figured I should try to solve the Google interview question.
- Below is the process or outline I wrote when I first thought about solving the question and true to the interview, I gave myself only an hour to solve it and viewed the video after I had finished!
- The question was challenging but very engaging and rewarding to solve.

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

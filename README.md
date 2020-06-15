# gradecheck
A program I made allowing someone to check how much an assignment will affect their grade, or just calculate it in general.

## NOTE: I made this for personal use and I'm just putting it on GitHub so I can take it between my mom and dad's houses. 

### Why did you waste your time making this?
Good question. I spend way more time doing the math of how my grade will be affected if I skip today's assignment than it takes to actually do the assignment. This program significantly cuts down on the time it takes to do the math. Also, it was good practice for Python and I hope to recreate this program in other languages as practice.

### How does the program work?
It's extremely simple. Just input the amount of assignments you have and then put in your score for each of them. If you want to calcuate the affect of skipping an assignment, just instead of the 15 already graded assignments, put 16.

### How does the output look?
```
shithead@localhost:~/gradecheck$ python gradecheck.py 
To calculate how an assignment will affect your grade add 1 to the input
Example: If you have 15 assignments not including the one you want to calculate enter 16
How many assignments do you have? : 2
Assignment 1 earned score (numerator) : 0
Assignment 1 attempted score (denominator) : 5
Assignment 2 earned score (numerator) : 50
Assignment 2 attempted score (denominator) : 50
90.91%
A+ = 97-100%
A = 93-96%
A- = 90-92%
B+ = 87-89%
B = 83-86%
B- = 80-82%
C+ = 77-79%
C = 73-76%
C- = 70-72%
D+ = 67-69%
D = 63-66%
D- = 60-62%
F = Below 60%
```

# Problem
Students that use UBC’s canvas and other assignment tracking applications such as PrairieLearn and WebWork find that it is difficult to maintain an up-to-date list of upcoming assignments. While canvas has a To-Do list implemented, instructors do not always add their assignments to canvas as assignments, and may opt to use other features such as modules or announcements, or altogether different systems such as PrairieLearn or WebWork. As such, it is hard for students to have a single location for all of the assignments they must complete. To compound the issue, choosing to use external To-Do lists or task managers is time consuming as students must manually add each assignment to the list, including any additional details they need and the due date.

# Solution
The application will allow you to add your account from different homework websites (such as canvas, prairielearn, or webwork). Then, it will compile a list of all your assignments sorted by closest due date to furthest due date. It will list the course name, the assignment name, and the assignment due date in this format:
[Course name] - [Assignment name] - [Due date]

In the list of assignments, the user can pin assignments or mark them as completed. When a user marks an assignment as completed, it gets moved to a different list called Completed assignments which can be viewed on a different tab. Pinned assignments always be above non-pinned assignments in the main list. Within the pinned assignments themselves, they will also be sorted from closest due date to furthest due date. This feature’s purpose is to allow users to put important or time-consuming assignments at the top, making it the first thing they see, so they are always reminded. If multiple assignments have the same due date, they will be sorted alphabetically. The user can use a refresh command or close and re-open the application to have the homework websites combed for the latest assignments. Each assignment will be assigned a number to users can perform an operation on them, which will be:

- refresh (combs websites for new assignments)
![refresh](spec%20images/refresh.png)

- pin <assignment numbers, comma separated> (pins assignments)
![pin assignments](spec%20images/pin.png)

- unpin <assignment numbers, comma separated> (unpins assignments)
![unpins assignments](spec%20images/unpin.png)

- finish <assignment numbers, comma separated> (marks assignments as finished)  
![finish](spec%20images/finish.png)

- unfinish <assignment numbers, comma separated> (marks finished assignments as unfinished so it will appear in the refresh list) 
![unfinish](spec%20images/unfinish.png)

- show pinned (shows all pinned assignments)
![show pinned](spec%20images/show%20pinned.png)

- show unpinned (shows all non-pinned assignments)
![show unpinned](spec%20images/show%20unpinned.png)

- show finished (shows all finished assignments)
![show finished](spec%20images/show%20finished.png)

- help (prints available commands)
![help](spec%20images/help.png)

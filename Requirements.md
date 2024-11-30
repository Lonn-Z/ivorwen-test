Sign-in Functionality

1. Use Canvas, Webwork and Prairielearn APIs to get the list of upcoming assignments  
2. Prompt user to create account or login  
3. Prompt user to give authorization for Canvas, Webwork and Prairielearn in command line (Y/N)  
4. Retrieve authorization token for read and write access to user’s Canvas account  
5. Retrieve authorization token for read and write access to user’s Webwork account  
6. Retrieve authorization token for read and write access to user’s Prairielearn account  
7. Store user tokens

Sync Functionality

1. Refresh \-new: Keeps user assigned pins and tags intact, loads in newly set assignments now visible on canvas

Database/Storage

1. Store data in Microsoft Azure server using SQL  
2. Store user email, username, password (encrypted)  
3. Store user tokens (encrypted)  
4. Store tasks  
5. Store incomplete Canvas tasks  
6. Store incomplete Webwork tasks  
7. Store incomplete Prairielearn tasks  
8. Store custom user created tasks

Display Functionality

1. Display due dates in format \<Month Day hh:mm \<PM/AM\> where hh:mm is a 12-hour clock.  
2. Display tasks in format “\<Course Code\> \- \<Assignment Name\> \- Due \<Due date\>  
3. Display pinned tasks in order sorted by due date, earliest due date first.  
4. Display pinned task in format “PINNED: \<task\>”  
5. Display unpinned tasks in order sorted by due date, earliest due date first.  
6. Display pinned tasks followed by unpinned tasks.

All database fields for each assignment:  
Assignment ID  
The assignment ID is determined by the order that each assignment was created. So the first assignment will have ID 1, the 2nd will have ID 2, etc.

Due date  
This is the due date on canvas / prairielearn / webwork.

Submit by date  
This is the “available until” date on canvas (or the normal due date on prairielearn / webwork).

Pinned  
Shows whether assignment is pinned or not (determined manually by user).

Completed  
Shows whether assignment is completed or uncompleted. (Should this be done automatically? It would be a nice feature, but it would add more complexity)

Name  
Name of the assignment. (ex. WW5)

Source  
The website the assignment came from (Canvas, Webwork, Prairielearn)

The program will allow users to pin and unpin assignments

Core Functionality

1. Sort user tasks by date  
2. Filter completed assignments out  
3. Filter overdue assignments out  
4. Display sorted, filtered tasks  
5. Update tasks as they are assigned and completed  
6. Assign assignment tags (“completed”, “ongoing”, etc.)  
7. Pin tasks so they always appear first

User Interface

1. Use a webpage to facilitate user inputs  
2. Display user assignment information in an organized and visually appealing manner on the webpage.

Webpage functions:

1. Correctly implement each of the following buttons:  
   1. refresh (syncs with linked platforms—such as Canvas—for new assignments)  
   2. pin (pins assignment)  
   3. unpin (unpins assignments)  
   4. finish (marks assignments as finished)  
   5. unfinish \<assignment numbers, comma separated\> (marks finished assignments as unfinished so it will appear in the refresh list)  
   6. show pinned (shows all pinned assignments)  
   7. show unpinned (shows all non-pinned assignments)  
   8. show finished (shows all finished assignments)  
   9. Login


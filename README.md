Features
    1. Adds tasks: Users can add tasks to a list.
    2. View Tasks: Displays a list of all added tasks.
    3. Delete Tasks: Removes a task by selecting its number.

The program is also user friendly with error handling

Upon running the script, the user will see a menu:

    1. Add Task
    2. View Task
    3. Delete Task 
    4. Quit Task

BRIEF EXPLANATION OF EACH FUNCTION

ADD TASK

to add a task you enter 1 and then type a desription of the task 

VIEW TASK   

to view the tasks you enter 2 and added tasks will be displayed

DELETE TASK

to delete a task enter 3 then select the index of the task you want deleted 

                0                   1                   2
Example : ['Eat Breakfast', 'Brush your teeth', 'Go for a run']

the index always starts at 0 so if you want to delete 'Eat Breakfast' you just enter 0

QUIT TASK

when you are done you enter 4

ERROR HANDLING 

So simple error handling has been added such as:
    1. If you dont enter anything when you try to add a task you will be informed that you cant add an empty task 
    2. If you try to delete a task index that doesnt exist you will get an error and told to try again
    3. Will display a warning for invalid menu selections
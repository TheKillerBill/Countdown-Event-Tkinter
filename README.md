# Countdown-Event
A program to display the countdown of a certain event.

The program has 7 inputs which are the event name, the year, the month, the day, the hour, the minute and the second.

   ![Screenshot 2021-10-06 191825](https://user-images.githubusercontent.com/19519174/136260546-3f930324-fb20-4add-97e7-32525c22b966.jpg)

The program checks if the date entered is in the past, and if so, an error will pop up prompting you to re-enter the date.

![Screenshot 2021-10-06 191947](https://user-images.githubusercontent.com/19519174/136260707-d8a1b9a1-0280-4e61-b32d-99191816f69d.jpg)

It also checks the info entered and will prompt an error if the info isn't in a correct form. For example, month can't be above 12, day can't be above 31, hour can't be above 23, minute can't be above 59 and second can't be above 59.

![Screenshot 2021-10-06 192059](https://user-images.githubusercontent.com/19519174/136260859-34dd95f2-bc88-4683-9d6b-f67a300184b6.jpg)

The event can be saved for the next time the program is launched, if the user chooses to do so. The info is saved inside an ini file in the same directory as the program.
When entering start after entering the info, you'll be presented with a countdown for the date you entered.

![Screenshot 2021-10-06 192337](https://user-images.githubusercontent.com/19519174/136261202-32804f7a-de83-424b-8637-3c392ceaf19c.jpg)

There's the button to save the event for the next time you launch the program, and a reset button that will bring you back to entering the info again.
When the countdown reaches to 0, a notification sound effect plays and you get directed to this window:

![Screenshot 2021-10-06 192633](https://user-images.githubusercontent.com/19519174/136261648-20470e18-b9e7-4beb-a3c5-417b37f2bbf4.jpg)

Clicking the back button naturally directs you back to entering another date.

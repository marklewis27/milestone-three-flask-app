# Used car database
This is a database that can be used by a car dealership to keep a track of the used vechiles they have in stock. It is simple to use and easy to make changes to a car details, delete a car and view the entire stock of the dealership.

## Ux
This site has been designed to be as easy to use as it is functional. I wanted the focus to be on ease of use, a site that anyone would feel comfortable using within a matter of minutes. 
Using the materiliaze styles i have adopted some simple to use buttons that are clear and interactive with hoover classes on them. For the button that deletes a car changing this to red to indicate that it would perform an unchangable action to the database. 
Along with these style choices i added in a few small but relevent images to the buttons to highlight there actions some more. Also i added in the small down arrow where the car make and model is displayed to give further information to the user that this has a dropdown element to it to view the rest of the information on that car.
I did draw up a couple of simple wireframes before starting the project which can be found in the wireframes file in the github repsoitory for this project, i have adapated some of the ideas from those first drawings as i got in to the project and realised that there were better ways to display the information on the page to the user.

## Features
Some of the features of the site.
1. Homepage at the top of the navigation, a simple clickable word that always takes the user the sites homepage.
1. New car button, A clear and visible way to add a new car to the database right at the top centre of the page.
1. Expanding dropdown of the cars details, gives a nice animated user friendly way to display the information without it all being on the screen at the same time for all of the cars.
1. Update details button styled with the pen to indicate that this is where you edit the details for the car the user is looking at.
1. Delete button again for each car having there own button, highlighted in red with a bin image to show clearly that this will delete the car from the site.
1. New and edit car forms use some of the materilize styling to make the form elements more pleasing to use with the green highligt as the user clicks on them.
1. consistant styling, across the pages keeping the colours the same and keep elements like buttons in the same place to make the sites different pages all easy to use and easy on the eye.

### Features left to implement
A admin login for deleting the car from the database with maybe an added popup giving the option to continue and delete or cancel the delete action.

## Technologies uesd
The main technologies used in the project listed below
1. The main framwork for the project is the Flask framework. https://flask.palletsprojects.com/en/1.1.x/
1. The python framework is built on the python language. https://www.python.org/downloads/
1. The styling on the page used the materilize styles. https://materializecss.com/
1. In this project materilize needed some javascript and JQuery to run its styling. https://www.javascript.com/  https://jquery.com/
1. The basics of this site use the HTML5 programming language. 
1. Along with the materilize built in styles i have made a few changes of my own using the CSS language for styles.

## Testing
During the start of the built i got the basic file structure in place with the basic dependecies in place as well and run these to make sure that the app was generating me a weblink in the console that i could click on and it take me to the site. 
Once that basic step was in place i could move on, when connecting to the mongo DB database i made a simple entry in to the database and set up the user etc as needed. Then i liked the database in to my app.py file and made a simple template to check that i could reach the database and show the data that was in there. 
Adding a new car, when making this part of the site i got the form elements in place and added in the information for a new car, submitted it and the went on to mongo DB to check that it was in the database. Which it was. However at this point i was only getting one car returning to my screen as i hadnt used the correct write up in my app.py to get all of the data but only one, once i changed this i was getting the data that i wanted back from the data base and displaying to the home screen.
Updating the car details, i made the form for the site and it was displaying as i wanted it to, however, it wasnt entering in the details that were already there for that car in the data base as i wanted them to. Once i got this to return the details for most of the items i had problems with the dropdown options showing the other options still. I was either getting no dropdown or a dropdown with no information in it. An error i was making with the else statement was causing me these problems and once solved i was getting back the data i wanted.
Delete car, This one was pretty easy to test. I made a few cars using the new car form, checked that they had gone over to the database which they had. I then went back to the site to delete them using the button, once clicked they went from the screen, i then went back to the mongo DB site to check that they had been removed, which that had so that was working well.
Mobile testing. The form elements i was using i was making sure were responsive to mobile, along with the buttons i made sure that when they were in place on the desktop view that they still rendered and worked when using a mobile device. 
I did have some issuses with the Navbar, to begin with i had the option to add the new car over to the right but when i went in to mobile view it would not be there anymore. A change to the layout to keep this in the center made it clearer for the user i felt and also made it work perfectly on mobile. All the other text on the screen i kept in this centre allignement to keep the layout simple and clean across all pages and on mobile responsive to the smaller size screen giving a good user experience still.
During the course of this project i have made sure to keep checking along the way that any changes i make work, and are bug free. using the dev tools to check for errors on the page and the app log in VS code for any problems that may occur.

### Deployment 
I have been backing up the work to github after every session i would sit at my computer working on this project. When it came to the deployment i set up a Heroku account and ran in to a few problems.
1. I didnt have a procfile setup in my file structure so i had to add this in.
1. I needed to tell heroku which version of python i was using as it was picking it up by default.
1. After these issues were fixed i was still getting errors and this was eventually solved by adding in th code at the bottom of the app.py file and specifying in heroku the IP port and value. Once i'd done these things it was working again.

### Credits
1. The startup of the project i followed the flask in vs code tutorial to get the basic file structure and dependancies installed for this project
1. For the delete functionaly i refered back to the course for how to get this setup.
1. The update displaying the data that was already there for a car i used the course as a reference to get me started and from there made my own for other options and added a lot more to it.

### Media
The only images and fonts used were from materilize

### Acknowledgements
Autotrader was the insiration for this site build

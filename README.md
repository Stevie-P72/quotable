# Quotable

A social website where users share quotes that they enjoyed, and can discuss them with other users in comments.

## UX
I have provided a few examples of what types of perople may use this website, and what they may use it for.

* User 1: A philosophy student who has just read something interesting from their favourite Greek Philosopher, and wants to share it with others.
* User 2: A film critic who wants to see others take on a famous movie quote before publishing their own take.
* User 3: Someone who reads poetry, and finds something thought provoking, so they post that quote, looking to find out what it means to different people.

For forms that would be difficult to layout on a mobile, I have added seperate pages for them, instead of integrating them into the page.

## Features
* The ability to create, read, update and delete posts.
* Comments on each post, so that you can discuss them with other users.
* A search function, to see what a particular user has uploaded, or find multiple quotes credited to one person.


## Features Left to Implement
The ability to log in, so that your user is a constant, along with stopping anyone else from deleting posts or comments you have made.

## Technologies Used
* HTML
    * https://html.spec.whatwg.org/multipage/
    * The basis for the content of the website
* CSS
    * https://www.w3.org/Style/CSS/
    * Adding custom style and design to the content on the website
* Jquery
    * https://jquery.com/
    * Used to initialize some of the elements taken from Materialize, and to make the page more responsive to user interaction
* Materialize
    * https://materializecss.com/
    * The front-end framework used to style the majority of the website, along with the interactive functionality
* Python
    * https://www.python.org/
    * The back end code, providing the functions to create, search, update and delete posts on the website, along with communicating the database in which these posts are stored.
* MongoDB
    * https://www.mongodb.com/
    * The database in which all data for this website is stored

## Deployment
This project was deployed to Heroku.
In order to do this, the following steps were taken:
* A Procfile was created, to inform Heroku what commands are required to run the website.
* A Requirements.txt file, which is used to install all of the dependencies this website has.
* Environment variables for IP, Port and the Mongo URL were set, so to give access to the Mongo Database.

## Credits
### Sample Quotes
All quotes are credited to the films, books or songs they are quoted from, and are the responsibility of the user to credit them accordingly.

### Media
The background image for the site is obtained from: https://www.wallpaperflare.com/
This image was licensed to use, share and modify.
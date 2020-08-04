<div><img src="assets/img/logo/logo2.jpg" alt="logo">
<h1>Audio Visualizer</h1>
</div>

## Stream Three Project: Database - Code Institute
### Note-this
[Note-this](https://note-this.herokuapp.com/) is a note-taking app. It began as an app for taking notes on wikipedia pages, working through a bookmarklet that the user would click while on a wikipedia page they wished to take notes on. They would then be directed to a page on the note-taking app which would allow them to read the wikipedia page through an iFrame while taking notes. This idea was changed to a general note taking app to increase scope, users can take notes on anything and not just wikipedia articles. This would be useful for a much broader range of users. The app was designed and created primarily with student note-takers in mind.


## Table of contents

- [Stream Three Project: Database - Code Institute](#stream-three-project-database---code-institute)
  - [How it works](#how-it-works)
- [Table of contents](#table-of-contents)
- [Demo](#demo)
- [Gallery](#gallery)
- [UX](#ux)
  - [User Stories](#user-stories)
  - [Design choices](#design-choices)
  - [Wireframes](#wireframes)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
  - [How this project was deployed to Heroku](#how-this-project-was-deployed-to-Heroku)
  - [How to run this project locally](#how-to-run-this-project-locally)
- [Testing](#testing)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)

## Demo

A live demo can be found [here](https://note-this.herokuapp.com/).

## Gallery

# UX

## User Stories

Note-this was designed with the following target audiences in mind:
- Students
- Users who need to access notes across multiple devices

User goals are:

Note-this meets these user needs by:

The following user stories were used to develop on the features that the site should have.

As a user:
- I would like to create, edit, save, and delete notes.
- I would like to read and create my notes across a range of devices and platforms.
- I would like to search through my notes for notes that contain certain text.
- I would like to tag notes according to subject or category and view my notes according to their tag.
- I would like the layout to be easy to use and intuitive.

As a student taking notes during a lecture:
- I would like to tag the note with its corresponding subject so I can view all notes under this tag together.
- I would like to be able to access my notes later from either a desktop or mobile device.
- I would like to be able to format my notes to create headings, highlight passages, and other stylistic formatting options for readability.
- I would like to be able to input source code.

## Design

### Font
- [Lato](https://fonts.google.com/specimen/Lato) was chosen as the font as it is a humanist sans serif typeface designed to convey a minimal and modern feel.

### Icons
- The icons for reading, editing, and deleting a note were chosen for their universal meaning.
- They save valuable space, particularly on mobile devices.

### Colours

<p align="center">
  <img src="app/static/img/colourpalette.png" height="100" width="100%">
</p>

- A neutral color palette was chosen for the site to convey a serious tone and to limit distraction to the user from their task.
- The orange highlight color was chosen to draw the user's attention to any interactive buttons or links.
- The text is black on a pale background to improve readability. 

### Styling

- A collapsible accordion was chosen to display the notes on the homepage. This allows the user to see the title of the note and click to display or hide the body of the note to quickly check it's contents without changing page.
- A slide out side navigation menu is used to allow the user to be able to access all the menu items from any page without taking up extra space
- The custom note menu bar was styled to look the same as the tinyMCE menu bar to create a seamless transition between these elements on the page. 
- The tag and info buttons on the note page are collapsible components to save screen space.
- The note form was designed with rounded corners to give a more modern appearance.


### Wireframes

## Features

### Existing Features

### Features Left to Implement

- Ability to download the note as a .txt file
- Ability to customise the website color theme
- Pre-emptive search string completion
- Ability to share notes with other users and allow approval of multiple user editors per note

## Technologies Used

- Visual Studio Code
- HTML
- CSS
- Javascript
  - Used to initialize the tinymce editor (tinymce.js)
- jQuery
  - For DOM manipulation
- Bootstrap (v4.3.1)
  - For responsive styling
- Materialize
  - For the navbar and sidenav styling
  - [Material Icon font](https://material.io/resources/icons/?style=baseline) for the icons
- [Google fonts](https://fonts.google.com/)
- [Autoprefixer](https://autoprefixer.github.io/)
- [jShint](https://jshint.com/)

## Deployment

This project was developed using the code editor Visual Studio Code, committed to git and pushed to Heroku using the terminal.

This site is hosted using Heroku, deployed directly from the master branch. The deployed site will update automatically when new commits to the master branch are pushed to Heroku. In order for the site to deploy correctly on Heroku, the landing page must be named `index.html`.

### How this app was deployed to Heroku
1. Create a git repository
2. Create requirements.txt
3. Create a Procfile
4. Commit all changes to the git repository
5. Create a new Heroku app on the Heroku website
6. Use the ```heroku git:remote``` command to set the remote to the git repository
7. In the Settings page of the app in Heroku, set the config variables
8. Use ```git push heroku master``` to deploy the latest version of the commited code

### How to run this project locally

1. Install Git following [these instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
2. Open a terminal
3. Create a directory by entering `mkdir repo` into the terminal
4. Change the current working directory to the directory from the previous step by entering 'cd repo' into the terminal
5. Clone the repository to this directory by entering `git clone https://github.com/tesoph/notes.git`
6. Install Python3
7. Create a virtual environment by entering `python3 -m venv venv` into the terminal
8. Use the command `source venv/bin/activate` to activate the virtual environment
9. Install pip3 
10. Install all required packages with the command `pip -r requirements.txt`
11. Create a .flaskenv file and set the following config variables in it:
    - FLASK_APP=notes.py
    - MONGO_URI=*[uri link to your own mongodb database]*
    - MONGO_DBNAME=*[the name of your own mongodb database]*
12. Create two collections in your mongodb database named `notes` and `users`
13. Run the application with `Flask run`
14. To cut ties with this GitHub repository, navigate to the directory it is in and type `git remote rm origin` into the command line.

## Testing

Testing information can be found in separate [testing.md](testing.md) file

## Credits

### Code


### Media

- Logo from Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
- The icons labelling the toolbar buttons and the popovers in the settings menu are from [Material icons](https://material.io/resources/icons/?style=baseline).

### Acknowledgements

- This README was created following the format of and has taken inspiration from Code Institute student [AJGreaves's README](https://github.com/AJGreaves/picflip/blob/master/README.md).

- Thanks to my mentor Brian Macharia for support and advice.

**This is for educational use.**
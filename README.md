# Coastal Paws Rescue - Dog Adoption Website

Coastal Paws Rescue is a user-friendly pet adoption platform where users can effortlessly discover dogs that match their lifestyle and needs. With a simple and easy-to-follow adoption form, users can apply for their desired dog and conveniently track the status of their application. [here](https://coastal-paws-rescue-app-7981fd69df53.herokuapp.com/).


---

## Table of Contents

- [User Experience (UX)](#user-experience-design)
  - [Strategy Plane](#strategy-plane)
  - [Scope Plane](#scope-plane)
  - [Structure Plane](#structure-plane)
  - [Skeleton Plane](#skeleton-plane)
  - [Surface Plane](#surface-plane)
- [Features](#Features)
- [Technologies](#Technologies)
- [Testing](#Testing)
  - [Test Results & Bugs](#test-results--bugs)
- [Deployment](#Deployment)
- [Credits](#Credits)

---

## User Experience Design

### **Strategy Plane**

#### Site Goals

- To list dogs for adption with an online adoption form
- To make it easy to manage listings and adoption requests

## User stories

### Admin User Stories:

### Adding Dogs:
- As a admin, I want to add new dog listings to the adoption platform.

#### Managing Listings:
- As an admin, I want to be able to view and manage all dog listings.
- As an admin, I want the ability to edit details and images of any dog listing.

#### Adoption Requests:
- As an admin, I want to view all adoption requests submitted by users.
- As an admin, I want to approve or reject adoption requests.

### Member User Stories:

### Adoption Requests:
- As a member, I want to submit adoption requests for dogs I'm interested in.
- As a member, I want to to be able to see my adoption requests and status.

## Regular User Stories:

### Browsing Dogs:
- As a regular user, I want to view a list of all available dogs for adoption.
- As a regular user, I want to search and filter dogs based on different criteria.

### User Registration:
- As a regular user, I want to register for an account to access additional features.

### Viewing Profiles:
- As a regular user, I want to view profiles of dogs available for adoption.

---

### **Scope Plane**

**Features planned:**



### **Structure Plane**


### **Skeleton Plane**


#### Database Design

MongoDB Object format examples:

**Collection: dogs**

**Collection: adoptionRequests**

**Collection: users**


#### Security

Database connection details are set up in an [env.py](https://pypi.org/project/env.py/) for development, for
security reasons this is not uploaded to GitHub so that database and connection details are not visible to
users. In production these are stored in Heroku.

__Site Security__


---

### **Surface Plane**

#### Wireframes


**Wireframes / Site Design**



#### Design

##### Colour Scheme

!

##### Typography



##### Graphics / Imagery


---

## Features

Add Features here



---

### Future Features

Add Future Features e.g other types of pets / book a meet and greet session



---

## Technologies

### Languages

- [HTML](https://en.wikipedia.org/wiki/HTML5)
  - Used to build the main structure of the site
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
  - Used to style the website
- [Vanilla JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [JQuery](https://jquery.com/)
- [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>)
  - Used to build the core of the backend of the project as well as the running/viewing of the website
  - Python Modules Used:
    - blinker==1.6.3
    - click==8.1.7
    - dnspython==2.4.2
    - Flask==3.0.0
    - Flask-PyMongo==2.3.0
    - itsdangerous==2.1.2
    - pymongo==4.5.0
    - Werkzeug==3.0.0

### Tools

- [Git](https://git-scm.com/)
  - Used for version control via Code Anywhere by using the terminal to Git and Push to GitHub
- [GitHub](https://github.com/)
  - Used to store the project code
- [Code Anywhere](https://codeanywhere.com/)
  - Used to create, edit & preview the project's code
- [Heroku](https://dashboard.heroku.com/apps)
  - Used to deploy the live site
- [Materialize](https://materializecss.com/)
  - Used to help with the responsiveness of the site and add styling
- [Google Fonts](https://fonts.google.com/)
  - Used to select & import the fonts to the project
- [Font Awesome](https://fontawesome.com/)
  - Used to add icons to the site to help with UX and to add more character
- [Favicon.io](https://favicon.io/favicon-converter/)
  - Used to create and add the favicon to the browser tab
- [Google Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools)
  - Used to inspect page elements, debug issues with the site & test responsiveness on different mockup devices
---

## Testing

The whole site has been thoroughly tested as follows:

To be done

- Automated Validation / Testing
    - HTML Validation: [W3C Markup Validation](https://validator.w3.org/nu/)
    - CSS Validation: [W3C CSS Validation](https://jigsaw.w3.org/css-validator/)
    - JavaScript Linting: [JS Hint](https://jshint.com/)
    - Python Linting: [pep8ci](https://pep8ci.herokuapp.com/) & Code Anywhere's inbuilt Linting
    - Accessibility: [Wave WebAIM](https://wave.webaim.org/)
    - Performance: [Google Chrome's Dev Tools](https://developer.chrome.com/docs/devtools/)
- Feature Testing
    - Full feature testing on all pages
    - Testing of CRUD functionality
    - Checking consistency between database & app content
    - Site tested across different browsers
    - Site tested across different devices
- User Stories Testing
    - Full app testing for each user story


---

### Test Results & Bugs

The full test results and details of any bugs and their fixes can be found in the [TESTING document](TESTING.md)

---

## Deployment

### Project Creation
I used the [CI MongoDB Code Anywhere Full Template](https://github.com/Code-Institute-Org/ci-mongo-template) to create this project and used Code Anywhere as my IDE.

From the CI Mongo template above the steps to create this project were:
1. Click on 'Use this template' and select 'Create a new repository'
2. Enter your chosen repo name
3. Click 'Create Repository'
4. From the new GitHub repo copy the the page URL
5. Open Code Anywhere and navigate to the 'workspaces' page
6. Click on 'New Workspace'
7. Paste the GitHub repo URL in to the 'Repository URL' box
8. Click 'Create'


### Deployment to Heroku
I used Heroku to deploy this project.

To deploy to Heroku:
1. In Code Anywhere CLI from the main directory run `pip3 freeze > requirements.txt` to create/update a requirements.txt file containing project dependencies.
2. In Code Anywhere CLI from the main directory run `echo web: python app.py > Procfile` to create a Procfile. Check that the file contains the text 'web: python app.py' and delete any blank lines at the bottom.
3. Push the 2 new files to the GitHub repository
4. Login to Heroku, select 'Create New App', create a unique name for the app and select your nearest region. Click 'Create App'
5. Navigate to the Deploy tab on Heroku dashboard and select Github, search for your repository by name and click 'connect'.
6. Navigate to 'settings', click reveal config vars and input the the following:

| Key | Value |
| :---: | :---: |
| CLOUD_API_KEY | _Cloudinary API key_ |
| CLOUD_API_SECRET | _Cloudinary API secret_ |
| CLOUD_NAME | _Cloudinary Name_   |
| IP | 0.0.0.0 |
| PORT | 5000 |
| MONGO_DB | _Mongodb Database Name_ |
| MONGO_URI | mongodb+srv://<_USERNAME_>:<_PASSWORD_>@<_CLUSTER_>.tfci8tb.mongodb.net/<_DATABASE_>?retryWrites=true&w=majority |
| SECRET_KEY | _Secret Key From env.py required for 'Session' & 'Flash' functions of Flask_ |

7. Go back to the Deploy tab and click on 'Enable Automatic Deploys'
8. Click deploy branch
9. Once build is complete click on 'View' to launch the new app

### Local Development
__NB: This project will not run locally with database connections unless hte user sets up an env.py file configuring the above environment variables as these are not included in the GitHub files for security reasons.__

To Run Locally:
1. Navigate to the [GitHub Repository](https://github.com/Hanmb17/CI_MS3_CoastalPawsRescue)
2. Click on 'Code' & select 'Download Zip' to download the files locally and open with an IDE or Copy the URL from the top box
3. If copying the code open your development editor & in the terminal use the 'Git Clone' command followed by the above URL to create a clone of the project locally.

To Fork Project:
1. Navigate to the [GitHub Repository](https://github.com/Hanmb17/CI_MS3_CoastalPawsRescue)
2. Click on the 'Fork' button at the top right of the page
3. This will duplicate the project for you to work on


---

## Credits

### Code

Details of any projects or online sources that I have learned from or adapted in developing this website.


### Images & Text

-


### Graphics



### Acknowledgements



---

---

[Go to Top]()

---
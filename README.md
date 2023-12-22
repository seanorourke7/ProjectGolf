# Seans Golf Adventures

Seans Golf Adventures is a Blog about golf courses around Ireland. The idea is to post about your visit to a course and leave feedback. The models ask for specific information like the players handicap, tees played off and their score at the end of the round. The user as well as Admin can post to it but only Admin can approve posts to be published. It encourages interaction through inviting the user to comment and like other peoples posts and to even submit a post themselves.

The live link can be found here: 
[Live Site - Seans Golf Adventures](https://projectgolf-537a6c2d3f19.herokuapp.com/)

## CONTENTS

- [Seans Golf Adventures](#seans-golf-adventures)
  - [CONTENTS](#contents)
  - [User Experience (UX)](#user-experience-ux)
  - [Agile Planning](#agile-planning)
    - [User Stories](#user-stories)
  - [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Imagery](#imagery)
    - [Wireframes](#wireframes)
  - [Features](#features)
    - [General features on each page](#general-features-on-each-page)
    - [Future Implementations](#future-implementations)
    - [Accessibility](#accessibility)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Deployment](#deployment)
      - [How to Fork](#how-to-fork)
      - [How to Clone](#how-to-clone)
  - [Testing](#testing)
  - [Bugs](#bugs)
  - [Credits](#credits)
    - [Acknowledgments](#acknowledgments)

---

## User Experience (UX)

## Agile Planning

This project was developed using agile methodologies by delivering small features in incremental steps. 

All issues were prioritized under the labels, Must have, would like to have, and Bug. "Must have" stories were completed first, and then finally "would like to have". It was done this way to ensure that all core requirements were completed first to give the project a complete feel, with the nice to have features being added should there be capacity.

There are still some "would like to have" issues left that I would like to impliment in future. 

The Kanban board was created using github projects and can be located here and can be viewed to see more information on the project cards. 

[Kanban Board](https://github.com/users/seanorourke7/projects/8)


### User Stories

First time visitors will be greeted with a well layed out and interesting website. The most recent 3 blog posts will be visible on the home page and then a simple navigation tool allows further browsing. Each blog post will have a picture either uploaded by the author or by default.

The user will be able to view the detail of each post by clicking on the name of the course. they will be taken to a page with the full blog post where they will see the review itself as well as the gross score and stableford score and the handicap and tees played off.

Upon registering users will be able to like and comment on posts and even submit their own posts to the blog. 
All comments and blog posts will be approved by Admin.

After posting a blog post Users will be able to review, edit and delete the posts. 

## Design

### Colour Scheme

The colour scheme is based on the background image of a golf course with each blog post photo sitting over this image. If there isn't a picture uploaded with the post a default image of a golf course will be provided. 
The background is white and the text overlay is black giving simple but effective contrast. The Footer is the opposite with a dark background contrasting with light colored text. 


### Imagery

Images used are a selection of golf course images from pexels.com. If the post author doesn't include an image a default image of a golf course will show in it's place.

### Wireframes

I drew out a very simple wireframes with Uizard.


![homepage wireframe](static/media/images/mockupgolf.png)
![homepage wireframe](static/media/images/mockupgolf2.png)

## Features

This site contains a home page with bog posts paginated by 6 with easy to navigate controls to reach more posts. 
Users can register and log in to comment and like posts as well as submit their own posts. 

![Homepage destop](static/media/images/ScreenshotDesktop.png)

![Homepage mobile](static/media/images/Screenshothomemobile.png)



![Signup destop](static/media/images/Screenshotsignupdesktop.png)
![Signup mobile](static/media/images/Screenshotsignupmobile.png)

![Create post desktop](static/media/images/Screenshotcreatepostdesktop.png)
![Create post mobile](static/media/images/Screenshotcreatemobile.png)

### General features on each page

There is a header and footer that are used across the site using django block content. 
The user can navigate to the log in/logout/register page by clicking the burger icon on small screens or the login/logout/signup button on larger screens.
The site logo "Seans Golf Adventures" also links to the home page.  
Once logged in a user can create their own post by clicking on the Create Post button at the bottom of the home page. 
The link in the footer leads to the creaters github profile. 

### Future Implementations

I would like to add the ability to rate each course with stars. So each user can rate out of 5 stars their experience of each course. And GeoTag the courses so the users can see the courses on a map. 

### Accessibility

All images and links used have aria labels and lighthouse scores the site above 90%. 

![Lighthouse](static/media/images/lighthousegolf.png)

## Technologies Used

ElephantSQL - for the database.

Cloudinary - for image hosting. 

Github - To save and store the files for the website.

Codeanywhere - to write the code.

Google Fonts - To import the fonts used on the website.

Crispy Alerts - for the alert boxes.

Google Dev Tools - To troubleshoot and test features, solve issues with responsiveness and styling.

Mockflow for the wireframe.


### Languages Used

Python, Django, HTML, CSS & JavaScript.

### Deployment

Deployment

Github Pages was used to deploy the live website. The instructions to achieve this are below:

Log in (or sign up) to Github.
Find the repository for this project, seanorourke7/ProjectGolf.
Click on the Settings link.
Click on the Pages link in the left hand side navigation bar.
In the Source section, choose main from the drop down select branch menu. Select Root from the drop down select folder menu.
Click Save. Your live Github Pages site is now deployed at the URL shown.

#### How to Fork

How to Fork
To fork the RPSLS repository:

Log in (or sign up) to Github.
Go to the repository for this project, seanorourke7/ProjectGolf.
Click the Fork button in the top right corner.

#### How to Clone

How to Clone
To clone the ProjectGolf repository:

Log in (or sign up) to GitHub.
Go to the repository for this project, seanorourke7/ProjectGolf.
Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

## Testing

Testing was ongoing throughout the entire build using dev tools and running tests in the terminal window.

More detailed information is included in the TESTING.md file. 

## Bugs

There was a bug in that the slug of each post was the id of the post which is unique to each post. This allows multiple posts/reviews of the same golf course. However when the post is submitted for approval the slug is set to none in the Admin page and when it's approved the id needs to be manually entered into the slug field. This should be automatic. I changed this to a random number geberator to create the slug.

The signup page is failing the W3C validator but as it's a direct import from Django I can't edit it. 

![W3C](static/media/images/w3csignup.png)

## Credits

This blog is heavily based on the walkthrough blog project from code institute. A lot of the standard code is used from this project. Like the structure of the blog and styling.  

Images are from pexels.com

### Acknowledgments

I realise this project may not be up to the standard that's most likely expected. 

I didn't have a lot of time with this project as I work in retail and due to some staffing issues the run up to Christmas was extremely busy for me. I asked for an extension to allow me more time to impliment changes but as yet I haven't got a response. 

There is a lot more I want to do with this project like add more detailed fields to the model and add more security. I need more authentication and I dont have any error 403/404/500 pages etc. I would also like to style it better.
the Readme and testing file are sparse as well but I haven't the time.

My Mentor Graham helped a lot and the tutor support really helped as well. 

<https://seanorourke7.github.io/ProjectGolf>

---

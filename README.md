# Elite Final Project Demo

## Intro
This is a demo of the Elite Web App Course final project. For demonstration, I filled out details from my personal website into the home page. 

Also, this contains a working copy of the functional component of the final project; the chatroom feature is accessible through the Nav bar.

## Components

### Personal Portfolio Page
This page is meant to showcase a personal portfolio, resume, or general personal content. This should provide a good northstar on the basics of HTML, CSS and responsive design.

In the starter final project template, we have provided:
* A hero section
* A sub banner section
* Text blurb
* Project descriptions
* Interests (with hover flip cards)
* Footer with contact info

The hero section for this project also has an added parallax effect. Feel free to contact me if you want assistance in implementing this for yourself.

### Chat Application
The chat application is the functional portion of the final project. A working solution should be able to generate user sessions, private chatrooms, and functional chat message posting and receiving. 

The typical user stories are as follows:

#### User Creates Chatroom
* User goes to the create channel page
* Fills in the channel name and hits submit
* User is directed to the channel page
* IF the user is not currently in a session
  * Redirect them to the session create (login) form
  * User gives a username and submits
  * User is given a token that's stored in cookies
  * User is redirected to the channel page
* User is on the channel page, gets initial messages, and can send messages

#### User Joins Chatroom
* User is given a link to a channel page
* User visits channel page
* IF the user is not currently in a session
  * Redirect them to the session create (login) form
  * User gives a username and submits
  * User is given a token that's stored in cookies
  * User is redirected to the channel page
* User is on the channel page, gets initial messages, and can send messages

Any user with the appropriate link should be able to join a room.

:warning: | Security
:---: | :---

This is meant to be a working demonstration at an appropriate level of complexity for the course. These chats should not be considered secure or truly private. There are two large issues that aren't addressed:
* Usernames can be assumed by anyone and there is no entity resolution performed on the backend. IE anyone can claim a username, and two people in the same chat with the same username will be considered the same.
* Chatrooms are private through obscurity and reliance on probability. Chatrooms are generated/identified through random hash, and collisions are not checked. We do not check authorization on chatrooms (how could we, there are no authenticated entities), and rely on simple randomness to ensure privacy. Collision checking is not included for sake of simplicity for the course.

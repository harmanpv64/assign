#Q1
#Access Tokens :- Access tokens are the thing that applications use to make API requests on behalf of a user.
# It represents the authorization of a specific application to access specific parts of a user's data.
#Access tokens must be kept confidential in transit and in storage.
#Consumer_Key ="Enter your key"
#Consumer_Secret="Enter your secret key"
#Access_Token="Enter your token key "
#Access_Secret="Enter your secret key"

#Q2:-

#IP Address of ganna.com 95.211.219.67
#IP Address of whatsapp 31.13.69.240
#IP Address of Snapchat 216.58.217.115
#IP Address of google  172.217.15.68
#IP Address of facebook 31.13.69.230

#question3:-
from key import Consumer_Key,Consumer_Secret,Access_Token,Access_Secret
import tweepy
oauth = tweepy.OAuthHandler(Consumer_Key ,Consumer_Secret)
oauth.set_access_token(Access_Token,Access_Secret)
api=tweepy.API(oauth)
print(api.search("#modi"))

#Q4:-
#library:- It is a collection of functions / objects that serves one particular purpose. you could use a library in a
# variety of projects. (Various specialized services in our case)
# API:- It is an interface for other programs to interact with your program or library  without having direct access.
#  ( giving specifications for our need to various vendors in our case)


#Library:It is written in same language which is collection of all the function required
#API: It can be written in any language

#Library: It contains re-usable chunks of code
#API:The re-usable codes of library is linked to our program through API.

#Library:-Every library has API that defines how it will interact with external code.
#Libarary example:- Numpy is a library of Python, adding support for large, multi-dimensional arrays and matrices, along
 #   with a large collection of high-level mathematical functions to operate on these arrays.

#API:-It is sum of all public/exported stuff.
#API example:-Uber ,Ola uses Google Maps API to show navigations and ways .
#Q5:-
from key import Consumer_Key,Consumer_Secret,Access_Token,Access_Secret
import tweepy
oauth = tweepy.OAuthHandler(Consumer_Key ,Consumer_Secret)
oauth.set_access_token(Access_Token,Access_Secret)
api=tweepy.API(oauth)
print(api.search("#FathersDay"))

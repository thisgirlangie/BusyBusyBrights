Hackbright class assignment:

1. Create 3 tables: Users, Posts, Votes
2. Make a webapp with Flask

Here are the types for said table columns:

Users
* id:int
* email:string
* password:string

Posts
* id:int
* title:string
* body:text
* user_id:int
* created_at:date

Votes
* id:int
* user_id:int
* post_id:int
* value:int

Flask project: What would Hackbrights do?
* Takes in posts (ie. ideas for events) by users
* Lets users vote on them
* Sorts by date (ie. view by today, tomorrow)

Requirements: 
1. Make user
2. Log in as user to add post (or, to add post, must log in as user)
3. Log in as user to vote (or, to vote, must log in as user)

Webpages Required:
* User_Add
* User_Log_In
* Post_Add 
* Vote_Add

Concepts to Tackle: 
* User Authentication
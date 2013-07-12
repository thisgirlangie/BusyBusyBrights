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
# ddd_shop Assesment

I did not manage to finish the task and I had no experience with django before starting. 
However, I thought it was still important to give it a go and I have explained a bit of my thought and design process. 

## Step 1: Requirements and HLD

My first step was to break down the requirements. 

I looked at each individual user requirements and drew an object relational diagram.

I also drew up a diagram showing how the upload process would work. 

##### Assumptions made
* Admin is the only one who can give users persmissions
* Sale items are only created after processing
* Attendants cannot access files after they are processed
* A store owner cannot be an attendant
* Only attendants can upload and modify files

## Step 2: Models

The first implementation step I took was to create the models.
I later saw that it was better to create applications for a store and sales

* [User model](ddd_shop/users/models.py)
* [Store model](ddd_shop/store/models.py)
* [Sales model](ddd_shop/sales/models.py)
## Step 3: Views and Permissions

My next step was to work on the views. 
This is where I had a major challenge and spent time to understand the framework.

* [Store Views](ddd_shop/store/views.py)
* [Sales Views](ddd_shop/sales/views.py)


## Step 5: Tasks

Unfortunately, I did not get to this step before the submission deadline 

However, this is how I had intented to go about it:

I was going to set up a task

1. to archive the files to a different repository
2. update sales from files

## Overall

__Thank you for considering my application thus far__ 

This was a great learning opportunity. I will definitely be using this to improve my skills. 
I know there is no perfect softare developer but with practice we learn to become better at delivering results.  




# Contribution Guidelines #

Your code is **OUR** code and we have to work as a team.  
For a consistent work flow and better understanding, please read and follow the path.  
*May the Force be with you!*

- [Submit an issue](#submit-an-issue)
- [Submit your work](#submit-your-work)
    - [Create a branch](#create-a-branch)
    - [Commit your work](#commit-your-work)
    - [Get help and feedback](#get-help-and-feedback)
    - [Document your code](#document-your-code)
    - [Test your code](#test-your-code)
- [Deploy](#deploy)

## Submit an issue ##

1. Make sure is a bug.  

2. Check Github to see if the bug wasn't already reported.  

3. Collect information

  * Try to reproduce the bug, on multiple accounts and/or browsers.
  * Use the browser console to see API calls, JS errors, trace files. If you find something related to the problem printscreen the information.
  * Find out if there isn't a bigger problem to which the issue is related.

## Submit your work ##

### Create a branch ###

Create a new branch from the newest version of **master** branch. Name it using the pattern:  

``` 
type/1234-description-name 
```

* *type* describes your type of work:  

  1. **b** from *bug*  

  2. **f** from *feature*  

* *1234* is the number of the issue from Github  

* *description-name* give's a short descriptive name for the branch.   

Don't use the word **master** for your branch. Name a master branch with the project name.

### Commit your work ###

Commit and update(push) on your branch continuously. **IMPORTANT**: When you commit your work/files add a short commit message and the issue number.  

Example: 
```
git commit -m 'added unittest for Mysql logger #1234'
```

### Get help and feedback ###

* Open a Pull Request(PR)  

When you have advanced in your task merge **master** branch with yours. In case of conflicts resolve them and open a PR.  

* Code review  

Ask for a code review. You can also ask on Campfire for a code review.  
Discuss with your reviewer and refactor/improve your code. It is encouraged that everyone does code review, don't be afraid, look for mistakes in code the other might have missed, or for best practices one should follow.

### Document your code ###

* Add comments in your code. Others and even you, will need to understand the logic of your code. More info [here](http://google-styleguide.googlecode.com/svn/trunk/pyguide.html?showone=Comments#Comments)
* If your task was a feature, which adds new files and logic to the code, add documentation.
* Documentation can be added in ```docs``` root folder.

### Test your code ###

Write unittests for your code. Everything has a place, if you don't know where to write one ask a team mate.

## Deploy ##

After reviewers give an ACK, the code is tested and works, and all tests pass, you can merge your PR in **master**.
#### Congrats! ####

This means that your feature/capability is live. You are in charge of fixing bugs related to your feature for a week's time after you deployed it.   

# Happy shipping! #

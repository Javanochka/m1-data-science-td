# Working with git

We will learn how to use git during this class. At the same time I will show you a way you could show me your work so that I could comment it. 


## Set-up and and main git commands

[A site with documentation and tutorials](https://git-scm.com/docs/gittutorial)

## Task done? 

1. Fork this repository. Later you will work with a forked repository.
2. Clone the forked repository to your computer.

  ```
  $ git clone <your-fork-url>
  ```
 
3. Create a branch, where you are going to work:

  ```
  $ git checkout -b <your-assignment-branch>
  ```
To work with the same thing let's all call the branch for the first task `git-task-01`.
General rule to share your work with me: each task is better to be in its own branch. 

To access the branch, when it is already created:

  ```
  $ git checkout <your-branch>
  ```

4. Complete your task. :) Now you can add information and three facts to the file `facts.py`, make sure one of the facts is wrong.

5. Save your changes and send them to the server:

  ```
  $ git commit -m <your-message>
  $ git push
  ```
If you push the branch for the first time, you should also mention that you want it to be sent to your forked repository and not this one.

  ```
  $ git push -u origin <your-assignment-branch>
  ```

6. Make a pull request into this repository, using instructions from [here](https://help.github.com/articles/creating-a-pull-request/). I will show how to do that in class though.

7. You can comment the pull request! And ask the author of it to change something. And this is how I will give you feedback in future.

8. Now, try to correct something. :) 

## Update with the original repository and new tasks completion

1. I assume you already have a fork repository and its copy on your laptop. If that's not true, see above how to do that.
2. Check that git is set up for synchronization with this repository:

  ```
  $ git remote -v
  ```
  
  If output of this command contains `upstream <original-repository-link>`, then go to step 4.

3. Set up git for synchronization with this repository:

  ```
  $ git remote add upstream <original-repository-link>
  ```
4. Get the updates to your fork:

  ```
  $ git fetch upstream
  ```

5. Apply the updates to the main branch. (There is still a possibility your main branch can be called something else -- check with `git branch -a`)
  ```
  $ git pull upstream main
  ```

6. Further you will work with this repository using steps 3-8 from the instruction above.




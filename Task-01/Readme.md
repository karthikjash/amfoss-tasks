## APPROACH
The Command Line Cup was very interesting, as I'm a die-hard fan of Harry Potter Franchise. following describes how i solved this challenge;

At first I cloned the github repository using the provided command to my local repository and created a directory named codes inside the repo.
Then I created My own repository called amfoss-tasks to store my results of the tasks and created "01" folder for my task 01.

**First Challenge**

To fight the blast-ended-skrewt, The required spell was in 0x directory within a .txt file named Spell_0y, where x found to be 6 and y is 5.
Using ls,cd, and cat commands, I Got the spell and I went to the spellbookdirectory that contains the python file which had similiar name. On the first execution, It didn't worked, and I accidentally deleted my python3 pkg. After some works, It went back to normal and then
I copied the code and saved it as part_1.txt along with the respective python file inside the codes directory.
Then Added the files for commit, commited the changes and pushed it to main branch, to my amfoss-tasks repo using necessary git commands.

**Second Challenge**

Found the spell by solving the riddle. I went through the same procedure I did previously and got the code.
I copied the second code and saved it as part_02.txt with the python file along with it in the codes dir.
then added, committed, and pushed the new files.

**Third Challenge**

Riddle was easy but I wasn't aware about branches, upon reading the guide that provided, I went to lupin's subject branch and got the python file. Using git checkout command, I was able to execute the python file
and saved the code.

Add, commit, push repeat :)

**Fourth Challenge**

I went to the commit logs of the provided repo in search of the ultimate spell against the Darklord inorder to escape.
Got the branch and path, through git checkout commands, went there and executed the spell to escape from him...

It took about *3-4 hours* of time to complete until here.

**The END**

Joined all the codes to find the finalcode and uploaded it as finalcode.txt to repo through commit.
Used echo base64 decoding command to find the hidden info and it turns out to be the link of another repo. So I went there took the screenshot and uploaded it to this repo through git commit.
Cloned that repo and it was a congradulating message from the amfoss. As they said I created another file named SOLUTION.md to save the commands used for this challenge.

## COMMANDS LEARNED

### *Ubuntu Terminal*

``cd <path>`` Changes the current working directory to the specified path.

``ls`` Lists files and directories present in the current directory.

``cp <file> <place>`` To copy a file to another place.

``mv <file> <place>`` To move a file to another place.

``mv <old name> <new name>`` To rename a file.

``mkdir <name> `` To create a directory.

``touch <name> `` To create an empty file.

``nano <filename>`` To create or modify an existing file.

``rm <filename>`` To remove a file.

``chmod:`` Modifies file permissions.

``cat <file_name>`` Outputs the contents of a file.

``python3 <filename.py>`` To run a python file

### *Git*

``git init:`` Initializes a directory as a Git repository.

``git clone <url>:`` Clones the repository from the specified URL.

``git add [filename]:`` Stages the specified file for commit.

``git add .:`` Stages all changes in the current directory for commit.

``git status:`` Displays the files that have been modified.

``git branch:`` Lists all available branches in the repository.

``git checkout <branch>:`` Switches between branches.

``git commit -m "commit message": `` To commit the changes.

``git push:`` Pushes the local branch's changes to the remote repository.

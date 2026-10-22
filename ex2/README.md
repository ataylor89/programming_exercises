# Exercise 2

I generated the file encrypted_message.txt by running the following commands in Terminal.

    % cd ~/Github/programming_exercises/ex2
    % ls
    __pycache__	addsubtract2.py	asdecrypt2.py	asencrypt2.py	bruteforce.py	dictionary.txt	README.md
    % python asencrypt2.py -m "hello world today is thursday october 22 2026" -k 235,239,293 -o encrypted_message.txt

Then I ran the script bruteforce.py with the following command:

    % python bruteforce.py 
    We were unable to decrypt the encrypted message.

You can see that our new algorithm is more secure.

It's more secure to use a list of integers as our key.

It's natural to ask, "Can we modify the bruteforce.py script to work for multiple-integer keys?"

This is a good question... and maybe we'll attempt it in a future exercise.

If a three-integer key turns out to be insecure, then we'll implement some improvements to make it more secure.

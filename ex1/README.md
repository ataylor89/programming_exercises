# Exercise 1

I generated the file encrypted_message.txt by running the following commands in Terminal.

    % cd ~/Github/programming_exercises/ex1
    % ls
    __pycache__	addsubtract.py	asdecrypt.py	asencrypt.py	bruteforce.py	dictionary.txt	README.md
    % python asencrypt.py -m "hello world today is thursday october 22 2026" -k 235 -o encrypted_message.txt

Then I ran the script bruteforce.py with the following command:

    % python bruteforce.py
    Success! We were able to decrypt the encrypted message.
    Message: hello world today is thursday october 22 2026
    Key: 235

You can see that our addsubtract encryption algorithm is not quite secure, because it can be easily brute forced.

However, we can make our algorithm a lot more secure, by making the key a list of numbers, instead of a single number.

We'll do this in programming exercise #2.

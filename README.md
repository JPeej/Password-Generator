<h1 align="center">Password Generator</h1>

I was tasked to create a password generator in my class, "100 Days of Code: The Complete Python Pro Bootcamp for 2022" by Dr. Angela Wu. I am taking this Udemy class on the side of my official coursework at Western Governors University. This is day five of the class. 

<h2>I was to focus on using the following concepts that I learned today.</h2>

-For loops.

-Range function.

<h2>What I learned</h2>
Today seemed like a larger step than normal. I would like to think grasping loops is a fundamental skill I must master. This project helped me move in that direction. Understanding that the variable declared in the for loop statement was assigned to each list item was a step for me. I also found through SO that rather than defining a range like:

```
range(0, num_symbols)
```

I can just do:

```
range(num_symbols)
```

It isn't much but will overtime cut down on data and time. My first attempt had much more code and attempted to create nested lists within a master password list, randomize order of that list through another for loop, and then concatenate the list in a very laborious way. After more SO I found both random.shuffle and .join. So much better. One more feature that I am proud of implementing is a check to make sure the desired amount of characters is actually available within the list.

<h2>Issues I had and where I can do better.</h2>
During my first attempt I defined a variable num_letters and tried to use in a range to find random letters. I don't remember exactly how it went but I think it was close to this:

```
num_letters = int(input("How many letters would you like in your password?\n"))

for i in range(0, num_letters):
    ran_letter = letters[random.randint(0, 53)]
    ...
```

I ran into a issue whenever the random character that came through was a duplicate it would throw a index out of range error. I had no idea how to fix it. I also wanted to implement a feature to check that the user did input integers and not characters. I came across the try and except statements but could not get them to work. I found where if I did input a character it would throw a ValueError. I tried to place both a try and except but got so many errors syntactly. I need to come back to that.

# How to use the provided solutions?

Some exercises might prove too tough for you to solve alone. Or you might want to see some reference code to try and figure out why your code does not work as intended. **That's why we've included our own solutions to each question!** Feel free to check them out.

Here's how to interpret the solution files:
- Usually, they start with a `# comment` or a `"""multiline comment"""`.
- You should try to **find the same comment in your own files**, because we use these comments as "bookmarks".
    - If a code block in the solution file starts with a comment, the code that follows should be placed under (or replace) the same comment in the original file.
    - Sometimes, a file might need to be modified in multiple different places. In this case, in the solution file there will be at least 2 blank lines between the last line of code, and the next comment that you should be looking for.
- Sometimes, it might be necessary to adjust the indendation of the copied code. Your code editor will most likely let you know if that is the case. You can fix it by selecting the affected block of code, and adjusting the indendation using the Tab or Shift+Tab keybinds.
- By applying these "solutions" to the original files, you should end up with perfectly working code.

<details>
<summary>💡 Here's an example how a solution file could work:</summary>

File python.py
```py
function()

# TODO: call function2 here.

function3()
```

File solutions/python.py
```py
# TODO: call function2 here.
function2()
```

Resulting file python.py:
```py
function()

function2()

function3()
```
</details>
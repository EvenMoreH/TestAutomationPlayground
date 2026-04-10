# Non-Breaking Space
There are cases in test automation when something should obviously work but for some reason it does not. Searching for an element by its text is one of those cases. Text caption may contain non-breaking spaces that have no visual difference from generic spaces.

## Scenario
Use the following xpath to find the button in your test:

//button[text()='My Button']

Notice that the XPath does not work. Change the space between 'My' and 'Button' to a non-breaking space. This time the XPath should be valid.


## Link
http://uitestingplayground.com/nbsp
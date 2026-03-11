# Text Input
Entering text with physical keyboard can be different from sending DOM events to an element. This page is specifically designed to illustrate this problem. There are cases when attempts to set a text via DOM events lead to nowhere and the only way to proceed is to emulate real keyboard input at OS level.

## Scenario
- Record setting text into the input field and pressing the button.
- Then execute your test to make sure that the button name is changing.

## Link
http://uitestingplayground.com/textinput
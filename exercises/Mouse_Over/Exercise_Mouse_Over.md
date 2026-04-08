# Mouse Over
Placing mouse over an element may lead to changes in the DOM tree. For example the element may be modified or replaced. It means if you keep a reference to the original element and will try to click on it - it may not work (stale element problem).

This puzzle complicates both recording and playback of a test.

## Scenario
- Record 2 consecutive link clicks.
- Execute the test and make sure that click count is increasing by 2.

## Link
http://uitestingplayground.com/mouseover
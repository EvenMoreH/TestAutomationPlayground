# Verify Text
In general inner text of a DOM element is different from displayed on screen. Browsers normalize text upon rendering, but DOM nodes contain text as it is in HTML markup. For example a browser may show the text as

Hello UserName!

and the text of the DOM element can be

                
    Hello UserName!
        

Take this fact into account when searching for an element using it's text value.

Does not work
//span[.='Welcome UserName!']

Works
//span[normalize-space(.)='Welcome UserName!']

## Scenario
- Create a test that finds an element with Welcome... text.

## Link
http://uitestingplayground.com/verifytext
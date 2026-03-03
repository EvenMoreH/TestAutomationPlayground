# Dynamic ID
Modern applications often generate dynamic IDs for elements. In this case ID is not a reliable attribute for using in element selector. By default many UI automation tools record IDs and this results in tests broken from the very beginning. An automation tool needs a way to instruct it to skip dynamic IDs when XPath is generated for an element.

## Scenario
- Record button click.
- Then execute your test to make sure that ID is not used for button identification.

## Link
http://uitestingplayground.com/dynamicid
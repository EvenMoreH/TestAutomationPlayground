# Frames
Working with frames requires switching context. Automation tools need to locate frames and switch into them before interacting with elements inside. This page contains nested frames with identical button markup to practice element location strategies.

## Element Search Strategies
- data-* attribute - find button by custom data attribute value
- text - find button by inner text content
- name - find button by @name attribute
- xpath with class - find button by class using XPath

## Scenario
- Switch to the outer frame (level 1).
- Find and click each button using different locator strategies.
- Switch to the inner frame (level 2) nested inside the outer frame.
- Find and click the same buttons (identical markup) in the inner frame.

## Link
http://uitestingplayground.com/frames
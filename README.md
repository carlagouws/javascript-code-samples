# Javascript Code Samples

A storage repo for practise javascript projects.

## Binary Calculator

**Tier:** 1-Beginner

**Description:** Allow the user to enter strings of up to 8 binary digits, 0's and 1's, in any sequence and then displays its decimal equivalent.

**User Stories:**
- User can enter up to 8 binary digits in one input field
- User must be notified if anything other than a 0 or 1 was entered
- User views the results in a single output field containing the decimal (base 10) equivalent of the binary number that was entered

## Calculator

**Tier:** 1-Beginner

**Description:** Create a calculator that supports basic arithmetic calculations on integers.

**Constraints:**
- Do not use the eval() function to execute calculations

**User Stories:**
- User can see a display showing the current number entered or the result of the last operation.
- User can see an entry pad containing buttons for the digits 0-9, operations - '+', '-', '/', and '=', a 'C' button (for clear), and an 'AC' button (for clear all).
- User can enter numbers as sequences up to 8 digits long by clicking on digits in the entry pad. Entry of any digits more than 8 will be ignored.
- User can click on an operation button to display the result of that operation on:
  - the result of the preceding operation and the last number entered OR 
  - the last two numbers entered OR 
  - the last number entered
- User can click the 'C' button to clear the last number or the last operation. If the users last entry was an operation the display will be updated to the value that preceded it.
- User can click the 'AC' button to clear all internal work areas and to set the display to 0.
- User can see 'ERR' displayed if any operation would exceed the 8 digit maximum.
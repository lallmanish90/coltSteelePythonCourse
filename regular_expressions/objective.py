"""
RegEx
Regular Expressions

what are regular expressions?
-a way of describing patterns within search strings 

**Example:
validating emails 
validation guidelines:
starts with 1 or more letter, number, + , _,-,. then
    a single sign then
        1 or more letter, number , or - then
             a single dot then
                ends with 1 or more letter , number, - , or . 
**lets write a regular expression:
(^[a-zA-Z0-9_.+-]+[a-zA-Z0-9-]+\.[a-zA-z0-9-.]+$)



potential use cases
-credit card number validating
-phone number validating
-advanced find/replace in text
-formating text/output
-syntax highlighting 


"""

"""
There are a TON of REGEX SYMBOLS.
-going to cover basic ones

\d - digit 0-9
\w - letter,digit, or underscore
\s - whitespace charector
\D - NOT ad digit
\W - NOT a word character 
\S - NOT a whitespace charector
. - any charecter except line break

"""

"""
Quantifiers 

+ - one or more
{3} - exactly , times. inside the curly braces 
{3,5} - this is a range of times
{4,} - at least this many times
* - zero or more times 
? - once or none(optional)
"""

"""
Class Charecters 
[]
[] - will match anything with any value inside the brackets 

"""
"""
Anchors 
^ - start of a string
$ - end of a string
\b -word boundry , either a space or end of a line
"""
"""
Logical OR
| (pipe character)

 has two sides 
 can use parens to group the conditional 
"""

## Introduction to Data Science in Python
### Course 1

Here goes the scripts that I wrote relating to the concepts discussed
in the first course of this specialization.  

### Scripts:

- **demo-p-value.py** - has no dependencies, should work locally  
A demo of the unreliability of p-values and how easy it is to generate
datasets with statistically significant difference using random numbers.  

- **demo-vectorization.py** - has no dependencies, should work locally  
A simple Speed comparison between different methods of adding
floating-point numbers and the power of vectorization.  


Having been introduced to the exciting world of Numpy, I was thrilled
to realize I can combine the power of Numpy with Pillow. The following
two scripts are my first attempts at doing just that.  

- **lincoln-encode.py** - dependencies accounted for, should work locally  
Embeds the United States Constitution into the famous Abraham Lincoln
"cracked glass plate" photograph.  

- **lincoln-decode.py** - dependencies accounted for, should work locally  
Extracts the United States Constitution from the famous Abraham Lincoln
"cracked glass plate" photograph. Basically, reversing the encoding.  

The cypher for the above two scripts is simple: put every character in
the US constitution in every prime numbered pixel of the image, starting
from pixel number 1787 (the year the Constitution was signed).  
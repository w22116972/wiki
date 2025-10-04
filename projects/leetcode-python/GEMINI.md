# Add py file for leetcode question

## when I type ${QUESTION_NUMBER_OF_LEETCODE}

### 1. Create py file named like following script

1. You should find the question name by question number
2. Use that question number and name to create py file

The naming rule of py file is "leetcode_{$QUESTION_NUMBER}_{$QUESTION_NAME}.py"
- question name should be all lower cases
    - space " " should be replaced by underscore "_"

### 2. Write content

- Leetcode initial python function `Class Solution` ... etc
    - import required library if there are any in input, e.g. `from typing import List`
- Leetcode Problem description, constraints, follow-up
- The initial function with input should be provided
- Don't provide any solution
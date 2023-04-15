# LeetCode-Solutions

 This repository contains my solutions to various LeetCode problems.


##Table of Contents

+Getting Started
+Dependencies
+Running the Code
+Solution Examples
+External Resources
+LeetCode Profile
+Conclusion

##Getting Started

LeetCode is a platform for practicing and improving your coding skills by solving algorithmic problems. This repository contains my solutions to various LeetCode problems, along with explanations and code snippets to help you understand my approach.

##Dependencies

The solutions in this repository are written in Python and require no additional dependencies.

##Running the Code

To run the code in this repository, simply clone the repository to your local machine and run the individual Python files for each problem.

##Solution Examples
Here are a few examples of my solutions to LeetCode problems:

###Two Sum
python 3
towsum code ss.png
`class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range((i+1),len(nums)):
                if((nums[i]+ nums[j]) == target):   
                    return [i,j]
        return []`

##External Resources

I used a variety of external resources to help me solve problems on LeetCode, including:

+[LeetCode Discuss Forum](https://leetcode.com/discuss/interview-question?currentPage=1&orderBy=hot&query=)
+[YouTube Tutorials](https://www.youtube.com/)
+[Online Articles and Blog Posts](https://www.google.com/)

##LeetCode Profile

To see more of my solutions and progress on LeetCode, check out my [LeetCode profile](https://leetcode.com/KavinduPiyumantha/).

##Conclusion

LeetCode has been a great platform for practicing and improving my coding skills, and I hope that my solutions can be helpful to others in the community. If you have any questions or feedback, feel free to reach out or leave a comment on a specific problem solution.




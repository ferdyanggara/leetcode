"""
Link: https://leetcode.com/problems/complex-number-multiplication/
A complex number can be represented as a string on the form "real+imaginaryi" where:

real is the real part and is an integer in the range [-100, 100].
imaginary is the imaginary part and is an integer in the range [-100, 100].
i2 == -1.
Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.



Example 1:

Input: num1 = "1+1i", num2 = "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:

Input: num1 = "1+-1i", num2 = "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.


Constraints:

num1 and num2 are valid complex numbers.
"""


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1_real, num1_imag = num1.split('+')
        num2_real, num2_imag = num2.split('+')
        num1_imag_mult = int(num1_imag[:-1])
        num2_imag_mult = int(num2_imag[:-1])
        num1_real = int(num1_real)
        num2_real = int(num2_real)
        num_imag_sq = num1_imag_mult * num2_imag_mult * -1
        num_imag_1 = num1_real * num2_imag_mult
        num_imag_2 = num2_real * num1_imag_mult
        total_imag = num_imag_1 + num_imag_2
        num_real = num1_real * num2_real
        return str(num_real + num_imag_sq) + '+' + str(total_imag) + 'i'

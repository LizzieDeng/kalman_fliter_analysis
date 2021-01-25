"""
A test script for the exponentiation functions.

This test script illustrates the performance difference between the two functions.

Author: Walker M. White (wmw2)
Date:   October 10, 2018
"""
import introcs
import com
import exp




def test_exp_slow():
    """
    Tests the slow version of exponentiation
    """
    # Count the number of call frames
    print('Testing exp_slow')
    exp.count_frames = 0
    introcs.assert_floats_equal(1.0,     exp.exp_slow(2, 0))
    introcs.assert_floats_equal(2.0,     exp.exp_slow(2, 1))
    introcs.assert_floats_equal(4.0,     exp.exp_slow(2, 2))
    introcs.assert_floats_equal(16.0,    exp.exp_slow(2, 4))
    introcs.assert_floats_equal(256.0,   exp.exp_slow(2, 8))
    introcs.assert_floats_equal(65536.0, exp.exp_slow(2, 16))
    print('Test used a total of '+str(exp.count_frames)+' call frames')


def test_exp_fast():
    """
    Tests the fast version of exponentiation
    """
    # Count the number of call frames
    print('Testing exp_fast')
    exp.count_frames = 0
    introcs.assert_floats_equal(1.0,     exp.exp_fast(2, 0))
    introcs.assert_floats_equal(2.0,     exp.exp_fast(2, 1))
    introcs.assert_floats_equal(4.0,     exp.exp_fast(2, 2))
    introcs.assert_floats_equal(16.0,    exp.exp_fast(2, 4))
    introcs.assert_floats_equal(256.0,   exp.exp_fast(2, 8))
    introcs.assert_floats_equal(65536.0, exp.exp_fast(2, 16))
    print('Test used a total of '+str(exp.count_frames)+' call frames')


# Application Code
if __name__ == '__main__':
    test_exp_slow()
    test_exp_fast()
    print('Module exp passed all tests')

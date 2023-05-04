import unittest
import filecmp

# To run test cases. 1) Go to scanner.py, run all the 11 test cases to produce the 
# results.txt file. 2) run the tests 3) If true it passed if false it failed
class TestAssetions(unittest.TestCase):
	# Test Case for Test 1
	def test_1(self):
		test_num1 = 'expected_outputs/eo_test1.txt'
		result = filecmp.cmp('output_results/results1.txt', f"{test_num1}")
		self.assertTrue(result)

	# Test Case for Test 2
	def test_2(self):
		test_num2 = 'expected_outputs/eo_test2.txt'
		result = filecmp.cmp('output_results/results2.txt', f"{test_num2}")
		self.assertTrue(result)

	# Test Case for Test 3
	def test_3(self):
		test_num3 = 'expected_outputs/eo_test3.txt'
		result = filecmp.cmp('output_results/results3.txt', f"{test_num3}")
		self.assertTrue(result)

	# Test Case for Test 4
	def test_4(self):
		test_num4 = 'expected_outputs/eo_test4.txt'
		result = filecmp.cmp('output_results/results4.txt', f"{test_num4}")
		self.assertTrue(result)

	# Test Case for Test 5
	def test_5(self):
		test_num5 = 'expected_outputs/eo_test5.txt'
		result = filecmp.cmp('output_results/results5.txt', f"{test_num5}")
		self.assertTrue(result)

	# Test Case for Test 6
	def test_6(self):
		test_num6 = 'expected_outputs/eo_test6.txt'
		result = filecmp.cmp('output_results/results6.txt', f"{test_num6}")
		self.assertTrue(result)

	# Test Case for Test 7
	def test_7(self):
		test_num7 = 'expected_outputs/eo_test7.txt'
		result = filecmp.cmp('output_results/results7.txt', f"{test_num7}")
		self.assertTrue(result)

	# Test Case for Test 8
	def test_8(self):
		test_num8 = 'expected_outputs/eo_test8.txt'
		result = filecmp.cmp('output_results/results8.txt', f"{test_num8}")
		self.assertTrue(result)

	# Test Case for Test 9
	def test_9(self):
		test_num9 = 'expected_outputs/eo_test9.txt'
		result = filecmp.cmp('output_results/results9.txt', f"{test_num9}")
		self.assertTrue(result)

	# Test Case for Test 10
	def test_10(self):
		test_num10 = 'expected_outputs/eo_test10.txt'
		result = filecmp.cmp('output_results/results10.txt', f"{test_num10}")
		self.assertTrue(result)
		
	# Test Case for Test 11
	def test_11(self):
		test_num11 = 'expected_outputs/eo_test11.txt'
		result = filecmp.cmp('output_results/results11.txt', f"{test_num11}")
		self.assertTrue(result)
	
if __name__ == '__main__':
	unittest.main()
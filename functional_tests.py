from selenium import webdriver
import unittest
import time

class NewVisitorTest(unittest.TestCase):
	# 开始函数
	def setUp (self):
		self.browser = webdriver.Firefox()
	
	# 结束函数
	def tearDown (self):
		self.browser.quit()
	
	# 测试的方法
	def test_can_start_a_list_and_retvieve_it_later (self):
		self.browser.get("http://localhost:8000")
		print(self.browser.title)
		self.assertIn("To-Do", self.browser.title)
		self.fail("Finish the test!")


if __name__ == '__main__':
	unittest.main(warnings = 'ignore')

# browser=webdriver.Firefox()
# browser.get("http://localhost:8000")
# assert 'TO-DO' in browser.title,"Browser title was "+browser.title
# browser.quit()

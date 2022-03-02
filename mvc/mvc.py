'''
python mvc minimum example

python mvc.py Hello
'''

import sys


class GenericModel:
	def __init__(self):
		pass
	def get_data(self, request):
		return {'request':request}

class GenericView:
	def __init__(self):
		pass
	def render(self, data):
		print(data)

class GenericController:
	def __init__(self) -> None:
		self.model = GenericModel()
		self.view = GenericView()
	def handle(self, request):
		we_wanna_show = self.model.get_data(request)
		self.view.render(we_wanna_show)

def main(name):
	request_handler = GenericController()
	request_handler.handle(name)

if __name__ == '__main__':
	main(sys.argv[1])

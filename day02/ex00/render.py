import sys, os, re

def	test_errors():
	# test arguments and files
	if len(sys.argv) != 2:
		print('Error. Invalid number of arguments')
		exit ()
	if os.path.isfile(sys.argv[1]) == False:
		print("Error. Template file doesn't exist")
		exit ()
	if os.path.isfile('settings.py') == False:
		print("Error. Settings file doesn't exist")
		exit ()
	# init variables
	file_template = sys.argv[1].split('.')
	name_html = file_template[0] + '.html'
	file_extension = file_template[1]
	# test extension file
	if file_extension != 'template':
		print("Error. Choose a '.template' file")
		exit ()
	return name_html

def	set_template_values(content_t, dic):
	new_content = content_t
	# replace infos in template
	for y in dic:
		new_content = new_content.replace('{' + y + '}', dic[y])
	return new_content.strip('\n')

def	write_html_file(file_html, content_t, dic):
	# set values in variables
	content_t = set_template_values(content_t, dic)
	# write new content in html
	file_html.write(f'''{content_t}
'''
	)

def	render():
	# test errors and return name_html if is ok
	name_html = test_errors()
	# open file and save content
	template = open(sys.argv[1], 'r')
	content_t = template.read()
	# read and save settings
	settings = open('settings.py', 'r')
	content_s = settings.read().split('\n')
	# create a dict with setting datas
	dic = dict()
	for line in content_s:
		var = line.split('=')
		if line != '':
			dic[var[0].strip(' ')] = var[1].strip(' ').strip('"')
	# create html file
	file_html = open(name_html, 'w')
	write_html_file(file_html, content_t, dic)
	# close files
	file_html.close()
	template.close()
	settings.close()

if __name__ == '__main__':
	render()
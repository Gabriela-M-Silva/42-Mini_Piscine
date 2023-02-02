# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    var_to_dict.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gde-mora <gde-mora@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/01 19:54:12 by gde-mora          #+#    #+#              #
#    Updated: 2023/02/01 21:44:42 by gde-mora         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	var_to_dict():
	d = [
		('Hendrix' , '1942'),
		('Allman' , '1946'),
		('King' , '1925'),
		('Clapton' , '1945'),
		('Johnson' , '1911'),
		('Berry' , '1926'),
		('Vaughan' , '1954'),
		('Cooder' , '1947'),
		('Page' , '1944'),
		('Richards' , '1943'),
		('Hammett' , '1962'),
		('Cobain' , '1967'),
		('Garcia' , '1942'),
		('Beck' , '1944'),
		('Santana' , '1947'),
		('Ramone' , '1948'),
		('White' , '1975'),
		('Frusciante', '1970'),
		('Thompson' , '1949'),
		('Burton' , '1939')
	]
	
	d_dic = { }
	for tup in d:
		if d_dic.setdefault(tup[1]):
			d_dic[tup[1]] = d_dic[tup[1]] + " " + tup[0]
		else:
			d_dic[tup[1]] = tup[0]
	
	for x, y in d_dic.items():
		print(x, ':', y)
	
if __name__ == '__main__':
	var_to_dict()
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    my_sort.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gde-mora <gde-mora@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/02 16:20:21 by gde-mora          #+#    #+#              #
#    Updated: 2023/02/03 19:39:14 by gde-mora         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	my_sort():
	d = {
		'Hendrix' : '1942',
		'Allman' : '1946',
		'King' : '1925',
		'Clapton' : '1945',
		'Johnson' : '1911',
		'Berry' : '1926',
		'Vaughan' : '1954',
		'Cooder' : '1947',
		'Page' : '1944',
		'Richards' : '1943',
		'Hammett' : '1962',
		'Cobain' : '1967',
		'Garcia' : '1942',
		'Beck' : '1944',
		'Santana' : '1947',
		'Ramone' : '1948',
		'White' : '1975',
		'Frusciante': '1970',
		'Thompson' : '1949',
		'Burton' : '1939',
	}
	lst_years = sorted(d.values())
	dic_sorted_name = dict(sorted(d.items()))
	hold = ''
	for y in lst_years:
		if y != hold:
			for x in dic_sorted_name:
				if y == dic_sorted_name[x]:
					print(x)
		hold = y

if __name__ == '__main__':
	my_sort()



	c = 42

	(char)c
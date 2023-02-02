# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    all_in.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gde-mora <gde-mora@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/02 16:20:21 by gde-mora          #+#    #+#              #
#    Updated: 2023/02/02 17:35:34 by gde-mora         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def all_in():
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
	if len(sys.argv) != 2:
		exit ()
	else:
		li = sys.argv[1].split(',')
		for i in li:
			aux_list = i.split(' ')
			aux_str = ''
			for x in aux_list:
				if aux_str == '':
					if x != ' ':
						aux_str = x
				else:
					aux_str = aux_str + ' ' + x
			if (aux_str != ''):
				aux_str = aux_str.strip(' ')
				flag = 0
				for s in states:
					if aux_str.lower() == s.lower():
						for y in capital_cities:
							if states[s] == y:
								print(capital_cities[y], 'is the capital of', aux_str.title())
								flag = 1
								break
				for c in capital_cities:
					if aux_str.lower() == capital_cities[c].lower():
						for y in states:
							if c == states[y]:
								print(aux_str.title(), 'is the capital of', y)
								flag = 1
								break
				if flag == 0:
					print(aux_str, 'is neither a capital city nor a state')

if __name__ == '__main__':
	all_in()
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    state.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gde-mora <gde-mora@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/02 16:04:07 by gde-mora          #+#    #+#              #
#    Updated: 2023/02/02 16:15:46 by gde-mora         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def state():
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
		for x in capital_cities:
			if sys.argv[1].lower() == capital_cities[x].lower():
				for y in states:
					if x == states[y]:
						print(y)
						exit ()
		print('Unknown capital city')

if __name__ == '__main__':
	state()
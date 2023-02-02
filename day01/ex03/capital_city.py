# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    capital_city.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gde-mora <gde-mora@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/02 15:23:02 by gde-mora          #+#    #+#              #
#    Updated: 2023/02/02 16:08:29 by gde-mora         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def	capital_city():
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
		for x in states:
			if sys.argv[1].lower() == x.lower():
				for y in capital_cities:
					if states[x] == y:
						print(capital_cities[y])
						exit ()
		print('Unknown state')

if __name__ == '__main__':
	capital_city()
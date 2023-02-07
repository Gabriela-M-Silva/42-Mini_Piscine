# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    numbers.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gde-mora <gde-mora@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/01 18:44:23 by gde-mora          #+#    #+#              #
#    Updated: 2023/02/07 19:00:16 by gde-mora         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	print_numbers(var):
	for x in var:
		print(x.strip("\n"))

def	read_numbers():
	f = open("numbers.txt", "r")
	var = f.read().split(",")
	print_numbers(var)
	f.close()

if __name__ == '__main__':
	try:
		read_numbers()
	except:
		print("Error. Numbers file doesn't exist.")
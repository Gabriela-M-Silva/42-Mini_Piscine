# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    var.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gde-mora <gde-mora@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/01 18:16:42 by gde-mora          #+#    #+#              #
#    Updated: 2023/02/01 18:39:39 by gde-mora         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	my_var():
	var = 42
	print(var, 'has a type', type(var))
	var = "42"
	print(var, 'has a type', type(var))
	var = "quarante-deux"
	print(var, 'has a type', type(var))
	var = 42.0
	print(var, 'has a type', type(var))
	var = True
	print(var, 'has a type', type(var))
	var = [42]
	print(var, 'has a type', type(var))
	var = {42: 42}
	print(var, 'has a type', type(var))
	var = (42,)
	print(var, 'has a type', type(var))
	var = set()
	print(var, 'has a type', type(var))
if __name__ == '__main__':
	my_var()
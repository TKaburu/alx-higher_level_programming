#!/usr/bin/python3

""" Define the class """


class MyList(list):
    """ define the method """
    def print_sorted(self):
        """ This method prints the sorted list """
        sort_the_list = sorted(self)
        print(sort_the_list)

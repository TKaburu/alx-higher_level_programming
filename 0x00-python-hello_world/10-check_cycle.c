#include "lists.h"

/**
 * check_cycle - This function checks if a
 * singly linked list has a cycle in it
 * list: Pointer to the list
 *
 * Return: 1 if cycle is found outherwise 0
 */

int check_cycle(listint_t *list)
{
	listint_t *head = list, *current = list;

	/*if the listpoints to the end of the file(null) return 0*/
	if (list == NULL || list->next == NULL)
		return (0);
	while (current && current->next)
	{
		head = head->next;
		current = current->next->next;
		if (head == current)
			return (1);
	}
	return (0);/*if no cycle is found*/
}

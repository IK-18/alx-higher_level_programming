#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node -  inserts a number into a sorted singly linked list
 * @head: pointer to list head
 * @number: number to be inserted
 *
 * Return: adress of new node or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head, *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (!tmp || tmp->n >= number)
	{
		new->next = tmp;
		*head = new;
		return (new);
	}
	while (tmp && tmp->next)
	{
		if (tmp->next->n >= number)
			break;
		tmp = tmp->next;
	}
	new->next = tmp->next;
	tmp->next = new;
	return (new);
}

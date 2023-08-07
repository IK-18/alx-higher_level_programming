#include "lists.h"

/**
 * check_cycle - check for loop in LL
 * @list: head of linked list
 *
 * Description - check for loops in LL
 * Return: 1 if cycled, 0 if not
 */

int check_cycle(listint_t *list)
{
	listin_t *tmp1, *tmp2;

	if (!list)
		return (0);
	tmp1 = list;
	tmp2 = list->next;
	while (tmp1 && tmp2 && tmp2 ->next)
	{
		if (tmp1 == tmp2)
			return (1);
		tmp1 = tmp1->next;
		tmp2 = tmp2->next->next;
	}
	return (0);
}

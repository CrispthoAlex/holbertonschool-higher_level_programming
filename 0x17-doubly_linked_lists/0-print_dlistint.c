#include "lists.h"

/**
 * print_dlistint - print elemts of list.
 *
 * Return: number of elements
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t numnodes = 0;

	while (h != NULL)
	{
		numnodes++;
		printf("%d\n", h->n);
		h = h->next;
	}
	return (numnodes);
}

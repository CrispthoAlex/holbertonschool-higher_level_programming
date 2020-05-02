#include "lists.h"

/**
 * print_dlistint - print elements of list.
 * @h: head variable
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

#include "lists.h"

/**
 * dlistint_len - returns number of elements in a linked list.
 * @h: head variable
 * Return: number of elements
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t numnodes = 0;

	while (h != NULL)
	{
		numnodes++;
		h = h->next;
	}
	return (numnodes);
}

#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *mynode, *tmp, *help;

	mynode = malloc(sizeof(listint_t));
	if (!mynode)
		return (NULL);
	mynode->n = number;

	if (!*head || (*head)->n >= number /*verified head*/)
	{
		mynode->next = *head;
		*head = mynode;
		return(mynode)
	}
	tmp = *head;
	while(tmp->next)
	{
		if (number <= tmp->next->n && number > tmp->n)
			break;
		tmp = tmp->next;
	}
	help = temp->next;
	tmp->next = mynode;
	node->next = help;
	return(node);
}

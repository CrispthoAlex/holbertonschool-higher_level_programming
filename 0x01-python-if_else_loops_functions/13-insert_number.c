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
	listint_t *mynode, *tempo, *help;

	mynode = malloc(sizeof(listint_t));
	if (!mynode)
		return (NULL);
	mynode->n = number;

	if (!*head || (*head)->n >= number /*verified head*/)
	{
		mynode->next = *head;
		*head = mynode;
		return(mynode);
	}
	tempo = *head;
	while(tempo->next)
	{
		if (number <= tempo->next->n && number > tempo->n)
			break;
		tempo = tempo->next;
	}
	help = tempo->next;
	tempo->next = mynode;
	mynode->next = help;
	return(mynode);
}

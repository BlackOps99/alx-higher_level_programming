#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 1 if it's a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *second_half, *prev = *head, *temp = NULL;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	if (fast != NULL)
		slow = slow->next;

	second_half = slow;
	prev->next = NULL;

	while (second_half != NULL)
	{
		temp = second_half->next;
		second_half->next = prev;
		prev = second_half;
		second_half = temp;
	}

	temp = *head;
	while (prev != NULL)
	{
		if (temp->n != prev->n)
		{
			is_palindrome = 0;
			break;
		}
		temp = temp->next;
		prev = prev->next;
	}
	return (is_palindrome);
}

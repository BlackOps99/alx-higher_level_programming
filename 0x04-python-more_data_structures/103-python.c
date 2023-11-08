#include <Python.h>
/**
 * print_python_list - Prints information about a Python list
 * @p: Python Object representing a list
 * Return: No return value
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *element = PyList_GetItem(p, i);

		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
	}
}

/**
 * print_python_bytes - Prints information about a
 * Python bytes object
 * @p: Python Object representing bytes
 * Return: No return value
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t size = PyBytes_Size(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n",
	PyUnicode_Decode_ASCII(PyBytes_AsString(p), size, "strict"));

	printf("  first %ld bytes: ", (size < 10) ? size : 10);
	for (Py_ssize_t i = 0; i < ((size < 10) ? size : 10); i++)
	{
		printf("%02x%s",
		(unsigned char)PyBytes_AsString(p)[i], (i == 9) ? "\n" : " ");
	}
}

#include <stdio.h>
#include <Python.h>

/**
* print_python_bytes - Print information about Python bytes objects.
* @p: Python object representing bytes.
* Return: Nothing.
**/
void print_python_bytes(PyObject *p)
{
	char *s;
	Py_ssize_t len, i;

	printf("[.] Bytes Object Info\n");
	if (!PyBytes_Check(p))
		printf("  [ERROR] Invalid Bytes Object\n");
	else
	{
		PyBytes_AsStringAndSize(p, &s, &len);
		printf("  Size: %lu\n", len);
		printf("  Attempted String: %s\n", s);
		if (len > 10)
			len = 10;
		else
			len++;
		printf("  First %lu Bytes: ", len);
		for (i = 0; i < len - 1; i++)
			printf("%02x ", s[i] & 0xff);
		printf("%02x\n", s[len - 1] & 0xff);
	}
}

/**
* print_python_list - Print information about Python lists and their elements.
* @p: Python object representing a list.
* Return: Nothing.
**/
void print_python_list(PyObject *p)
{
	Py_ssize_t i;
	PyObject *in_list;

	if (PyList_Check(p))
	{
		printf("[*] Python List Info\n");
		printf("[*] Size of the List: %lu\n", PyList_Size(p));
		printf("[*] Allocated Memory: %lu\n", ((PyListObject *)p)->allocated);
		for (i = 0; i < PyList_Size(p); i++)
		{
			in_list = PySequence_GetItem(p, i);
			printf("Element %lu Type: %s\n", i,
			       in_list->ob_type->tp_name);
			if (strcmp(in_list->ob_type->tp_name, "bytes") == 0)
				print_python_bytes(in_list);
		}
	}
}

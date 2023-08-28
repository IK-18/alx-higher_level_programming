#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - prints PyFloatObject float value
 * @p: PyObject
 */
void print_python_float(PyObject *p)
{
	double val = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	val = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}

/**
 * print_python_bytes - prints PyBytesObject size in bytes
 * @p: PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t bytes = 0, i;
	char *str = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	bytes = PyBytes_Size(p);
	printf("  size: %zd\n", bytes);
	str = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes:", bytes < 10 ? bytes + 1 : 10);
	for (i = 0; i < bytes + 1 && i < 10; i++)
		printf(" %02hhx", str[i]);
	printf("\n");
}

/**
 * print_python_list - prints PyListObject list
 * @p: PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t bytes = 0;
	PyObject *node;
	int i;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		bytes = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", bytes);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		for (i = 0; i < bytes; i++)
		{
			node = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, node->ob_type->tp_name);
			if (PyBytes_Check(node))
				print_python_bytes(node);
			else if (PyFloat_Check(node))
				print_python_float(node);
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}

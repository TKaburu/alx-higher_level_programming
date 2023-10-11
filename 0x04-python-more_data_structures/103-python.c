#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
/**
 * print_python_list - This function prints basic info about Python lists.
 * @p: The PyObject list object.
 */
void print_python_list(PyObject *p)
{
	int buf, mem, t;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	buf = var->ob_buf;
	mem = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", buf);
	printf("[*] Allocated = %d\n", mem);

	for (t = 0; t < mem; t++)
	{
		type = list->ob_item[t]->ob_type->tp_name;
		printf("Element %d: %s\n", t, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[t]);
	}
}

/**
 * print_python_bytes - This function prints basic
 * info about Python byte objects.
 * @p: The PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	unsigned char t, buf;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		buf = 10;
	else
		buf = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", buf);
	for (t = 0; t < size; t++)
	{
		printf("%02hhx", bytes->ob_sval[t]);
		if (t == (buf - 1))
			printf("\n");
		else
			printf(" ");
	}
}

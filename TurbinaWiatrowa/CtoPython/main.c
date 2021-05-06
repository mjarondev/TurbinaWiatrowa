
#include <Python.h>

#include "wiatrakDeploy.h"

static PyObject *ObliczMoc(PyObject *self, PyObject *args)
{

    float predkoscWiatru, katGoraDol, katLewoPrawo;
    float flagaSzybko;

    if(!PyArg_ParseTuple(args, "fff", &predkoscWiatru, &katGoraDol, &katLewoPrawo))
    {
        return NULL;
    }

    wiatrakDeploy_U.windspeed = predkoscWiatru;
    wiatrakDeploy_U.katzadany = katGoraDol;
    wiatrakDeploy_U.KatWianiaWiatruLewoPrawo = katLewoPrawo;
    wiatrakDeploy_step();

    PyObject *lista = PyList_New(6);
    PyList_SetItem(lista, 0, PyFloat_FromDouble(wiatrakDeploy_Y.P));
    PyList_SetItem(lista, 1, PyFloat_FromDouble(wiatrakDeploy_Y.RPM));
    PyList_SetItem(lista, 2, PyFloat_FromDouble(wiatrakDeploy_Y.CzolowaPredkoscWiatru));
    PyList_SetItem(lista, 3, PyFloat_FromDouble(wiatrakDeploy_Y.KatPitchWzgledemPunktuStartoweg));
    PyList_SetItem(lista, 4, PyFloat_FromDouble(wiatrakDeploy_Y.KatNaseliWzgledemPunktuStartowe));
    PyList_SetItem(lista, 5, PyFloat_FromDouble(wiatrakDeploy_Y.Hamulec));

    return lista;

}

static PyMethodDef WiatrakMethods[] = {
{"obliczMoc", ObliczMoc, METH_VARARGS, "Python interface for calculate wind turbine power and rpm based on wind speed and wind angle"},
{NULL, NULL, 0, NULL}
};

static struct PyModuleDef wiatrakModule = {
PyModuleDef_HEAD_INIT,
"wiatrak",
"Python interface for calculate wind turbine power and rpm based on wind speed and wind angle",
-1,
WiatrakMethods
};

PyMODINIT_FUNC PyInit_wiatrak(void)
{
    wiatrakDeploy_initialize();
    return PyModule_Create(&wiatrakModule);
}



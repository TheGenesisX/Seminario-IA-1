#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main(void){
	int opcion = 0;

	do{
		cout<<"----------MENU----------"<<endl;
		cout<<"|1. Ingresar datos.    |"<<endl;
		cout<<"|2. Mostrar datos.     |"<<endl;
		cout<<"|3. Salir.             |"<<endl;
		cout<<"------------------------"<<endl<<endl;
		cout<<"Opcion: ";
		cin>>opcion;

		switch(opcion){
			case 1:
				void ingresarDatos();
				break;
			case 2:
				void mostrarDatos();
				break;
			case 3:
				break;
			default:
				cout<<"Opcion no valida";
				break;

		}
	}while(opcion != 3)
}
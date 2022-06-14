#include <iostream>
using namespace std;

int main(){
	
	cout<<"Project Based Learning Group-A\n\n";
	
	/*User Input*/
	int InputMaterial, InputFaseMaterial;
	float InputTemperatur;
	
	cout<<"Pilih material berdasarkan nomor.\n 1. Air\n 2. Refrigerant 134-a\n 3. Ammonia\n\nNomor : ";cin>>InputMaterial;
	if ((InputMaterial <= 0) || (InputMaterial >= 4)){
		cout<<"\nProgram Error. Pilih nomor yang benar!";
		exit(0);
	}
	cout<<"\nPilih fasa material berdasarkan nomor.\n 1. Cair (Liquid)\n 2. Uap (Vapor)\n\nNomor : ";cin>>InputFaseMaterial;
	if ((InputFaseMaterial <= 0) || (InputFaseMaterial >= 3)){
		cout<<"\nProgram Error. Pilih nomor yang benar!";
		exit(0);
	}
	
	
	//Meng-output rentang temperatur agar user tahu temperatur yang dapat dimasukkan.
		if (InputMaterial == 1){
			cout<<"\nRentang temperatur untuk Air = 0.01\370C - 200\370C\n";
		}
		else if (InputMaterial == 2){
			cout<<"\nRentang temperatur untuk Refrigerant 134-a = -40\370C - 100\370C";
		}
		else if (InputMaterial == 3){
			cout<<"\nRentang temperatur untuk Ammonia = -40\370C - 100\370C";
		}
	
	
	cout<<"\n\nInput temperatur material dalam (\370C) : ";cin>>InputTemperatur;
	if (InputMaterial == 1){
		if ((InputTemperatur < 0.01) || (InputTemperatur > 200)){
			cout<<"\nTemperatur yang dimasukkan tidak dapat dihitung untuk material Air.";
			exit(0);
		}
	}
	else if (InputMaterial == 2){
		if ((InputTemperatur < -40) || (InputTemperatur > 100)){
			cout<<"\nTemperatur yang dimasukkan tidak dapat dihitung untuk material Refrigerant 134-a.";
			exit(0);
		}
	}	
	else if (InputMaterial == 2){
	if ((InputTemperatur < -40) || (InputTemperatur > 100)){
		cout<<"\nTemperatur yang dimasukkan tidak dapat dihitung untuk material Ammonia.";
		exit(0);
		}
	}
	
	return 0;
}

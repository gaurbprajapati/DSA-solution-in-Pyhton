


#include<iostream>
#include<string>
using namespace std;


int selection_sort(int array[],int n){

    for (int i=0;i<n;i++){
        for (int j=i;j<n+1;j++){
            if (array[i]>array[j]){
                int temp=array[i];
                array[i]=array[j];
                array[j]=temp;

            }

        }
    }
    cout<<"The sorted array"<<endl;
    
    for(int m=0;m<n;m++){
        cout<<array[m]<<endl;
    }



    return 0;

}

int main(){

    int n;cout<<"the number of elemenyt in array:-";cin>>n;

    int array[n];


    cout<<"The unsorted array:-"<<endl;
    
    for (int i=0;i<n;i++){
        cin>>array[i];
    }


    selection_sort(array,n);


 
    
    
    return 0;
}
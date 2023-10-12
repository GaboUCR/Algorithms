#include <stdio.h>
#include <stdlib.h>
#include "LinkedList.h"

node* nuevo (int valor) {

    node* nuevo_elemento = malloc(sizeof(node));
    nuevo_elemento->value = valor;
    nuevo_elemento->next = NULL;
    
    return nuevo_elemento;    
} 

void imprimir_lista (LinkedList* lista) {

    node * cur = lista->head;
    printf("\n[");

    for (int i = 0; i < lista->len; i++) {

        if (i == lista->len -1) {
            printf("%d",cur->value);
            break;
        }
        printf("%d,", cur->value);

        cur = cur->next;
    }

    printf("]\n");
}

int insertar (LinkedList* lista, int valor) {

    if (lista->len == 0) {
        lista->head = nuevo(valor);
        lista->len++;  

        return 1;
    }

    node * cur = lista->head;

    for (int i = 0; i < lista->len -1; i++) {
        cur = cur->next;
    }

    cur->next = nuevo(valor);
    
    lista->len++;

    return 1;
}

int remover (LinkedList* lista, int indice) {

    node* cur;

    if (indice == 0) {
        cur = (lista->head);
        lista->head = cur->next;
        lista->len--;
        free(cur);
        return 1;
    }

    cur = lista->head;
    for (int i = 0; i < indice - 1; i++) {
        cur = cur->next;
    }
    
    node* del;
    del = cur->next;

    cur->next = (cur->next)->next;
    lista->len--;
    free(del);

    return 1;
}


int main() {

    LinkedList * lista = malloc(sizeof(LinkedList));
    lista->len = 0;
    lista->head = NULL;

    for (int i=0; i < 100; i++) {

        insertar(lista, i);
    }

    
    remover(lista, 0);
    

    imprimir_lista(lista);

    return 0;
}

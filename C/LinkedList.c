#include <stdio.h>
#include <stdlib.h>
#include "LinkedList.h"
#include <time.h> 

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

int bubble_sort(LinkedList* lista) {

    int swaps = 0;
    node* cur;
    node* nxt;
    node* prev;

    while (1) {

        cur = lista->head;
        for (int i =0; i < lista->len-1; i++) {

            if (cur->value > (cur->next)->value) {

                if (i == 0) {
                    
                    nxt = (cur->next)->next;
                    lista->head = cur->next;
                    (lista->head) -> next = cur;
                    cur->next = nxt;
                    prev = lista->head; 
                }
                else {

                    prev->next = cur->next;
                    nxt = (cur->next)->next;
                    cur->next = nxt;
                    (prev->next)->next = cur;

                    prev = prev->next;
                }
                swaps++;
                continue;
            }
            prev = cur;
            cur = cur->next;
        }

        if (swaps == 0) {
            break;
        }
        else {
            swaps = 0;
        }
    }

    return 1;
}

#include <time.h> // Para time y rand

// Genera una lista con valores aleatorios
LinkedList* generar_lista_aleatoria(int len) {
    LinkedList* lista = malloc(sizeof(LinkedList));
    lista->len = 0;
    lista->head = NULL;

    for (int i = 0; i < len; i++) {
        int valor = rand() % 1000;  // genera números entre 0 y 999
        insertar(lista, valor);
    }

    return lista;
}

void test_bubble_sort() {
    // 1. Caso: Lista ordenada ascendentemente
    LinkedList* caso1 = malloc(sizeof(LinkedList));
    caso1->len = 0;
    caso1->head = NULL;
    for (int i = 0; i < 10; i++) {
        insertar(caso1, i);
    }
    printf("Caso 1: Lista ordenada ascendentemente\n");
    imprimir_lista(caso1);
    bubble_sort(caso1);
    imprimir_lista(caso1);

    // 2. Caso: Lista ordenada descendentemente
    LinkedList* caso2 = malloc(sizeof(LinkedList));
    caso2->len = 0;
    caso2->head = NULL;
    for (int i = 9; i >= 0; i--) {
        insertar(caso2, i);
    }
    printf("Caso 2: Lista ordenada descendentemente\n");
    imprimir_lista(caso2);
    bubble_sort(caso2);
    imprimir_lista(caso2);

    // 3. Caso: Elementos iguales
    LinkedList* caso3 = malloc(sizeof(LinkedList));
    caso3->len = 0;
    caso3->head = NULL;
    for (int i = 0; i < 10; i++) {
        insertar(caso3, 5);
    }
    printf("Caso 3: Todos los elementos son iguales\n");
    imprimir_lista(caso3);
    bubble_sort(caso3);
    imprimir_lista(caso3);

    // 4. Caso: Un solo elemento
    LinkedList* caso4 = malloc(sizeof(LinkedList));
    caso4->len = 0;
    caso4->head = NULL;
    insertar(caso4, 7);
    printf("Caso 4: Un solo elemento\n");
    imprimir_lista(caso4);
    bubble_sort(caso4);
    imprimir_lista(caso4);

    // 5. Caso: Lista vacía
    LinkedList* caso5 = malloc(sizeof(LinkedList));
    caso5->len = 0;
    caso5->head = NULL;
    printf("Caso 5: Lista vacía\n");
    imprimir_lista(caso5);
    bubble_sort(caso5);
    imprimir_lista(caso5);

    // 6. Caso: Lista aleatoria
    LinkedList* caso6 = generar_lista_aleatoria(10);
    printf("Caso 6: Lista aleatoria\n");
    imprimir_lista(caso6);
    bubble_sort(caso6);
    imprimir_lista(caso6);
}

int main() {
    srand(time(NULL));  // inicializa el generador de números aleatorios

    test_bubble_sort();

    return 0;
}

// int main() {

//     LinkedList * lista = malloc(sizeof(LinkedList));
//     lista->len = 0;
//     lista->head = NULL;

//     insertar(lista, 1);
//     insertar(lista, 0);
//     insertar(lista, 10);
//     insertar(lista, 111);
//     insertar(lista, 2353);
//     insertar(lista, 4);
//     insertar(lista, 31);
//     insertar(lista, 4532);
//     // for (int i=0; i < 100; i++) {

//     //     insertar(lista, i);
//     // }

    
//     // remover(lista, 50);
    

//     imprimir_lista(lista);

//     bubble_sort(lista);

//     imprimir_lista(lista);

//     return 0;
// }

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/yQPZ0SBC)


## Testes single threaded:

Requisições | Single Threaded (Serv+Clien) | Multitreaded (Serv+Client) | Multithreaded (Serv) |
-|-|-|-|
100_000 | 77.8804s | 78.1447s | |
10_000 | 7.0706s | 5.1915s | |
1_000 | 0.6868s | 1.3289s | | 

## Conclusão

Apesar do multithreading rodar mais rapido inicialmente,
quando o numero de requisições aumenta muito o servidor e o cliente
começam a mandar/receber requisições mais lentamente. Provavelmente
isso é causado por overhead de uso de uma thread por requisição;
Já o single threaded segue no mesmo ritmo do começo ao fim.

<img src="media/multithread.gif" />
<img src="media/singlethread.gif" />

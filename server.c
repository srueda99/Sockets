#include <stdio.h>
#include <arpa/inet.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>

int main()
{
    int sock;
    struct sockaddr_in serv_addr;
    char buffer[128];

    sock = socket(AF_INET, SOCK_STREAM, 0);

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(5000);

    inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr);
    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0)
    {
        printf("Error en la conexión\n");
        return -1;
    }

    while (1)
    {
        fgets(buffer, 128, stdin);
        send(sock, buffer, strlen(buffer), 0);
    }

    return 0;
}
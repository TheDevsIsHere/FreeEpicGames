#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <time.h>

int main()
{
    time_t now = time(NULL);
    struct tm *local = localtime(&now);

    if (local->tm_hour > 14)
    {
        printf("Buonasera, sono le: %02d:%02d:%02d\n", local->tm_hour, local->tm_min, local->tm_sec);
    }
    else
    {
        printf("Buongiorno, sono le: %02d:%02d:%02d\n", local->tm_hour, local->tm_min, local->tm_sec);
    }

    int tm_wday = local->tm_wday; // Giorno della settimana (0 = Domenica, ..., 3 = Mercoledì, 4 = Giovedì)

    if (tm_wday == 3)
    {
        printf("È mercoledì: ci dovrebbero essere giochi su Epic da prendere!\n");
        Sleep(2000);
        system("start https://store.epicgames.com/it-IT/free-games?lang=it-IT");
    }
    else if (tm_wday == 4)
    {
        printf("È giovedì: ultimo giorno per riscattare i giochi da Epic!\n");
        Sleep(2000);
        system("start https://store.epicgames.com/it-IT/free-games?lang=it-IT");
    }
    else
    {
        printf("Nessun gioco da riscattare oggi.\n");
        Sleep(2000);
    }

    return 0;
}

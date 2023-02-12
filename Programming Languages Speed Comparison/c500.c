#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <sys/time.h>
int main()
{
    struct timeval start, end;
    FILE *filePointer;
    FILE *filePointerr;
    char ch;
    filePointer = fopen("500MB.txt", "r");
    gettimeofday(&start, NULL);
    if (filePointer == NULL)
    {
        printf("File is not available \n");
    }
    else
    {
        while ((ch = fgetc(filePointer)) != EOF)
        {
            ch=toupper(ch);
        }
    }
    gettimeofday(&end, NULL);
    double time_taken;
    fclose(filePointer);
    time_taken = (end.tv_sec - start.tv_sec) * 1e6;
    time_taken = (time_taken + (end.tv_usec - start.tv_usec)) * 1e-6;
    printf("C : %.2f \n",time_taken); 
    filePointerr = fopen("C.txt", "a");
    fprintf(filePointerr, "%.2f",time_taken);
    fprintf(filePointerr, "\n");
    fclose(filePointerr);
    return 0;
}
#include "../Kernel/kernel.h"

int buffer=0;

void task1()
{ 
  nkprint("\nsou a task 1 e o buffer vale%d\n",buffer);
  buffer=1;
  int i;
  for(i = 0; i < 1000; i++)
  {
    buffer++;
  }
  nkprint("\ntask1 a= %d",buffer);
  taskexit();
}
void task2()
{ 
  nkprint("\nsou a task 2 e o buffer vale%d\n",buffer);
  buffer=2;
  int i;
  for(i = 0; i < 1000; i++)
  {
    buffer++;
  }
  nkprint("\ntask2 a= %d",buffer);
  taskexit();
}
void task3()
{ 
  nkprint("\nsou a task 3 e o buffer vale%d\n",buffer);
  buffer=3;
  int i;
  for(i = 0; i < 1000; i++)
  {
    buffer++;
  }
  nkprint("\ntask3 a= %d",buffer);
  taskexit();
}
int main (int argc, char *argv[])
{
  int t1,t2,t3;
  taskcreate(&t1,task1);
  taskcreate(&t2,task2);
  taskcreate(&t3,task3);
  start(FIFO);
  return 0;
}

#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#define n 3
int stack[n],top=-1;
void push()
{
    int x;
    if(top==n-1)
    {
        printf("stack overflow");
    }
    else
    {
        printf("enter number to push");
        scanf("%d",&x);

        top++;
        stack[top]=x;
    }

}
void peek()
{
    int i;
    printf("enter number yo peep");
    scanf("%d",&i);
    if((top-i+1)<=0)
    {
        printf("stack underflow for entered element");
    }
    else
    {
        printf("%d",stack[top-i+1]);
    }
}
void pop()
{
    if(top==-1)
    {
        printf("stack underflow:");
    }
    else
    {
        printf("deleted element:%d",stack[top]);
        top--;
    }
}
void change()
{
    int c,ne;
    printf("enter number yo peep");
    scanf("%d",&c);
    if((top-c+1)<=0)
    {
        printf("stack underflow for entered element");
    }
    else
    {
        printf("enter value to be replaced:");
        scanf("%d",&ne);

        stack[top-c+1]=ne;
    }
}
void dis()
{
    if(top==-1)
    {
        printf("stack underflow");
    }
    else
    {
        int i;
        for(i=top;i>=0;i++)
        {
            printf("%d\n",stack[i]);
        }
    }
}

void main()
{
    int ch;
    while(1)
    {
        printf("enter: 1 for push\n\t 2 for pop \n\t 3 for peep \n\t 4 for change \n\t 5 for display \n\t 6 for exit");
    scanf("%d",&ch);

    switch(ch)
    {
    case 1:
        push();
        break;

    case 2:
        pop();
        break;

    case 3:
        peek();
        break;

    case 4:
        change();
        break;

    case 5:
        dis();
        break;

    case 6:
        exit(0);

    }
    }
}

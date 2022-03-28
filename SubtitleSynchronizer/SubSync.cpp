#include<bits/stdc++.h>
using namespace std;
int main()
{
    while(1)
    {
    int sec=-6,msec=-500,index=1;
    char path[MAX_PATH],New_path[MAX_PATH];
    bool print=false,cpy=false;
    cout<<"Enter Address of the Target Subtitle File:";
    cin>>path;
/******************************Extraction****************************/
    ifstream fs(path);
    if(fs.is_open())
    {
        for(int i=strlen(path)-1;i>=0;i--)
        {
            if(cpy==true)
            New_path[i]=path[i];
            if(path[i]=='.')
                cpy=true;
        }
        strcat(New_path,"-Synced.srt");
        cout<<"Enter Second-Shift:";
        cin>>sec;
        cout<<"Enter MilliSecond-Shift:";
        cin>>msec;
        cout<<"Extracting...\n";
        ofstream mf(New_path);
        while(!fs.eof())
        {
        string gh;
        getline(fs,gh);
        if(gh.c_str()[0]=='0')
        {
            int seq[2][4];
            char buf[4],l[50];
            strcpy(l,gh.c_str());
            int ind=0,sqn=0;
            while(l[0]!='\0')
            {
                stringstream(l)>>seq[sqn][ind];
                ind++;
                if(ind>3)
                {
                    sqn=1;
                    ind=0;
                }
                int i,j;
                bool cpy=false;
                for(i=0;i<strlen(l);i++)
                    {
                        if(l[i]<'0'||l[i]>'9')
                        cpy=true;
    if((l[i]>='0'&&l[i]<='9'&&cpy==true)||l[i]=='\0')
                            break;
                    }
                for(j=i;j<strlen(l);j++)
                    l[j-i]=l[j];
                l[j-i]='\0';
            }
/****************************Update****************************/
            for(int i=0;i<2;i++)
            {
                int time=0;
                time+=seq[i][0]*3600000;
                time+=seq[i][1]*60000;
                time+=seq[i][2]*1000;
                time+=seq[i][3];
                time+=(sec*1000+msec);
                if(time<0)
                {
                    print=false;
                    goto endh;
                }
                print=true;
                seq[i][0]=time/3600000;
                time=time%3600000;
                seq[i][1]=time/60000;
                time=time%60000;
                seq[i][2]=time/1000;
                time=time%1000;
                seq[i][3]=time;
            }
/****************************Rebuilding****************************/
char source[50]={};
bool junk=false;
for(int j=0;j<2;j++)
{
for(int i=0;i<3;i++)
{
    char buf[4];
    sprintf(buf,"%d",seq[j][i]);
    if(strlen(buf)<2)
        strcat(source,"0");
    strcat(source,buf);
        strcat(source,":");
}
char buf[4];
    sprintf(buf,"%d",seq[j][3]);
    if(strlen(buf)==1)
        strcat(source,"00");
    else if(strlen(buf)==2)
        strcat(source,"0");
    strcat(source,buf);
if(junk==false)
{
    junk=true;
    strcat(source," --> ");
}
}
mf<<index<<endl;
index++;
mf<<source<<endl;
        }
else if(gh.c_str()[0]>='1'&&gh.c_str()[0]<='9')
    continue;
        else
            if(print==true)
            mf<<gh<<endl;
        endh:
            print=print;
        }
        cout<<"Extraction Completed!\nUpdating...\n";
        cout<<"Synchronization Completed!\n";
        mf.close();
        fs.close();
    }
    else
        cout<<"File Not Found!\n";
    }
}

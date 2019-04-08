function Q=projection_error(fi,Af,x0,y0,R)
%Af=Af(:,:,1);
P=zeros(3,3,1002001);
%P=zeros(3,3,1);
COS=cos(fi);
SIN=sin(fi);
%Kada pristupamo elementima Af peko maske, ne mozemo da definisemo masku kao
%mask=Af>..., pa onda Af(mask & mask1), vec moramo A=Af(i,j,:), pa A(mask).

        
% P1=zeros(1,1);
%         fill=ones(1,1);
%         P1P2=zeros(1,1); DP1=zeros(1,1);
%         DP2=zeros(1,1); AP1=zeros(1,1);
%pocetna tacka
for i=1:3
    for j=1:3
        P1=zeros(1,1002001);
        fill=ones(1,1002001);
        P1P2=zeros(1,1002001); DP1=zeros(1,1002001);
        DP2=zeros(1,1002001);  AP1=zeros(1,1002001);
        A=Af(i,j,:);
        mask = A>0;
            mask1 = A<tan(fi)/2; %trougao 
            
                P1P2(mask & mask1)=sqrt(max(0,(2*(A(mask & mask1)))./(cos(fi)*sin(fi)))); DP1(mask & mask1)=P1P2(mask & mask1)*cos(fi);  %DP2=P1P2*sin(fi); %proveriti P1P2
                P1(mask & mask1)=[i*fill(mask & mask1)',(j-DP1(mask & mask1))']*[COS;SIN];                                               %P2=[i-DP2,j]*[cos(fi),sin(fi)]';
            
            mask2 = (A>=tan(fi)/2 & A<=1-tan(fi)/2); %trapez
                
                DP2(mask & mask2)=tan(fi); AP1(mask & mask2)=(2*A(mask & mask2)-tan(fi))/2;                                              %BP2=(2*Af(i,j,l)+tan(fi))/2; 
                P1(mask & mask2)=[(i-AP1(mask & mask2))',(j*fill(mask & mask2)-1)']*[COS;SIN];                                           %P2=[i-BP2,j]*[cos(fi),sin(fi)]';
            
            mask3 = (A>1-tan(fi)/2); %dopunjen trougao
                
                P1P2(mask & mask3)=sqrt(max(0,2*(1-(A(mask & mask3)))/(cos(fi)*sin(fi)))); DP1(mask & mask3)=P1P2(mask & mask3)*sin(fi); %DP2=P1P2*cos(fi); 
                 P1(mask & mask3)=[(i-1+DP1(mask & mask3))',(j*fill(mask & mask3)-1)']*[COS;SIN];                                                    
                %P1=[i-1+sqrt(2*(1-Af(i,j,l))*tan(fi)),j-1]*[cos(fi),sin(fi)]';   %proverirti ovaj red 2
            
            mask4 = (Af(i,j,:)==0);
            
            P1(mask4)=3*sqrt(2); %ako je vrednost pixela 0, projekciju postavljamo na maximum
            P(i,j,:)=P1;
            end
        end
        
 l=1:1002001;
 proj(l)=roundn(min(min(P(:,:,l))),-15);
 Q=roundn((proj'-([x0',y0']*[cos(fi),sin(fi)]'-R)),-12);
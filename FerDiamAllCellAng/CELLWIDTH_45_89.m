function cellWidth_45_89=CELLWIDTH_45_89(fi,I)

Af=I;
[w,h] = size(Af(:,:,1));

COS=cos(fi);
SIN=sin(fi);

P=ones(w,h,368)*200;  

%minimal projection
for i=1:round(w/2)+2
    for j=1:round(h/2)+2
        P1=zeros(1,368);
        fill=ones(1,369);
        P1P2=zeros(1,368); DP1=zeros(1,368);
        DP2=zeros(1,368);  AP1=zeros(1,368); 
        A=Af(i,j,:);
       mask = (A>0 & A<=1);
            mask1 = A<tan(pi/2-fi)/2; %triangle
                P1P2(mask & mask1)=sqrt(max(0,(2*(A(mask & mask1)))./(cos(pi/2-fi)*sin(pi/2-fi)))); DP1(mask & mask1)=P1P2(mask & mask1)*cos(pi/2-fi);  
                P1(mask & mask1)=[(i-DP1(mask & mask1))',(j*fill(mask & mask1))']*[COS;SIN];                                              
            mask2 = (A>=tan(pi/2-fi)/2 & A<=1-tan(pi/2-fi)/2); %trapeze
                DP2(mask & mask2)=tan(pi/2-fi); AP1(mask & mask2)=(2*A(mask & mask2)-tan(pi/2-fi))/2;                                              
                P1(mask & mask2)=[(i*fill(mask & mask2)-1)',(j-AP1(mask & mask2))']*[COS;SIN];                                           
            mask3 = (A>1-tan(pi/2-fi)/2); %pentagon
                P1P2(mask & mask3)=sqrt(max(0,2*(1-(A(mask & mask3)))/(cos(pi/2-fi)*sin(pi/2-fi)))); DP1(mask & mask3)=P1P2(mask & mask3)*sin(pi/2-fi); 
                P1(mask & mask3)=[(i*fill(mask & mask3)-1)',(j-1+DP1(mask & mask3))']*[COS;SIN];                                                    
            mask4 = (A<=0 | A>1);
                P1(mask4)=400;
        P(i,j,:)=P1;
    end
end
        
l=1:368;
projMin(l)=roundn(min(min(P(:,:,l))),-15);

P=zeros(w,h,368);
%maximal projection
  for i=round(w/2)-2:w
    for j=round(h/2)-2:h
        P1=zeros(1,368);
        fill=ones(1,368);
        P1P2=zeros(1,368); DP1=zeros(1,368);
        DP2=zeros(1,368);  AP1=zeros(1,368);
        A=1-Af(i,j,:);
        mask = (A>=0 & A<1);
            mask1 = A<tan(pi/2-fi)/2; %triangle 
                P1P2(mask & mask1)=sqrt(max(0,(2*(A(mask & mask1)))./(cos(pi/2-fi)*sin(pi/2-fi)))); DP1(mask & mask1)=P1P2(mask & mask1)*cos(pi/2-fi);  
                P1(mask & mask1)=[(i-DP1(mask & mask1))',(j*fill(mask & mask1))']*[COS;SIN];                                               
            mask2 = (A>=tan(pi/2-fi)/2 & A<=1-tan(pi/2-fi)/2); %trapeze
                DP2(mask & mask2)=tan(pi/2-fi); AP1(mask & mask2)=(2*A(mask & mask2)-tan(pi/2-fi))/2;                                              
                P1(mask & mask2)=[(i*fill(mask & mask2)-1)',(j-AP1(mask & mask2))']*[COS;SIN];                                           
            mask3 = (A>1-tan(pi/2-fi)/2); %pentagon
                P1P2(mask & mask3)=sqrt(max(0,2*(1-(A(mask & mask3)))/(cos(pi/2-fi)*sin(pi/2-fi)))); DP1(mask & mask3)=P1P2(mask & mask3)*sin(pi/2-fi); 
                P1(mask & mask3)=[(i*fill(mask & mask3)-1)',(j-1+DP1(mask & mask3))']*[COS;SIN];                                                    
            mask4 = (A>=1 | A<0);
            P1(mask4)=0; 
            P(i,j,:)=P1;
    end
end
        
l=1:368;
projMax(l)=roundn(max(max(P(:,:,l))),-15);
cellWidth_45_89=projMax-projMin;

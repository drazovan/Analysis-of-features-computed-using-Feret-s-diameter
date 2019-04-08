%POKUSAJ SA KRUGOM SA POZNATIM OBIMOM I KURVATUROM
%PROVERITI ellipseCover
%PROVERITI ErrF
%R1=rand(1,1000)-0.5; R2=rand(1,1000)-0.5;
%Teta=pi/4;
finalDiameter=[];
for K=1:0.5:100 K
for rot=90; %22.5%11:5:45 %0:90
R1=rand(1,1000); R2=rand(1,1000);
a=100; %b=10;
Kfinal=[];
ERRFERET=[];
ERR=[];
DIAMETER=[];
%rot=rot*pi/180;

    PerApp=[];
    Per=0;
    %b=20;
    b=sqrt(K*a);
    %b=90;
        xC=104-1/2+R1;
        yC=104-1/2+R2;
        I=elipseCoverRot(a,b,xC,yC); %ovde treba ellipseCoverBW
Diameter=0;
wFinal=[];
global J
global projMin
global projMax
ErrFeret=[];
for fi=0:45% 80%0:9:90 
    fi,K, rot
    fi=fi*pi/180;
    Width=elipseProjectionCenterBW(fi,I);
    ErrF=Width-sqrt((2*((a*b)/(sqrt(b^2+(tan(fi)*a)^2))))^2+(2*tan(fi)*(a*b)/(sqrt(b^2+(tan(fi)*a)^2)))^2);
    ErrF=Width-sin(fi)*2*sqrt((tan(pi/2+fi))^2*a^2+b^2);
    ErrFeret=vertcat(ErrFeret,ErrF);
    wFinal=vertcat(wFinal,Width);
    
end
for fi=46:90% 80%0:9:90 
    fi,K
    fi=fi*pi/180;
    Width=elipseProjectionCenterBW(fi,I);
    %ErrF=Width-sqrt((2*((a*b)/(sqrt(b^2+(tan(fi)*a)^2))))^2+(2*tan(fi)*(a*b)/(sqrt(b^2+(tan(fi)*a)^2)))^2);
%     if fi~=90*pi/180
%     ErrF=Width-sin(fi)*2*sqrt((tan(pi/2+fi))^2*a^2+b^2);
%     end
%     ErrFeret=vertcat(ErrFeret,ErrF);
    wFinal=vertcat(wFinal,Width);
    
    
 end
Diameter=max(wFinal);
Kfinal=horzcat(Kfinal,wFinal');


PerApp=pi*sum(wFinal)/90;    
%Per=4*a*mfun('EllipticE',(((a^2-b^2)/a^2))); %done with sqrt
Per=4*a*E;
PerErr=PerApp-Per;
ERR=vertcat(ERR,PerErr);
DIAMETER=vertcat(DIAMETER,Diameter);
ERRFERET=horzcat(ERRFERET,ErrFeret);
end
finalDiameter=vertcat(finalDiameter,DIAMETER);
end

%PUSTITI NA 100 ELIPSI


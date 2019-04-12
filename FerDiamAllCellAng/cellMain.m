%loading the data, i.e. pixel coverage of cells
load('coverSegm.mat')

I=coverSegm{1};

CellWidth_0_44=[];
for fi=0:44
    fi=fi*pi/180;
    width_0_44=CELLWIDTH_0_44(fi,I);
    CellWidth_0_44=vertcat(CellWidth_0_44,width_0_44);
end

CellWidth_45_89 = [];    
for fi=45:89
    fi=fi*pi/180;
    width_45_89=CELLWIDTH_45_89(fi,I);
    CellWidth_45_89=vertcat(CellWidth_45_89,width_45_89);
end

% rotating image for 90^o and reperating the computations is the same as
% continuing angle iterations to 91^o...180^o
I=imrotate(I,90); 
    
CellWidth_90_134=[];
for fi=0:44
    fi=fi*pi/180;
    width_0_44=CELLWIDTH_0_44(fi,I);
    CellWidth_90_134=vertcat(CellWidth_90_134,width_0_44);
end
    
CellWidth_135_179=[];
for fi=45:89
    fi=fi*pi/180;
    width_45_89=CELLWIDTH_45_89(fi,I);
    CellWidth_135_179=vertcat(CellWidth_135_179,width_45_89);
end

% matrix with columns representing width function for a cell
widthAllCells=[CellWidth_0_44;CellWidth_45_89;CellWidth_90_134;CellWidth_135_179];




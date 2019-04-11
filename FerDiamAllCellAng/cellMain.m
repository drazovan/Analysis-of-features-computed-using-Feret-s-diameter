%loading the data, i.e. pixel coverage of cells
load('coverSegm.mat')

I=coverSegm{1};

CellWidth_0_45=[];
for fi=0:44
    fi=fi*pi/180;
    width_0_45=CELLWIDTH_0_45(fi,I);
    CellWidth_0_45=vertcat(CellWidth_0_45,width_0_45);
end

CellWidth_46_90 = [];    
for fi=45:89
    fi=fi*pi/180;
    width_46_90=CELLWIDTH_46_90(fi,I);
    CellWidth_46_90=vertcat(CellWidth_46_90,width_46_90);
end

% rotating image for 90^o and reperating the computations is the same as
% continuing angle iterations to 91^o...180^o
I=imrotate(I,90); 
    
CellWidth_91_135=[];
for fi=0:44
    fi=fi*pi/180;
    width_0_45=CELLWIDTH_0_45(fi,I);
    CellWidth_91_135=vertcat(CellWidth_91_135,width_0_45);
end
    
CellWidth_136_180=[];
for fi=45:89
    fi=fi*pi/180;
    width_46_90=CELLWIDTH_46_90(fi,I);
    CellWidth_136_180=vertcat(CellWidth_136_180,width_46_90);
end

% matrix with columns representing width function for a cell
widthAllCells=[CellWidth_0_45;CellWidth_46_90;CellWidth_91_135;CellWidth_136_180];




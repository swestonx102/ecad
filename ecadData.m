clear all variables
close all
clc

data = readtable('ecad_data.csv')
data(1,:) = [];
data(:,1) = [];
name = table2array(data(1,:));
year = table2array(data(4,:));
lat = table2array(data(8,:));
long = table2array(data(9,:));

hold on

for i = 1:length(name)
    redness = (str2double(year(i)) - 1898)/106
    plot(str2double(lat(i)),str2double(long(i)),'x','color',[redness 0 1],'LineWidth',2);
    %text(str2double(lat(i)),str2double(long(i)),name(i))
    
end


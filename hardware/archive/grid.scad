
/*
Design to support touch screens and act as the anchoring point for metal rods making the 
bottom grid of a mouse cage.
Screens are from adafruit https://www.adafruit.com/product/1751
dimensions are: 206mm X 165mm

design by Andre M Chagas
CC BY SA 4.0
04/2023

*/

$fn=100;
tol = 0.1;



z_length = 40;
x_length = 206;
y_length =  2.9;

z_offset = 2.9;

r_hole = 1.5;
n_hole = 20;

x_offset_hole = 10;
y_offset_hole = 10;


grid = 1;


module grid(){
difference(){
cube([x_length,y_length,z_length]);

for ( i = [2.5:x_offset_hole:x_length]){
    translate([i,z_length/2,y_offset_hole])
    rotate([90,0,0]){
    cylinder(r=r_hole+tol,h=2*z_length);
    }//end rotate
    
    }//end for    
}//end difference
}


if (grid == 1){
    rotate([90,0,0]){
    grid();}
}//end rotate

